import os
import json
import tempfile
import subprocess
from pathlib import Path
from typing import Dict, List, Any, Optional
from google.adk.agents import Agent
import requests
from datetime import datetime

# For YouTube API
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

# For OpenAI TTS
import openai


def process_background_video(video_path: str, duration: int = 60) -> Dict[str, Any]:
    """Process background video for YouTube Shorts format."""
    try:
        if not os.path.exists(video_path):
            return {
                "status": "error", 
                "error_message": f"Video file not found: {video_path}"
            }
        
        # Create output filename
        output_path = f"processed_background_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
        
        # FFmpeg command for YouTube Shorts format (9:16 aspect ratio, max 60 seconds)
        ffmpeg_cmd = [
            'ffmpeg', '-i', video_path,
            '-vf', f'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920',
            '-t', str(duration),  # Limit to specified duration
            '-c:v', 'libx264', '-c:a', 'aac',
            '-b:v', '2M', '-b:a', '128k',
            '-movflags', '+faststart',
            '-y', output_path
        ]
        
        # Execute FFmpeg
        result = subprocess.run(ffmpeg_cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            return {
                "status": "success",
                "message": f"Video processed successfully: {output_path}",
                "output_path": output_path,
                "format": "9:16 (YouTube Shorts)",
                "duration": duration
            }
        else:
            return {
                "status": "error",
                "error_message": f"FFmpeg error: {result.stderr}"
            }
            
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error processing video: {str(e)}"
        }


def generate_tts_audio(transcript: str, voice: str = "alloy") -> Dict[str, Any]:
    """Generate text-to-speech audio from transcript using OpenAI."""
    try:
        # Check for OpenAI API key
        openai_key = os.getenv('OPENAI_API_KEY')
        if not openai_key:
            return {
                "status": "error",
                "error_message": "OpenAI API key not configured. Set OPENAI_API_KEY environment variable."
            }
        
        # Initialize OpenAI client
        client = openai.OpenAI(api_key=openai_key)
        
        # Create output filename
        audio_path = f"voiceover_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
        
        # Generate TTS
        response = client.audio.speech.create(
            model="tts-1",
            voice=voice,  # alloy, echo, fable, onyx, nova, shimmer
            input=transcript
        )
        
        # Save audio file
        response.stream_to_file(audio_path)
        
        return {
            "status": "success", 
            "message": f"TTS audio generated: {audio_path}",
            "audio_path": audio_path,
            "voice": voice,
            "transcript_length": len(transcript)
        }
        
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error generating TTS: {str(e)}"
        }


def combine_audio_video(video_path: str, audio_path: str, title: str = "YouTube Short") -> Dict[str, Any]:
    """Combine processed video with TTS audio."""
    try:
        if not os.path.exists(video_path) or not os.path.exists(audio_path):
            return {
                "status": "error",
                "error_message": "Video or audio file not found"
            }
        
        # Create output filename
        output_path = f"youtube_short_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
        
        # FFmpeg command to combine audio and video
        ffmpeg_cmd = [
            'ffmpeg', '-i', video_path, '-i', audio_path,
            '-c:v', 'copy', '-c:a', 'aac', '-b:a', '128k',
            '-map', '0:v:0', '-map', '1:a:0',
            '-shortest',  # Stop at shortest input (audio or video)
            '-movflags', '+faststart',
            '-y', output_path
        ]
        
        # Execute FFmpeg
        result = subprocess.run(ffmpeg_cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            return {
                "status": "success",
                "message": f"YouTube Short created: {output_path}",
                "output_path": output_path,
                "title": title,
                "ready_for_upload": True
            }
        else:
            return {
                "status": "error", 
                "error_message": f"FFmpeg error: {result.stderr}"
            }
            
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error combining audio/video: {str(e)}"
        }


def upload_to_youtube(video_path: str, title: str, description: str = "", tags: List[str] = None) -> Dict[str, Any]:
    """Upload video to YouTube using YouTube Data API."""
    try:
        # Check for YouTube credentials
        client_id = os.getenv('YOUTUBE_CLIENT_ID')
        client_secret = os.getenv('YOUTUBE_CLIENT_SECRET') 
        refresh_token = os.getenv('YOUTUBE_REFRESH_TOKEN')
        
        if not all([client_id, client_secret, refresh_token]):
            return {
                "status": "error",
                "error_message": "YouTube API credentials not configured. Need YOUTUBE_CLIENT_ID, YOUTUBE_CLIENT_SECRET, YOUTUBE_REFRESH_TOKEN"
            }
        
        if not os.path.exists(video_path):
            return {
                "status": "error",
                "error_message": f"Video file not found: {video_path}"
            }
        
        # Create YouTube API service
        credentials = Credentials(
            token=None,
            refresh_token=refresh_token,
            token_uri='https://oauth2.googleapis.com/token',
            client_id=client_id,
            client_secret=client_secret,
            scopes=['https://www.googleapis.com/auth/youtube.upload']
        )
        
        youtube = build('youtube', 'v3', credentials=credentials)
        
        # Video metadata
        body = {
            'snippet': {
                'title': title,
                'description': description,
                'tags': tags or ['shorts', 'ai', 'automation'],
                'categoryId': '22'  # People & Blogs
            },
            'status': {
                'privacyStatus': 'public',  # or 'private', 'unlisted'
                'selfDeclaredMadeForKids': False
            }
        }
        
        # Create media upload
        media = MediaFileUpload(
            video_path,
            chunksize=-1,
            resumable=True,
            mimetype='video/mp4'
        )
        
        # Upload video
        request = youtube.videos().insert(
            part=','.join(body.keys()),
            body=body,
            media_body=media
        )
        
        response = request.execute()
        
        video_id = response['id']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        
        return {
            "status": "success",
            "message": f"Video uploaded successfully!",
            "video_id": video_id,
            "video_url": video_url,
            "title": title
        }
        
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error uploading to YouTube: {str(e)}"
        }


def create_youtube_short(video_path: str, transcript: str, title: str, description: str = "", voice: str = "alloy", tags: List[str] = None) -> Dict[str, Any]:
    """Complete pipeline: Create and upload YouTube Short."""
    try:
        results = {"pipeline_steps": []}
        
        # Step 1: Process background video
        print("🎬 Step 1: Processing background video...")
        video_result = process_background_video(video_path, duration=60)
        results["pipeline_steps"].append({"step": "video_processing", "result": video_result})
        
        if video_result["status"] == "error":
            return {
                "status": "error",
                "error_message": f"Video processing failed: {video_result['error_message']}",
                "pipeline_results": results
            }
        
        processed_video = video_result["output_path"]
        
        # Step 2: Generate TTS audio
        print("🎤 Step 2: Generating TTS audio...")
        audio_result = generate_tts_audio(transcript, voice)
        results["pipeline_steps"].append({"step": "tts_generation", "result": audio_result})
        
        if audio_result["status"] == "error":
            return {
                "status": "error", 
                "error_message": f"TTS generation failed: {audio_result['error_message']}",
                "pipeline_results": results
            }
        
        audio_file = audio_result["audio_path"]
        
        # Step 3: Combine audio and video
        print("🎞️ Step 3: Combining audio and video...")
        combine_result = combine_audio_video(processed_video, audio_file, title)
        results["pipeline_steps"].append({"step": "audio_video_combine", "result": combine_result})
        
        if combine_result["status"] == "error":
            return {
                "status": "error",
                "error_message": f"Audio/video combination failed: {combine_result['error_message']}",
                "pipeline_results": results
            }
        
        final_video = combine_result["output_path"]
        
        # Step 4: Upload to YouTube
        print("📤 Step 4: Uploading to YouTube...")
        upload_result = upload_to_youtube(final_video, title, description, tags)
        results["pipeline_steps"].append({"step": "youtube_upload", "result": upload_result})
        
        if upload_result["status"] == "error":
            return {
                "status": "partial_success",
                "message": f"YouTube Short created but upload failed: {upload_result['error_message']}",
                "final_video_path": final_video,
                "pipeline_results": results
            }
        
        # Success!
        return {
            "status": "success",
            "message": "YouTube Short created and uploaded successfully!",
            "video_url": upload_result["video_url"],
            "video_id": upload_result["video_id"],
            "final_video_path": final_video,
            "pipeline_results": results
        }
        
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Pipeline error: {str(e)}",
            "pipeline_results": results.get("pipeline_steps", [])
        }


def get_supported_voices() -> Dict[str, Any]:
    """Get list of supported TTS voices."""
    return {
        "status": "success",
        "supported_voices": {
            "alloy": "Neutral, balanced voice",
            "echo": "Male voice", 
            "fable": "British accent",
            "onyx": "Deep male voice",
            "nova": "Female voice",
            "shimmer": "Soft female voice"
        },
        "default": "alloy",
        "note": "These are OpenAI TTS voices. Make sure OPENAI_API_KEY is configured."
    }


root_agent = Agent(
    name="youtube_short_maker",
    model="gemini-2.0-flash",
    description=(
        "Agent that creates YouTube Shorts by combining background video with AI-generated voiceover and uploads to YouTube."
    ),
    instruction=(
        "You are a YouTube Short creation assistant. You can process videos, generate text-to-speech audio, "
        "combine them into YouTube Shorts format (9:16 aspect ratio), and upload to YouTube. "
        "You handle the complete pipeline from raw materials to published content."
    ),
    tools=[
        process_background_video,
        generate_tts_audio, 
        combine_audio_video,
        upload_to_youtube,
        create_youtube_short,
        get_supported_voices
    ],
) 