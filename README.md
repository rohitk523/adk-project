05-18-2025 06:34:36 PM [AppRunner] Starting to deploy your application source code.
05-18-2025 06:35:01 PM [AppRunner] Starting to build your application source code.
05-18-2025 06:35:37 PM [PreBuild] Sending build context to Docker daemon  2.217MB

05-18-2025 06:35:37 PM [PreBuild] Step 1/3 : FROM 082388193175.dkr.ecr.us-east-1.amazonaws.com/awsfusionruntime-python311-build:uuid-python311-20250424-004344-81 AS pre-build-stage
05-18-2025 06:35:37 PM [PreBuild] uuid-python311-20250424-004344-81: Pulling from awsfusionruntime-python311-build
05-18-2025 06:35:37 PM [PreBuild] 1cf9fb914831: Pulling fs layer
05-18-2025 06:35:37 PM [PreBuild] ceb0345e0fe1: Pulling fs layer
05-18-2025 06:35:37 PM [PreBuild] c71ecbc356e5: Pulling fs layer
05-18-2025 06:35:37 PM [PreBuild] c71ecbc356e5: Verifying Checksum
05-18-2025 06:35:37 PM [PreBuild] c71ecbc356e5: Download complete
05-18-2025 06:35:37 PM [PreBuild] 1cf9fb914831: Verifying Checksum
05-18-2025 06:35:37 PM [PreBuild] 1cf9fb914831: Download complete
05-18-2025 06:35:37 PM [PreBuild] ceb0345e0fe1: Verifying Checksum
05-18-2025 06:35:37 PM [PreBuild] ceb0345e0fe1: Download complete
05-18-2025 06:35:37 PM [PreBuild] 1cf9fb914831: Pull complete
05-18-2025 06:35:37 PM [PreBuild] ceb0345e0fe1: Pull complete
05-18-2025 06:35:37 PM [PreBuild] c71ecbc356e5: Pull complete
05-18-2025 06:35:37 PM [PreBuild] Digest: sha256:85cea0c103d94eb8fdc5586d7b94e0274db2b55d69fd27603b3ad005616002a6
05-18-2025 06:35:37 PM [PreBuild] Status: Downloaded newer image for 082388193175.dkr.ecr.us-east-1.amazonaws.com/awsfusionruntime-python311-build:uuid-python311-20250424-004344-81
05-18-2025 06:35:37 PM [PreBuild]  ---> 7d84de39bf61
05-18-2025 06:35:37 PM [PreBuild] Step 2/3 : COPY . /app
05-18-2025 06:35:37 PM [PreBuild]  ---> a1d9f686a91c
05-18-2025 06:35:37 PM [PreBuild] Step 3/3 : WORKDIR /app//configs/internal
05-18-2025 06:35:37 PM [PreBuild]  ---> Running in d9b3c942eb0f
05-18-2025 06:35:37 PM [PreBuild] Removing intermediate container d9b3c942eb0f
05-18-2025 06:35:37 PM [PreBuild]  ---> 4eae7bbd658f
05-18-2025 06:35:37 PM [PreBuild] Successfully built 4eae7bbd658f
05-18-2025 06:35:38 PM  
05-18-2025 06:35:43 PM [Build] Sending build context to Docker daemon  2.217MB

05-18-2025 06:35:43 PM [Build] Step 1/7 : FROM 082388193175.dkr.ecr.us-east-1.amazonaws.com/awsfusionruntime-python311-build:uuid-python311-20250424-004344-81 AS pre-build-stage
05-18-2025 06:35:43 PM [Build]  ---> 7d84de39bf61
05-18-2025 06:35:43 PM [Build] Step 2/7 : COPY . /app
05-18-2025 06:35:43 PM [Build]  ---> Using cache
05-18-2025 06:35:43 PM [Build]  ---> a1d9f686a91c
05-18-2025 06:35:43 PM [Build] Step 3/7 : WORKDIR /app//configs/internal
05-18-2025 06:35:43 PM [Build]  ---> Using cache
05-18-2025 06:35:43 PM [Build]  ---> 4eae7bbd658f
05-18-2025 06:35:43 PM [Build] Step 4/7 : FROM pre-build-stage as build-stage
05-18-2025 06:35:43 PM [Build]  ---> 4eae7bbd658f
05-18-2025 06:35:43 PM [Build] Step 5/7 : WORKDIR /app//configs/internal
05-18-2025 06:35:43 PM [Build]  ---> Running in c27bb7acc112
05-18-2025 06:35:43 PM [Build] Removing intermediate container c27bb7acc112
05-18-2025 06:35:43 PM [Build]  ---> 7be9892ea6a8
05-18-2025 06:35:43 PM [Build] Step 6/7 : RUN pip3 install --upgrade pip
05-18-2025 06:35:43 PM [Build]  ---> Running in 16563821c985
05-18-2025 06:35:43 PM [Build] Requirement already satisfied: pip in /usr/local/lib/python3.11/site-packages (24.0)
05-18-2025 06:35:43 PM [Build] Collecting pip
05-18-2025 06:35:43 PM [Build]   Downloading pip-25.1.1-py3-none-any.whl.metadata (3.6 kB)
05-18-2025 06:35:43 PM [Build] Downloading pip-25.1.1-py3-none-any.whl (1.8 MB)
05-18-2025 06:35:43 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 66.4 MB/s eta 0:00:00
05-18-2025 06:35:43 PM [Build] Installing collected packages: pip
05-18-2025 06:35:43 PM [Build]   Attempting uninstall: pip
05-18-2025 06:35:43 PM [Build]     Found existing installation: pip 24.0
05-18-2025 06:35:43 PM [Build]     Uninstalling pip-24.0:
05-18-2025 06:35:43 PM [Build]       Successfully uninstalled pip-24.0
05-18-2025 06:35:43 PM [Build] Successfully installed pip-25.1.1
05-18-2025 06:35:43 PM [Build] [91mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
05-18-2025 06:35:43 PM [Build] [0mRemoving intermediate container 16563821c985
05-18-2025 06:35:43 PM [Build]  ---> 74a4a93eed2a
05-18-2025 06:35:43 PM [Build] Step 7/7 : RUN pip3 install -r ../requirements.txt
05-18-2025 06:35:43 PM [Build]  ---> Running in 0c951ad23200
05-18-2025 06:35:43 PM [Build] Collecting boto3>=1.34.0 (from -r ../requirements.txt (line 2))
05-18-2025 06:35:43 PM [Build]   Downloading boto3-1.38.18-py3-none-any.whl.metadata (6.6 kB)
05-18-2025 06:35:43 PM [Build] Collecting botocore (from -r ../requirements.txt (line 3))
05-18-2025 06:35:43 PM [Build]   Downloading botocore-1.38.18-py3-none-any.whl.metadata (5.7 kB)
05-18-2025 06:35:43 PM [Build] Collecting requests-aws4auth (from -r ../requirements.txt (line 4))
05-18-2025 06:35:43 PM [Build]   Downloading requests_aws4auth-1.3.1-py3-none-any.whl.metadata (18 kB)
05-18-2025 06:35:43 PM [Build] Collecting pandas>=2.2.0 (from -r ../requirements.txt (line 7))
05-18-2025 06:35:43 PM [Build]   Downloading pandas-2.2.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (89 kB)
05-18-2025 06:35:43 PM [Build] Collecting numpy>=1.26.0 (from -r ../requirements.txt (line 8))
05-18-2025 06:35:43 PM [Build]   Downloading numpy-2.2.6-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (62 kB)
05-18-2025 06:35:43 PM [Build] Collecting scikit-learn>=1.4.0 (from -r ../requirements.txt (line 9))
05-18-2025 06:35:43 PM [Build]   Downloading scikit_learn-1.6.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (18 kB)
05-18-2025 06:35:43 PM [Build] Collecting fastapi>=0.109.0 (from -r ../requirements.txt (line 12))
05-18-2025 06:35:43 PM [Build]   Downloading fastapi-0.115.12-py3-none-any.whl.metadata (27 kB)
05-18-2025 06:35:43 PM [Build] Collecting uvicorn>=0.27.0 (from -r ../requirements.txt (line 13))
05-18-2025 06:35:43 PM [Build]   Downloading uvicorn-0.34.2-py3-none-any.whl.metadata (6.5 kB)
05-18-2025 06:35:43 PM [Build] Collecting opensearch-py>=2.4.0 (from -r ../requirements.txt (line 16))
05-18-2025 06:35:43 PM [Build]   Downloading opensearch_py-2.8.0-py3-none-any.whl.metadata (6.9 kB)
05-18-2025 06:35:43 PM [Build] Collecting langchain>=0.1.0 (from -r ../requirements.txt (line 19))
05-18-2025 06:35:43 PM [Build]   Downloading langchain-0.3.25-py3-none-any.whl.metadata (7.8 kB)
05-18-2025 06:35:43 PM [Build] Collecting langchain-openai (from -r ../requirements.txt (line 20))
05-18-2025 06:35:43 PM [Build]   Downloading langchain_openai-0.3.17-py3-none-any.whl.metadata (2.3 kB)
05-18-2025 06:35:43 PM [Build] Collecting langchain_community>=0.0.10 (from -r ../requirements.txt (line 21))
05-18-2025 06:35:43 PM [Build]   Downloading langchain_community-0.3.24-py3-none-any.whl.metadata (2.5 kB)
05-18-2025 06:35:43 PM [Build] Collecting langchain-aws>=0.0.5 (from -r ../requirements.txt (line 22))
05-18-2025 06:35:43 PM [Build]   Downloading langchain_aws-0.2.23-py3-none-any.whl.metadata (3.2 kB)
05-18-2025 06:35:43 PM [Build] Collecting spacy_download (from -r ../requirements.txt (line 25))
05-18-2025 06:35:43 PM [Build]   Downloading spacy_download-1.1.0-py3-none-any.whl.metadata (2.6 kB)
05-18-2025 06:35:46 PM [Build] Collecting spacy>=3.7.0 (from -r ../requirements.txt (line 26))
05-18-2025 06:35:46 PM [Build]   Downloading spacy-3.8.4-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (27 kB)
05-18-2025 06:35:46 PM [Build] Collecting fuzzywuzzy (from -r ../requirements.txt (line 27))
05-18-2025 06:35:46 PM [Build]   Downloading fuzzywuzzy-0.18.0-py2.py3-none-any.whl.metadata (4.9 kB)
05-18-2025 06:35:46 PM [Build] Collecting python-Levenshtein (from -r ../requirements.txt (line 28))
05-18-2025 06:35:46 PM [Build]   Downloading python_levenshtein-0.27.1-py3-none-any.whl.metadata (3.7 kB)
05-18-2025 06:35:46 PM [Build] Collecting python-dotenv>=1.0.0 (from -r ../requirements.txt (line 31))
05-18-2025 06:35:46 PM [Build]   Downloading python_dotenv-1.1.0-py3-none-any.whl.metadata (24 kB)
05-18-2025 06:35:46 PM [Build] Collecting pyyaml (from -r ../requirements.txt (line 32))
05-18-2025 06:35:46 PM [Build]   Downloading PyYAML-6.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (2.1 kB)
05-18-2025 06:35:46 PM [Build] Collecting jinja2 (from -r ../requirements.txt (line 35))
05-18-2025 06:35:46 PM [Build]   Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
05-18-2025 06:35:46 PM [Build] Collecting python-multipart>=0.0.9 (from -r ../requirements.txt (line 36))
05-18-2025 06:35:46 PM [Build]   Downloading python_multipart-0.0.20-py3-none-any.whl.metadata (1.8 kB)
05-18-2025 06:35:46 PM [Build] Collecting openpyxl (from -r ../requirements.txt (line 37))
05-18-2025 06:35:46 PM [Build]   Downloading openpyxl-3.1.5-py2.py3-none-any.whl.metadata (2.5 kB)
05-18-2025 06:35:46 PM [Build] Collecting requests (from -r ../requirements.txt (line 38))
05-18-2025 06:35:46 PM [Build]   Downloading requests-2.32.3-py3-none-any.whl.metadata (4.6 kB)
05-18-2025 06:35:46 PM [Build] Collecting lark (from -r ../requirements.txt (line 39))
05-18-2025 06:35:46 PM [Build]   Downloading lark-1.2.2-py3-none-any.whl.metadata (1.8 kB)
05-18-2025 06:35:46 PM [Build] Collecting py==1.11.0 (from -r ../requirements.txt (line 40))
05-18-2025 06:35:46 PM [Build]   Downloading py-1.11.0-py2.py3-none-any.whl.metadata (2.8 kB)
05-18-2025 06:35:46 PM [Build] Collecting pytest (from -r ../requirements.txt (line 43))
05-18-2025 06:35:46 PM [Build]   Downloading pytest-8.3.5-py3-none-any.whl.metadata (7.6 kB)
05-18-2025 06:35:46 PM [Build] Collecting pytest-asyncio (from -r ../requirements.txt (line 44))
05-18-2025 06:35:46 PM [Build]   Downloading pytest_asyncio-0.26.0-py3-none-any.whl.metadata (4.0 kB)
05-18-2025 06:35:46 PM [Build] Collecting pytest-cov (from -r ../requirements.txt (line 45))
05-18-2025 06:35:46 PM [Build]   Downloading pytest_cov-6.1.1-py3-none-any.whl.metadata (28 kB)
05-18-2025 06:35:46 PM [Build] Collecting pytest-xdist (from -r ../requirements.txt (line 46))
05-18-2025 06:35:46 PM [Build]   Downloading pytest_xdist-3.6.1-py3-none-any.whl.metadata (4.3 kB)
05-18-2025 06:35:46 PM [Build] Collecting pytest-mock (from -r ../requirements.txt (line 47))
05-18-2025 06:35:46 PM [Build]   Downloading pytest_mock-3.14.0-py3-none-any.whl.metadata (3.8 kB)
05-18-2025 06:35:46 PM [Build] Collecting pydantic>=2.6.0 (from -r ../requirements.txt (line 50))
05-18-2025 06:35:46 PM [Build]   Downloading pydantic-2.11.4-py3-none-any.whl.metadata (66 kB)
05-18-2025 06:35:46 PM [Build] Collecting pydantic-settings (from -r ../requirements.txt (line 51))
05-18-2025 06:35:46 PM [Build]   Downloading pydantic_settings-2.9.1-py3-none-any.whl.metadata (3.8 kB)
05-18-2025 06:35:46 PM [Build] Collecting tqdm (from -r ../requirements.txt (line 54))
05-18-2025 06:35:46 PM [Build]   Downloading tqdm-4.67.1-py3-none-any.whl.metadata (57 kB)
05-18-2025 06:35:46 PM [Build] Collecting regex (from -r ../requirements.txt (line 55))
05-18-2025 06:35:46 PM [Build]   Downloading regex-2024.11.6-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (40 kB)
05-18-2025 06:35:46 PM [Build] Collecting httpx (from -r ../requirements.txt (line 56))
05-18-2025 06:35:46 PM [Build]   Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
05-18-2025 06:35:46 PM [Build] Collecting tenacity (from -r ../requirements.txt (line 57))
05-18-2025 06:35:46 PM [Build]   Downloading tenacity-9.1.2-py3-none-any.whl.metadata (1.2 kB)
05-18-2025 06:35:46 PM [Build] Collecting retry (from -r ../requirements.txt (line 58))
05-18-2025 06:35:46 PM [Build]   Downloading retry-0.9.2-py2.py3-none-any.whl.metadata (5.8 kB)
05-18-2025 06:35:46 PM [Build] Collecting aiohttp (from -r ../requirements.txt (line 59))
05-18-2025 06:35:46 PM [Build]   Downloading aiohttp-3.11.18-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.7 kB)
05-18-2025 06:35:46 PM [Build] Collecting setuptools>=70.0.0 (from -r ../requirements.txt (line 60))
05-18-2025 06:35:46 PM [Build]   Downloading setuptools-80.7.1-py3-none-any.whl.metadata (6.6 kB)
05-18-2025 06:35:46 PM [Build] Collecting apscheduler (from -r ../requirements.txt (line 63))
05-18-2025 06:35:46 PM [Build]   Downloading APScheduler-3.11.0-py3-none-any.whl.metadata (6.4 kB)
05-18-2025 06:35:46 PM [Build] Collecting chevron (from -r ../requirements.txt (line 66))
05-18-2025 06:35:46 PM [Build]   Downloading chevron-0.14.0-py3-none-any.whl.metadata (4.9 kB)
05-18-2025 06:35:48 PM [Build] Collecting langsmith (from -r ../requirements.txt (line 69))
05-18-2025 06:35:48 PM [Build]   Downloading langsmith-0.3.42-py3-none-any.whl.metadata (15 kB)
05-18-2025 06:35:48 PM [Build] Collecting jmespath<2.0.0,>=0.7.1 (from boto3>=1.34.0->-r ../requirements.txt (line 2))
05-18-2025 06:35:48 PM [Build]   Downloading jmespath-1.0.1-py3-none-any.whl.metadata (7.6 kB)
05-18-2025 06:35:48 PM [Build] Collecting s3transfer<0.13.0,>=0.12.0 (from boto3>=1.34.0->-r ../requirements.txt (line 2))
05-18-2025 06:35:48 PM [Build]   Downloading s3transfer-0.12.0-py3-none-any.whl.metadata (1.7 kB)
05-18-2025 06:35:48 PM [Build] Collecting python-dateutil<3.0.0,>=2.1 (from botocore->-r ../requirements.txt (line 3))
05-18-2025 06:35:48 PM [Build]   Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
05-18-2025 06:35:48 PM [Build] Collecting urllib3!=2.2.0,<3,>=1.25.4 (from botocore->-r ../requirements.txt (line 3))
05-18-2025 06:35:48 PM [Build]   Downloading urllib3-2.4.0-py3-none-any.whl.metadata (6.5 kB)
05-18-2025 06:35:48 PM [Build] Collecting six>=1.5 (from python-dateutil<3.0.0,>=2.1->botocore->-r ../requirements.txt (line 3))
05-18-2025 06:35:48 PM [Build]   Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
05-18-2025 06:35:48 PM [Build] Collecting pytz>=2020.1 (from pandas>=2.2.0->-r ../requirements.txt (line 7))
05-18-2025 06:35:48 PM [Build]   Downloading pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
05-18-2025 06:35:48 PM [Build] Collecting tzdata>=2022.7 (from pandas>=2.2.0->-r ../requirements.txt (line 7))
05-18-2025 06:35:48 PM [Build]   Downloading tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
05-18-2025 06:35:48 PM [Build] Collecting scipy>=1.6.0 (from scikit-learn>=1.4.0->-r ../requirements.txt (line 9))
05-18-2025 06:35:48 PM [Build]   Downloading scipy-1.15.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (61 kB)
05-18-2025 06:35:48 PM [Build] Collecting joblib>=1.2.0 (from scikit-learn>=1.4.0->-r ../requirements.txt (line 9))
05-18-2025 06:35:48 PM [Build]   Downloading joblib-1.5.0-py3-none-any.whl.metadata (5.6 kB)
05-18-2025 06:35:48 PM [Build] Collecting threadpoolctl>=3.1.0 (from scikit-learn>=1.4.0->-r ../requirements.txt (line 9))
05-18-2025 06:35:48 PM [Build]   Downloading threadpoolctl-3.6.0-py3-none-any.whl.metadata (13 kB)
05-18-2025 06:35:48 PM [Build] Collecting starlette<0.47.0,>=0.40.0 (from fastapi>=0.109.0->-r ../requirements.txt (line 12))
05-18-2025 06:35:48 PM [Build]   Downloading starlette-0.46.2-py3-none-any.whl.metadata (6.2 kB)
05-18-2025 06:35:48 PM [Build] Collecting typing-extensions>=4.8.0 (from fastapi>=0.109.0->-r ../requirements.txt (line 12))
05-18-2025 06:35:48 PM [Build]   Downloading typing_extensions-4.13.2-py3-none-any.whl.metadata (3.0 kB)
05-18-2025 06:35:48 PM [Build] Collecting annotated-types>=0.6.0 (from pydantic>=2.6.0->-r ../requirements.txt (line 50))
05-18-2025 06:35:48 PM [Build]   Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
05-18-2025 06:35:48 PM [Build] Collecting pydantic-core==2.33.2 (from pydantic>=2.6.0->-r ../requirements.txt (line 50))
05-18-2025 06:35:48 PM [Build]   Downloading pydantic_core-2.33.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.8 kB)
05-18-2025 06:35:48 PM [Build] Collecting typing-inspection>=0.4.0 (from pydantic>=2.6.0->-r ../requirements.txt (line 50))
05-18-2025 06:35:48 PM [Build]   Downloading typing_inspection-0.4.0-py3-none-any.whl.metadata (2.6 kB)
05-18-2025 06:35:48 PM [Build] Collecting anyio<5,>=3.6.2 (from starlette<0.47.0,>=0.40.0->fastapi>=0.109.0->-r ../requirements.txt (line 12))
05-18-2025 06:35:48 PM [Build]   Downloading anyio-4.9.0-py3-none-any.whl.metadata (4.7 kB)
05-18-2025 06:35:48 PM [Build] Collecting idna>=2.8 (from anyio<5,>=3.6.2->starlette<0.47.0,>=0.40.0->fastapi>=0.109.0->-r ../requirements.txt (line 12))
05-18-2025 06:35:48 PM [Build]   Downloading idna-3.10-py3-none-any.whl.metadata (10 kB)
05-18-2025 06:35:48 PM [Build] Collecting sniffio>=1.1 (from anyio<5,>=3.6.2->starlette<0.47.0,>=0.40.0->fastapi>=0.109.0->-r ../requirements.txt (line 12))
05-18-2025 06:35:48 PM [Build]   Downloading sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
05-18-2025 06:35:48 PM [Build] Collecting click>=7.0 (from uvicorn>=0.27.0->-r ../requirements.txt (line 13))
05-18-2025 06:35:48 PM [Build]   Downloading click-8.2.0-py3-none-any.whl.metadata (2.5 kB)
05-18-2025 06:35:48 PM [Build] Collecting h11>=0.8 (from uvicorn>=0.27.0->-r ../requirements.txt (line 13))
05-18-2025 06:35:48 PM [Build]   Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
05-18-2025 06:35:48 PM [Build] Collecting certifi>=2024.07.04 (from opensearch-py>=2.4.0->-r ../requirements.txt (line 16))
05-18-2025 06:35:48 PM [Build]   Downloading certifi-2025.4.26-py3-none-any.whl.metadata (2.5 kB)
05-18-2025 06:35:48 PM [Build] Collecting Events (from opensearch-py>=2.4.0->-r ../requirements.txt (line 16))
05-18-2025 06:35:48 PM [Build]   Downloading Events-0.5-py3-none-any.whl.metadata (3.9 kB)
05-18-2025 06:35:48 PM [Build] Collecting charset-normalizer<4,>=2 (from requests->-r ../requirements.txt (line 38))
05-18-2025 06:35:48 PM [Build]   Downloading charset_normalizer-3.4.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (35 kB)
05-18-2025 06:35:48 PM [Build] Collecting langchain-core<1.0.0,>=0.3.58 (from langchain>=0.1.0->-r ../requirements.txt (line 19))
05-18-2025 06:35:48 PM [Build]   Downloading langchain_core-0.3.60-py3-none-any.whl.metadata (5.8 kB)
05-18-2025 06:35:48 PM [Build] Collecting langchain-text-splitters<1.0.0,>=0.3.8 (from langchain>=0.1.0->-r ../requirements.txt (line 19))
05-18-2025 06:35:48 PM [Build]   Downloading langchain_text_splitters-0.3.8-py3-none-any.whl.metadata (1.9 kB)
05-18-2025 06:35:48 PM [Build] Collecting SQLAlchemy<3,>=1.4 (from langchain>=0.1.0->-r ../requirements.txt (line 19))
05-18-2025 06:35:48 PM [Build]   Downloading sqlalchemy-2.0.41-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (9.6 kB)
05-18-2025 06:35:48 PM [Build] Collecting orjson<4.0.0,>=3.9.14 (from langsmith->-r ../requirements.txt (line 69))
05-18-2025 06:35:48 PM [Build]   Downloading orjson-3.10.18-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (41 kB)
05-18-2025 06:35:48 PM [Build] Collecting packaging>=23.2 (from langsmith->-r ../requirements.txt (line 69))
05-18-2025 06:35:48 PM [Build]   Downloading packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
05-18-2025 06:35:48 PM [Build] Collecting requests-toolbelt<2.0.0,>=1.0.0 (from langsmith->-r ../requirements.txt (line 69))
05-18-2025 06:35:48 PM [Build]   Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl.metadata (14 kB)
05-18-2025 06:35:48 PM [Build] Collecting zstandard<0.24.0,>=0.23.0 (from langsmith->-r ../requirements.txt (line 69))
05-18-2025 06:35:48 PM [Build]   Downloading zstandard-0.23.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.0 kB)
05-18-2025 06:35:48 PM [Build] Collecting httpcore==1.* (from httpx->-r ../requirements.txt (line 56))
05-18-2025 06:35:48 PM [Build]   Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
05-18-2025 06:35:48 PM [Build] Collecting jsonpatch<2.0,>=1.33 (from langchain-core<1.0.0,>=0.3.58->langchain>=0.1.0->-r ../requirements.txt (line 19))
05-18-2025 06:35:48 PM [Build]   Downloading jsonpatch-1.33-py2.py3-none-any.whl.metadata (3.0 kB)
05-18-2025 06:35:48 PM [Build] Collecting packaging>=23.2 (from langsmith->-r ../requirements.txt (line 69))
05-18-2025 06:35:48 PM [Build]   Downloading packaging-24.2-py3-none-any.whl.metadata (3.2 kB)
05-18-2025 06:35:48 PM [Build] Collecting jsonpointer>=1.9 (from jsonpatch<2.0,>=1.33->langchain-core<1.0.0,>=0.3.58->langchain>=0.1.0->-r ../requirements.txt (line 19))
05-18-2025 06:35:48 PM [Build]   Downloading jsonpointer-3.0.0-py2.py3-none-any.whl.metadata (2.3 kB)
05-18-2025 06:35:48 PM [Build] Collecting greenlet>=1 (from SQLAlchemy<3,>=1.4->langchain>=0.1.0->-r ../requirements.txt (line 19))
05-18-2025 06:35:48 PM [Build]   Downloading greenlet-3.2.2-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (4.1 kB)
05-18-2025 06:35:48 PM [Build] Collecting openai<2.0.0,>=1.68.2 (from langchain-openai->-r ../requirements.txt (line 20))
05-18-2025 06:35:48 PM [Build]   Downloading openai-1.79.0-py3-none-any.whl.metadata (25 kB)
05-18-2025 06:35:48 PM [Build] Collecting tiktoken<1,>=0.7 (from langchain-openai->-r ../requirements.txt (line 20))
05-18-2025 06:35:48 PM [Build]   Downloading tiktoken-0.9.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.7 kB)
05-18-2025 06:35:48 PM [Build] Collecting distro<2,>=1.7.0 (from openai<2.0.0,>=1.68.2->langchain-openai->-r ../requirements.txt (line 20))
05-18-2025 06:35:48 PM [Build]   Downloading distro-1.9.0-py3-none-any.whl.metadata (6.8 kB)
05-18-2025 06:35:48 PM [Build] Collecting jiter<1,>=0.4.0 (from openai<2.0.0,>=1.68.2->langchain-openai->-r ../requirements.txt (line 20))
05-18-2025 06:35:48 PM [Build]   Downloading jiter-0.9.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.2 kB)
05-18-2025 06:35:48 PM [Build] Collecting dataclasses-json<0.7,>=0.5.7 (from langchain_community>=0.0.10->-r ../requirements.txt (line 21))
05-18-2025 06:35:48 PM [Build]   Downloading dataclasses_json-0.6.7-py3-none-any.whl.metadata (25 kB)
05-18-2025 06:35:48 PM [Build] Collecting httpx-sse<1.0.0,>=0.4.0 (from langchain_community>=0.0.10->-r ../requirements.txt (line 21))
05-18-2025 06:35:48 PM [Build]   Downloading httpx_sse-0.4.0-py3-none-any.whl.metadata (9.0 kB)
05-18-2025 06:35:48 PM [Build] Collecting aiohappyeyeballs>=2.3.0 (from aiohttp->-r ../requirements.txt (line 59))
05-18-2025 06:35:48 PM [Build]   Downloading aiohappyeyeballs-2.6.1-py3-none-any.whl.metadata (5.9 kB)
05-18-2025 06:35:48 PM [Build] Collecting aiosignal>=1.1.2 (from aiohttp->-r ../requirements.txt (line 59))
05-18-2025 06:35:48 PM [Build]   Downloading aiosignal-1.3.2-py2.py3-none-any.whl.metadata (3.8 kB)
05-18-2025 06:35:48 PM [Build] Collecting attrs>=17.3.0 (from aiohttp->-r ../requirements.txt (line 59))
05-18-2025 06:35:50 PM [Build]   Downloading attrs-25.3.0-py3-none-any.whl.metadata (10 kB)
05-18-2025 06:35:50 PM [Build] Collecting frozenlist>=1.1.1 (from aiohttp->-r ../requirements.txt (line 59))
05-18-2025 06:35:50 PM [Build]   Downloading frozenlist-1.6.0-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (16 kB)
05-18-2025 06:35:50 PM [Build] Collecting multidict<7.0,>=4.5 (from aiohttp->-r ../requirements.txt (line 59))
05-18-2025 06:35:50 PM [Build]   Downloading multidict-6.4.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.3 kB)
05-18-2025 06:35:50 PM [Build] Collecting propcache>=0.2.0 (from aiohttp->-r ../requirements.txt (line 59))
05-18-2025 06:35:50 PM [Build]   Downloading propcache-0.3.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (10 kB)
05-18-2025 06:35:50 PM [Build] Collecting yarl<2.0,>=1.17.0 (from aiohttp->-r ../requirements.txt (line 59))
05-18-2025 06:35:50 PM [Build]   Downloading yarl-1.20.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (72 kB)
05-18-2025 06:35:50 PM [Build] Collecting marshmallow<4.0.0,>=3.18.0 (from dataclasses-json<0.7,>=0.5.7->langchain_community>=0.0.10->-r ../requirements.txt (line 21))
05-18-2025 06:35:50 PM [Build]   Downloading marshmallow-3.26.1-py3-none-any.whl.metadata (7.3 kB)
05-18-2025 06:35:50 PM [Build] Collecting typing-inspect<1,>=0.4.0 (from dataclasses-json<0.7,>=0.5.7->langchain_community>=0.0.10->-r ../requirements.txt (line 21))
05-18-2025 06:35:50 PM [Build]   Downloading typing_inspect-0.9.0-py3-none-any.whl.metadata (1.5 kB)
05-18-2025 06:35:50 PM [Build] Collecting mypy-extensions>=0.3.0 (from typing-inspect<1,>=0.4.0->dataclasses-json<0.7,>=0.5.7->langchain_community>=0.0.10->-r ../requirements.txt (line 21))
05-18-2025 06:35:50 PM [Build]   Downloading mypy_extensions-1.1.0-py3-none-any.whl.metadata (1.1 kB)
05-18-2025 06:35:50 PM [Build] Collecting numpy>=1.26.0 (from -r ../requirements.txt (line 8))
05-18-2025 06:35:50 PM [Build]   Downloading numpy-1.26.4-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (61 kB)
05-18-2025 06:35:50 PM [Build] Collecting spacy-legacy<3.1.0,>=3.0.11 (from spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:50 PM [Build]   Downloading spacy_legacy-3.0.12-py2.py3-none-any.whl.metadata (2.8 kB)
05-18-2025 06:35:50 PM [Build] Collecting spacy-loggers<2.0.0,>=1.0.0 (from spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:50 PM [Build]   Downloading spacy_loggers-1.0.5-py3-none-any.whl.metadata (23 kB)
05-18-2025 06:35:50 PM [Build] Collecting murmurhash<1.1.0,>=0.28.0 (from spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:50 PM [Build]   Downloading murmurhash-1.0.12-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (2.1 kB)
05-18-2025 06:35:50 PM [Build] Collecting cymem<2.1.0,>=2.0.2 (from spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:50 PM [Build]   Downloading cymem-2.0.11-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (8.5 kB)
05-18-2025 06:35:50 PM [Build] Collecting preshed<3.1.0,>=3.0.2 (from spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:50 PM [Build]   Downloading preshed-3.0.9-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (2.2 kB)
05-18-2025 06:35:50 PM [Build] Collecting thinc<8.4.0,>=8.3.4 (from spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:50 PM [Build]   Downloading thinc-8.3.6-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (15 kB)
05-18-2025 06:35:50 PM [Build] Collecting wasabi<1.2.0,>=0.9.1 (from spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:50 PM [Build]   Downloading wasabi-1.1.3-py3-none-any.whl.metadata (28 kB)
05-18-2025 06:35:50 PM [Build] Collecting srsly<3.0.0,>=2.4.3 (from spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:50 PM [Build]   Downloading srsly-2.5.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (19 kB)
05-18-2025 06:35:50 PM [Build] Collecting catalogue<2.1.0,>=2.0.6 (from spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:50 PM [Build]   Downloading catalogue-2.0.10-py3-none-any.whl.metadata (14 kB)
05-18-2025 06:35:50 PM [Build] Collecting weasel<0.5.0,>=0.1.0 (from spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:50 PM [Build]   Downloading weasel-0.4.1-py3-none-any.whl.metadata (4.6 kB)
05-18-2025 06:35:50 PM [Build] Collecting typer<1.0.0,>=0.3.0 (from spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:50 PM [Build]   Downloading typer-0.15.4-py3-none-any.whl.metadata (15 kB)
05-18-2025 06:35:50 PM [Build] Collecting langcodes<4.0.0,>=3.2.0 (from spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:50 PM [Build]   Downloading langcodes-3.5.0-py3-none-any.whl.metadata (29 kB)
05-18-2025 06:35:52 PM [Build] Collecting language-data>=1.2 (from langcodes<4.0.0,>=3.2.0->spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:52 PM [Build]   Downloading language_data-1.3.0-py3-none-any.whl.metadata (4.3 kB)
05-18-2025 06:35:52 PM [Build] Collecting blis<1.4.0,>=1.3.0 (from thinc<8.4.0,>=8.3.4->spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:52 PM [Build]   Downloading blis-1.3.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.4 kB)
05-18-2025 06:35:52 PM [Build] Collecting confection<1.0.0,>=0.0.1 (from thinc<8.4.0,>=8.3.4->spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:52 PM [Build]   Downloading confection-0.1.5-py3-none-any.whl.metadata (19 kB)
05-18-2025 06:35:52 PM [Build] INFO: pip is looking at multiple versions of thinc to determine which version is compatible with other requirements. This could take a while.
05-18-2025 06:35:52 PM [Build] Collecting thinc<8.4.0,>=8.3.4 (from spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:52 PM [Build]   Downloading thinc-8.3.4-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (15 kB)
05-18-2025 06:35:52 PM [Build] Collecting blis<1.3.0,>=1.2.0 (from thinc<8.4.0,>=8.3.4->spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:52 PM [Build]   Downloading blis-1.2.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.4 kB)
05-18-2025 06:35:52 PM [Build] Collecting click>=7.0 (from uvicorn>=0.27.0->-r ../requirements.txt (line 13))
05-18-2025 06:35:52 PM [Build]   Downloading click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
05-18-2025 06:35:52 PM [Build] Collecting shellingham>=1.3.0 (from typer<1.0.0,>=0.3.0->spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:52 PM [Build]   Downloading shellingham-1.5.4-py2.py3-none-any.whl.metadata (3.5 kB)
05-18-2025 06:35:52 PM [Build] Collecting rich>=10.11.0 (from typer<1.0.0,>=0.3.0->spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:52 PM [Build]   Downloading rich-14.0.0-py3-none-any.whl.metadata (18 kB)
05-18-2025 06:35:52 PM [Build] Collecting cloudpathlib<1.0.0,>=0.7.0 (from weasel<0.5.0,>=0.1.0->spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:52 PM [Build]   Downloading cloudpathlib-0.21.1-py3-none-any.whl.metadata (14 kB)
05-18-2025 06:35:52 PM [Build] Collecting smart-open<8.0.0,>=5.2.1 (from weasel<0.5.0,>=0.1.0->spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:52 PM [Build]   Downloading smart_open-7.1.0-py3-none-any.whl.metadata (24 kB)
05-18-2025 06:35:52 PM [Build] Collecting wrapt (from smart-open<8.0.0,>=5.2.1->weasel<0.5.0,>=0.1.0->spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:52 PM [Build]   Downloading wrapt-1.17.2-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.4 kB)
05-18-2025 06:35:52 PM [Build] Collecting Levenshtein==0.27.1 (from python-Levenshtein->-r ../requirements.txt (line 28))
05-18-2025 06:35:52 PM [Build]   Downloading levenshtein-0.27.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.6 kB)
05-18-2025 06:35:52 PM [Build] Collecting rapidfuzz<4.0.0,>=3.9.0 (from Levenshtein==0.27.1->python-Levenshtein->-r ../requirements.txt (line 28))
05-18-2025 06:35:52 PM [Build]   Downloading rapidfuzz-3.13.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (12 kB)
05-18-2025 06:35:52 PM [Build] Collecting MarkupSafe>=2.0 (from jinja2->-r ../requirements.txt (line 35))
05-18-2025 06:35:52 PM [Build]   Downloading MarkupSafe-3.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.0 kB)
05-18-2025 06:35:52 PM [Build] Collecting et-xmlfile (from openpyxl->-r ../requirements.txt (line 37))
05-18-2025 06:35:52 PM [Build]   Downloading et_xmlfile-2.0.0-py3-none-any.whl.metadata (2.7 kB)
05-18-2025 06:35:52 PM [Build] Collecting iniconfig (from pytest->-r ../requirements.txt (line 43))
05-18-2025 06:35:52 PM [Build]   Downloading iniconfig-2.1.0-py3-none-any.whl.metadata (2.7 kB)
05-18-2025 06:35:52 PM [Build] Collecting pluggy<2,>=1.5 (from pytest->-r ../requirements.txt (line 43))
05-18-2025 06:35:52 PM [Build]   Downloading pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
05-18-2025 06:35:52 PM [Build] Collecting coverage>=7.5 (from coverage[toml]>=7.5->pytest-cov->-r ../requirements.txt (line 45))
05-18-2025 06:35:52 PM [Build]   Downloading coverage-7.8.0-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (8.5 kB)
05-18-2025 06:35:52 PM [Build] Collecting execnet>=2.1 (from pytest-xdist->-r ../requirements.txt (line 46))
05-18-2025 06:35:52 PM [Build]   Downloading execnet-2.1.1-py3-none-any.whl.metadata (2.9 kB)
05-18-2025 06:35:52 PM [Build] Collecting decorator>=3.4.2 (from retry->-r ../requirements.txt (line 58))
05-18-2025 06:35:52 PM [Build]   Downloading decorator-5.2.1-py3-none-any.whl.metadata (3.9 kB)
05-18-2025 06:35:52 PM [Build] Collecting tzlocal>=3.0 (from apscheduler->-r ../requirements.txt (line 63))
05-18-2025 06:35:52 PM [Build]   Downloading tzlocal-5.3.1-py3-none-any.whl.metadata (7.6 kB)
05-18-2025 06:35:52 PM [Build] Collecting marisa-trie>=1.1.0 (from language-data>=1.2->langcodes<4.0.0,>=3.2.0->spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:52 PM [Build]   Downloading marisa_trie-1.2.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (9.0 kB)
05-18-2025 06:35:52 PM [Build] Collecting markdown-it-py>=2.2.0 (from rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:52 PM [Build]   Downloading markdown_it_py-3.0.0-py3-none-any.whl.metadata (6.9 kB)
05-18-2025 06:35:52 PM [Build] Collecting pygments<3.0.0,>=2.13.0 (from rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:52 PM [Build]   Downloading pygments-2.19.1-py3-none-any.whl.metadata (2.5 kB)
05-18-2025 06:35:52 PM [Build] Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy>=3.7.0->-r ../requirements.txt (line 26))
05-18-2025 06:35:52 PM [Build]   Downloading mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
05-18-2025 06:35:52 PM [Build] Downloading py-1.11.0-py2.py3-none-any.whl (98 kB)
05-18-2025 06:35:52 PM [Build] Downloading boto3-1.38.18-py3-none-any.whl (139 kB)
05-18-2025 06:35:52 PM [Build] Downloading botocore-1.38.18-py3-none-any.whl (13.6 MB)
05-18-2025 06:35:52 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.6/13.6 MB 199.0 MB/s eta 0:00:00
05-18-2025 06:35:52 PM [Build] Downloading jmespath-1.0.1-py3-none-any.whl (20 kB)
05-18-2025 06:35:52 PM [Build] Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
05-18-2025 06:35:52 PM [Build] Downloading s3transfer-0.12.0-py3-none-any.whl (84 kB)
05-18-2025 06:35:52 PM [Build] Downloading urllib3-2.4.0-py3-none-any.whl (128 kB)
05-18-2025 06:35:52 PM [Build] Downloading requests_aws4auth-1.3.1-py3-none-any.whl (24 kB)
05-18-2025 06:35:52 PM [Build] Downloading pandas-2.2.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (13.1 MB)
05-18-2025 06:35:52 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.1/13.1 MB 230.5 MB/s eta 0:00:00
05-18-2025 06:35:52 PM [Build] Downloading scikit_learn-1.6.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (13.5 MB)
05-18-2025 06:35:52 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.5/13.5 MB 158.6 MB/s eta 0:00:00
05-18-2025 06:35:52 PM [Build] Downloading fastapi-0.115.12-py3-none-any.whl (95 kB)
05-18-2025 06:35:52 PM [Build] Downloading pydantic-2.11.4-py3-none-any.whl (443 kB)
05-18-2025 06:35:52 PM [Build] Downloading pydantic_core-2.33.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.0 MB)
05-18-2025 06:35:52 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.0/2.0 MB 172.2 MB/s eta 0:00:00
05-18-2025 06:35:52 PM [Build] Downloading starlette-0.46.2-py3-none-any.whl (72 kB)
05-18-2025 06:35:52 PM [Build] Downloading anyio-4.9.0-py3-none-any.whl (100 kB)
05-18-2025 06:35:52 PM [Build] Downloading uvicorn-0.34.2-py3-none-any.whl (62 kB)
05-18-2025 06:35:52 PM [Build] Downloading opensearch_py-2.8.0-py3-none-any.whl (353 kB)
05-18-2025 06:35:52 PM [Build] Downloading requests-2.32.3-py3-none-any.whl (64 kB)
05-18-2025 06:35:52 PM [Build] Downloading charset_normalizer-3.4.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (147 kB)
05-18-2025 06:35:52 PM [Build] Downloading idna-3.10-py3-none-any.whl (70 kB)
05-18-2025 06:35:52 PM [Build] Downloading langchain-0.3.25-py3-none-any.whl (1.0 MB)
05-18-2025 06:35:52 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.0/1.0 MB 103.0 MB/s eta 0:00:00
05-18-2025 06:35:52 PM [Build] Downloading langsmith-0.3.42-py3-none-any.whl (360 kB)
05-18-2025 06:35:52 PM [Build] Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
05-18-2025 06:35:52 PM [Build] Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
05-18-2025 06:35:52 PM [Build] Downloading langchain_core-0.3.60-py3-none-any.whl (437 kB)
05-18-2025 06:35:52 PM [Build] Downloading tenacity-9.1.2-py3-none-any.whl (28 kB)
05-18-2025 06:35:52 PM [Build] Downloading jsonpatch-1.33-py2.py3-none-any.whl (12 kB)
05-18-2025 06:35:52 PM [Build] Downloading langchain_text_splitters-0.3.8-py3-none-any.whl (32 kB)
05-18-2025 06:35:52 PM [Build] Downloading orjson-3.10.18-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (132 kB)
05-18-2025 06:35:52 PM [Build] Downloading packaging-24.2-py3-none-any.whl (65 kB)
05-18-2025 06:35:52 PM [Build] Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl (54 kB)
05-18-2025 06:35:52 PM [Build] Downloading sqlalchemy-2.0.41-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.3 MB)
05-18-2025 06:35:54 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 222.1 MB/s eta 0:00:00
05-18-2025 06:35:54 PM [Build] Downloading zstandard-0.23.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (5.4 MB)
05-18-2025 06:35:54 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.4/5.4 MB 228.6 MB/s eta 0:00:00
05-18-2025 06:35:54 PM [Build] Downloading langchain_openai-0.3.17-py3-none-any.whl (62 kB)
05-18-2025 06:35:54 PM [Build] Downloading openai-1.79.0-py3-none-any.whl (683 kB)
05-18-2025 06:35:54 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 683.3/683.3 kB 93.1 MB/s eta 0:00:00
05-18-2025 06:35:54 PM [Build] Downloading distro-1.9.0-py3-none-any.whl (20 kB)
05-18-2025 06:35:54 PM [Build] Downloading jiter-0.9.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (351 kB)
05-18-2025 06:35:54 PM [Build] Downloading tiktoken-0.9.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.2 MB)
05-18-2025 06:35:54 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 129.0 MB/s eta 0:00:00
05-18-2025 06:35:54 PM [Build] Downloading typing_extensions-4.13.2-py3-none-any.whl (45 kB)
05-18-2025 06:35:54 PM [Build] Downloading langchain_community-0.3.24-py3-none-any.whl (2.5 MB)
05-18-2025 06:35:54 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.5/2.5 MB 136.3 MB/s eta 0:00:00
05-18-2025 06:35:54 PM [Build] Downloading pydantic_settings-2.9.1-py3-none-any.whl (44 kB)
05-18-2025 06:35:54 PM [Build] Downloading aiohttp-3.11.18-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.7 MB)
05-18-2025 06:35:54 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 151.3 MB/s eta 0:00:00
05-18-2025 06:35:54 PM [Build] Downloading dataclasses_json-0.6.7-py3-none-any.whl (28 kB)
05-18-2025 06:35:54 PM [Build] Downloading httpx_sse-0.4.0-py3-none-any.whl (7.8 kB)
05-18-2025 06:35:54 PM [Build] Downloading marshmallow-3.26.1-py3-none-any.whl (50 kB)
05-18-2025 06:35:54 PM [Build] Downloading multidict-6.4.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (223 kB)
05-18-2025 06:35:54 PM [Build] Downloading typing_inspect-0.9.0-py3-none-any.whl (8.8 kB)
05-18-2025 06:35:54 PM [Build] Downloading yarl-1.20.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (358 kB)
05-18-2025 06:35:54 PM [Build] Downloading langchain_aws-0.2.23-py3-none-any.whl (120 kB)
05-18-2025 06:35:54 PM [Build] Downloading numpy-1.26.4-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (18.3 MB)
05-18-2025 06:35:54 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 18.3/18.3 MB 233.6 MB/s eta 0:00:00
05-18-2025 06:35:54 PM [Build] Downloading spacy_download-1.1.0-py3-none-any.whl (3.6 kB)
05-18-2025 06:35:54 PM [Build] Downloading spacy-3.8.4-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (30.6 MB)
05-18-2025 06:35:54 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 30.6/30.6 MB 160.2 MB/s eta 0:00:00
05-18-2025 06:35:54 PM [Build] Downloading tqdm-4.67.1-py3-none-any.whl (78 kB)
05-18-2025 06:35:54 PM [Build] Downloading catalogue-2.0.10-py3-none-any.whl (17 kB)
05-18-2025 06:35:54 PM [Build] Downloading cymem-2.0.11-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (218 kB)
05-18-2025 06:35:54 PM [Build] Downloading langcodes-3.5.0-py3-none-any.whl (182 kB)
05-18-2025 06:35:54 PM [Build] Downloading murmurhash-1.0.12-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (134 kB)
05-18-2025 06:35:54 PM [Build] Downloading preshed-3.0.9-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (157 kB)
05-18-2025 06:35:54 PM [Build] Downloading spacy_legacy-3.0.12-py2.py3-none-any.whl (29 kB)
05-18-2025 06:35:54 PM [Build] Downloading spacy_loggers-1.0.5-py3-none-any.whl (22 kB)
05-18-2025 06:35:54 PM [Build] Downloading srsly-2.5.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.1 MB)
05-18-2025 06:35:54 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 135.7 MB/s eta 0:00:00
05-18-2025 06:35:54 PM [Build] Downloading thinc-8.3.4-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.9 MB)
05-18-2025 06:35:54 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.9/3.9 MB 163.5 MB/s eta 0:00:00
05-18-2025 06:35:54 PM [Build] Downloading blis-1.2.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.7 MB)
05-18-2025 06:35:54 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.7/11.7 MB 139.5 MB/s eta 0:00:00
05-18-2025 06:35:54 PM [Build] Downloading confection-0.1.5-py3-none-any.whl (35 kB)
05-18-2025 06:35:54 PM [Build] Downloading typer-0.15.4-py3-none-any.whl (45 kB)
05-18-2025 06:35:54 PM [Build] Downloading click-8.1.8-py3-none-any.whl (98 kB)
05-18-2025 06:35:54 PM [Build] Downloading wasabi-1.1.3-py3-none-any.whl (27 kB)
05-18-2025 06:35:54 PM [Build] Downloading weasel-0.4.1-py3-none-any.whl (50 kB)
05-18-2025 06:35:54 PM [Build] Downloading cloudpathlib-0.21.1-py3-none-any.whl (52 kB)
05-18-2025 06:35:54 PM [Build] Downloading smart_open-7.1.0-py3-none-any.whl (61 kB)
05-18-2025 06:35:54 PM [Build] Downloading fuzzywuzzy-0.18.0-py2.py3-none-any.whl (18 kB)
05-18-2025 06:35:54 PM [Build] Downloading python_levenshtein-0.27.1-py3-none-any.whl (9.4 kB)
05-18-2025 06:35:54 PM [Build] Downloading levenshtein-0.27.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (161 kB)
05-18-2025 06:35:54 PM [Build] Downloading rapidfuzz-3.13.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.1 MB)
05-18-2025 06:35:54 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.1/3.1 MB 197.1 MB/s eta 0:00:00
05-18-2025 06:35:54 PM [Build] Downloading python_dotenv-1.1.0-py3-none-any.whl (20 kB)
05-18-2025 06:35:54 PM [Build] Downloading PyYAML-6.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (762 kB)
05-18-2025 06:35:54 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 763.0/763.0 kB 89.1 MB/s eta 0:00:00
05-18-2025 06:35:54 PM [Build] Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
05-18-2025 06:35:54 PM [Build] Downloading python_multipart-0.0.20-py3-none-any.whl (24 kB)
05-18-2025 06:35:54 PM [Build] Downloading openpyxl-3.1.5-py2.py3-none-any.whl (250 kB)
05-18-2025 06:35:54 PM [Build] Downloading lark-1.2.2-py3-none-any.whl (111 kB)
05-18-2025 06:35:54 PM [Build] Downloading pytest-8.3.5-py3-none-any.whl (343 kB)
05-18-2025 06:35:54 PM [Build] Downloading pluggy-1.6.0-py3-none-any.whl (20 kB)
05-18-2025 06:35:54 PM [Build] Downloading pytest_asyncio-0.26.0-py3-none-any.whl (19 kB)
05-18-2025 06:35:54 PM [Build] Downloading pytest_cov-6.1.1-py3-none-any.whl (23 kB)
05-18-2025 06:35:54 PM [Build] Downloading pytest_xdist-3.6.1-py3-none-any.whl (46 kB)
05-18-2025 06:35:54 PM [Build] Downloading pytest_mock-3.14.0-py3-none-any.whl (9.9 kB)
05-18-2025 06:35:54 PM [Build] Downloading regex-2024.11.6-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (792 kB)
05-18-2025 06:35:54 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 792.7/792.7 kB 89.1 MB/s eta 0:00:00
05-18-2025 06:35:54 PM [Build] Downloading retry-0.9.2-py2.py3-none-any.whl (8.0 kB)
05-18-2025 06:35:54 PM [Build] Downloading setuptools-80.7.1-py3-none-any.whl (1.2 MB)
05-18-2025 06:35:54 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 98.4 MB/s eta 0:00:00
05-18-2025 06:35:54 PM [Build] Downloading APScheduler-3.11.0-py3-none-any.whl (64 kB)
05-18-2025 06:35:54 PM [Build] Downloading chevron-0.14.0-py3-none-any.whl (11 kB)
05-18-2025 06:35:54 PM [Build] Downloading aiohappyeyeballs-2.6.1-py3-none-any.whl (15 kB)
05-18-2025 06:35:54 PM [Build] Downloading aiosignal-1.3.2-py2.py3-none-any.whl (7.6 kB)
05-18-2025 06:35:54 PM [Build] Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
05-18-2025 06:35:54 PM [Build] Downloading attrs-25.3.0-py3-none-any.whl (63 kB)
05-18-2025 06:35:54 PM [Build] Downloading certifi-2025.4.26-py3-none-any.whl (159 kB)
05-18-2025 06:35:54 PM [Build] Downloading coverage-7.8.0-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (244 kB)
05-18-2025 06:35:54 PM [Build] Downloading decorator-5.2.1-py3-none-any.whl (9.2 kB)
05-18-2025 06:35:54 PM [Build] Downloading execnet-2.1.1-py3-none-any.whl (40 kB)
05-18-2025 06:35:54 PM [Build] Downloading frozenlist-1.6.0-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (313 kB)
05-18-2025 06:35:54 PM [Build] Downloading greenlet-3.2.2-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (583 kB)
05-18-2025 06:35:54 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 583.9/583.9 kB 63.8 MB/s eta 0:00:00
05-18-2025 06:35:54 PM [Build] Downloading h11-0.16.0-py3-none-any.whl (37 kB)
05-18-2025 06:35:54 PM [Build] Downloading joblib-1.5.0-py3-none-any.whl (307 kB)
05-18-2025 06:35:54 PM [Build] Downloading jsonpointer-3.0.0-py2.py3-none-any.whl (7.6 kB)
05-18-2025 06:36:20 PM [Build] Downloading language_data-1.3.0-py3-none-any.whl (5.4 MB)
05-18-2025 06:36:20 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.4/5.4 MB 210.3 MB/s eta 0:00:00
05-18-2025 06:36:20 PM [Build] Downloading marisa_trie-1.2.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.4 MB)
05-18-2025 06:36:20 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.4/1.4 MB 153.5 MB/s eta 0:00:00
05-18-2025 06:36:20 PM [Build] Downloading MarkupSafe-3.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (23 kB)
05-18-2025 06:36:20 PM [Build] Downloading mypy_extensions-1.1.0-py3-none-any.whl (5.0 kB)
05-18-2025 06:36:20 PM [Build] Downloading propcache-0.3.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (232 kB)
05-18-2025 06:36:20 PM [Build] Downloading pytz-2025.2-py2.py3-none-any.whl (509 kB)
05-18-2025 06:36:20 PM [Build] Downloading rich-14.0.0-py3-none-any.whl (243 kB)
05-18-2025 06:36:20 PM [Build] Downloading pygments-2.19.1-py3-none-any.whl (1.2 MB)
05-18-2025 06:36:20 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 143.5 MB/s eta 0:00:00
05-18-2025 06:36:20 PM [Build] Downloading markdown_it_py-3.0.0-py3-none-any.whl (87 kB)
05-18-2025 06:36:20 PM [Build] Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)
05-18-2025 06:36:20 PM [Build] Downloading scipy-1.15.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (37.7 MB)
05-18-2025 06:36:20 PM [Build]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 37.7/37.7 MB 171.4 MB/s eta 0:00:00
05-18-2025 06:36:20 PM [Build] Downloading shellingham-1.5.4-py2.py3-none-any.whl (9.8 kB)
05-18-2025 06:36:20 PM [Build] Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
05-18-2025 06:36:20 PM [Build] Downloading sniffio-1.3.1-py3-none-any.whl (10 kB)
05-18-2025 06:36:20 PM [Build] Downloading threadpoolctl-3.6.0-py3-none-any.whl (18 kB)
05-18-2025 06:36:20 PM [Build] Downloading typing_inspection-0.4.0-py3-none-any.whl (14 kB)
05-18-2025 06:36:20 PM [Build] Downloading tzdata-2025.2-py2.py3-none-any.whl (347 kB)
05-18-2025 06:36:20 PM [Build] Downloading tzlocal-5.3.1-py3-none-any.whl (18 kB)
05-18-2025 06:36:20 PM [Build] Downloading et_xmlfile-2.0.0-py3-none-any.whl (18 kB)
05-18-2025 06:36:20 PM [Build] Downloading Events-0.5-py3-none-any.whl (6.8 kB)
05-18-2025 06:36:20 PM [Build] Downloading iniconfig-2.1.0-py3-none-any.whl (6.0 kB)
05-18-2025 06:36:20 PM [Build] Downloading wrapt-1.17.2-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (83 kB)
05-18-2025 06:36:20 PM [Build] Installing collected packages: pytz, fuzzywuzzy, Events, cymem, chevron, zstandard, wrapt, wasabi, urllib3, tzlocal, tzdata, typing-extensions, tqdm, threadpoolctl, tenacity, spacy-loggers, spacy-legacy, sniffio, six, shellingham, setuptools, regex, rapidfuzz, pyyaml, python-multipart, python-dotenv, pygments, py, propcache, pluggy, packaging, orjson, numpy, mypy-extensions, murmurhash, multidict, mdurl, MarkupSafe, lark, jsonpointer, joblib, jmespath, jiter, iniconfig, idna, httpx-sse, h11, greenlet, frozenlist, execnet, et-xmlfile, distro, decorator, coverage, cloudpathlib, click, charset-normalizer, certifi, catalogue, attrs, annotated-types, aiohappyeyeballs, yarl, uvicorn, typing-inspection, typing-inspect, srsly, SQLAlchemy, smart-open, scipy, retry, requests, python-dateutil, pytest, pydantic-core, preshed, openpyxl, marshmallow, markdown-it-py, marisa-trie, Levenshtein, jsonpatch, jinja2, httpcore, blis, apscheduler, anyio, aiosignal, tiktoken, starlette, scikit-learn, rich, requests-toolbelt, requests-aws4auth, python-Levenshtein, pytest-xdist, pytest-mock, pytest-cov, pytest-asyncio, pydantic, pandas, opensearch-py, language-data, httpx, dataclasses-json, botocore, aiohttp, typer, s3transfer, pydantic-settings, openai, langsmith, langcodes, fastapi, confection, weasel, thinc, langchain-core, boto3, spacy, langchain-text-splitters, langchain-openai, langchain-aws, spacy_download, langchain, langchain_community
05-18-2025 06:36:20 PM [Build]   Attempting uninstall: setuptools
05-18-2025 06:36:20 PM [Build]     Found existing installation: setuptools 65.5.0
05-18-2025 06:36:20 PM [Build]     Uninstalling setuptools-65.5.0:
05-18-2025 06:36:20 PM [Build]       Successfully uninstalled setuptools-65.5.0
05-18-2025 06:36:46 PM [Build] Successfully installed Events-0.5 Levenshtein-0.27.1 MarkupSafe-3.0.2 SQLAlchemy-2.0.41 aiohappyeyeballs-2.6.1 aiohttp-3.11.18 aiosignal-1.3.2 annotated-types-0.7.0 anyio-4.9.0 apscheduler-3.11.0 attrs-25.3.0 blis-1.2.1 boto3-1.38.18 botocore-1.38.18 catalogue-2.0.10 certifi-2025.4.26 charset-normalizer-3.4.2 chevron-0.14.0 click-8.1.8 cloudpathlib-0.21.1 confection-0.1.5 coverage-7.8.0 cymem-2.0.11 dataclasses-json-0.6.7 decorator-5.2.1 distro-1.9.0 et-xmlfile-2.0.0 execnet-2.1.1 fastapi-0.115.12 frozenlist-1.6.0 fuzzywuzzy-0.18.0 greenlet-3.2.2 h11-0.16.0 httpcore-1.0.9 httpx-0.28.1 httpx-sse-0.4.0 idna-3.10 iniconfig-2.1.0 jinja2-3.1.6 jiter-0.9.0 jmespath-1.0.1 joblib-1.5.0 jsonpatch-1.33 jsonpointer-3.0.0 langchain-0.3.25 langchain-aws-0.2.23 langchain-core-0.3.60 langchain-openai-0.3.17 langchain-text-splitters-0.3.8 langchain_community-0.3.24 langcodes-3.5.0 langsmith-0.3.42 language-data-1.3.0 lark-1.2.2 marisa-trie-1.2.1 markdown-it-py-3.0.0 marshmallow-3.26.1 mdurl-0.1.2 multidict-6.4.3 murmurhash-1.0.12 mypy-extensions-1.1.0 numpy-1.26.4 openai-1.79.0 openpyxl-3.1.5 opensearch-py-2.8.0 orjson-3.10.18 packaging-24.2 pandas-2.2.3 pluggy-1.6.0 preshed-3.0.9 propcache-0.3.1 py-1.11.0 pydantic-2.11.4 pydantic-core-2.33.2 pydantic-settings-2.9.1 pygments-2.19.1 pytest-8.3.5 pytest-asyncio-0.26.0 pytest-cov-6.1.1 pytest-mock-3.14.0 pytest-xdist-3.6.1 python-Levenshtein-0.27.1 python-dateutil-2.9.0.post0 python-dotenv-1.1.0 python-multipart-0.0.20 pytz-2025.2 pyyaml-6.0.2 rapidfuzz-3.13.0 regex-2024.11.6 requests-2.32.3 requests-aws4auth-1.3.1 requests-toolbelt-1.0.0 retry-0.9.2 rich-14.0.0 s3transfer-0.12.0 scikit-learn-1.6.1 scipy-1.15.3 setuptools-80.7.1 shellingham-1.5.4 six-1.17.0 smart-open-7.1.0 sniffio-1.3.1 spacy-3.8.4 spacy-legacy-3.0.12 spacy-loggers-1.0.5 spacy_download-1.1.0 srsly-2.5.1 starlette-0.46.2 tenacity-9.1.2 thinc-8.3.4 threadpoolctl-3.6.0 tiktoken-0.9.0 tqdm-4.67.1 typer-0.15.4 typing-extensions-4.13.2 typing-inspect-0.9.0 typing-inspection-0.4.0 tzdata-2025.2 tzlocal-5.3.1 urllib3-2.4.0 uvicorn-0.34.2 wasabi-1.1.3 weasel-0.4.1 wrapt-1.17.2 yarl-1.20.0 zstandard-0.23.0
05-18-2025 06:36:46 PM [Build] [91mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
05-18-2025 06:36:46 PM [Build] [0mRemoving intermediate container 0c951ad23200
05-18-2025 06:36:46 PM [Build]  ---> 2e96e0b1fbb4
05-18-2025 06:36:46 PM [Build] Successfully built 2e96e0b1fbb4
05-18-2025 06:36:52 PM [PreRun] Sending build context to Docker daemon  2.217MB

05-18-2025 06:36:52 PM [PreRun] Step 1/14 : FROM 082388193175.dkr.ecr.us-east-1.amazonaws.com/awsfusionruntime-python311-build:uuid-python311-20250424-004344-81 AS pre-build-stage
05-18-2025 06:36:52 PM [PreRun]  ---> 7d84de39bf61
05-18-2025 06:36:52 PM [PreRun] Step 2/14 : COPY . /app
05-18-2025 06:36:52 PM [PreRun]  ---> Using cache
05-18-2025 06:36:52 PM [PreRun]  ---> a1d9f686a91c
05-18-2025 06:36:52 PM [PreRun] Step 3/14 : WORKDIR /app//configs/internal
05-18-2025 06:36:52 PM [PreRun]  ---> Using cache
05-18-2025 06:36:52 PM [PreRun]  ---> 4eae7bbd658f
05-18-2025 06:36:52 PM [PreRun] Step 4/14 : FROM pre-build-stage as build-stage
05-18-2025 06:36:52 PM [PreRun]  ---> 4eae7bbd658f
05-18-2025 06:36:52 PM [PreRun] Step 5/14 : WORKDIR /app//configs/internal
05-18-2025 06:36:52 PM [PreRun]  ---> Using cache
05-18-2025 06:36:52 PM [PreRun]  ---> 7be9892ea6a8
05-18-2025 06:36:52 PM [PreRun] Step 6/14 : RUN pip3 install --upgrade pip
05-18-2025 06:36:52 PM [PreRun]  ---> Using cache
05-18-2025 06:36:52 PM [PreRun]  ---> 74a4a93eed2a
05-18-2025 06:36:52 PM [PreRun] Step 7/14 : RUN pip3 install -r ../requirements.txt
05-18-2025 06:36:52 PM [PreRun]  ---> Using cache
05-18-2025 06:36:52 PM [PreRun]  ---> 2e96e0b1fbb4
05-18-2025 06:36:52 PM [PreRun] Step 8/14 : FROM 082388193175.dkr.ecr.us-east-1.amazonaws.com/awsfusionruntime-python311:uuid-python311-20250424-004344-81 AS packaging-stage
05-18-2025 06:36:52 PM [PreRun] uuid-python311-20250424-004344-81: Pulling from awsfusionruntime-python311
05-18-2025 06:36:52 PM [PreRun] 1cf9fb914831: Already exists
05-18-2025 06:36:52 PM [PreRun] ceb0345e0fe1: Already exists
05-18-2025 06:36:52 PM [PreRun] 686961784caf: Pulling fs layer
05-18-2025 06:36:52 PM [PreRun] 686961784caf: Verifying Checksum
05-18-2025 06:36:52 PM [PreRun] 686961784caf: Download complete
05-18-2025 06:36:52 PM [PreRun] 686961784caf: Pull complete
05-18-2025 06:36:52 PM [PreRun] Digest: sha256:fe4ae0f8a9fe3ef8b0d96d1ec9a3cae624bc6f6b988b5eab9b3298905b0760f6
05-18-2025 06:36:52 PM [PreRun] Status: Downloaded newer image for 082388193175.dkr.ecr.us-east-1.amazonaws.com/awsfusionruntime-python311:uuid-python311-20250424-004344-81
05-18-2025 06:36:52 PM [PreRun]  ---> c28a917c7624
05-18-2025 06:36:52 PM [PreRun] Step 9/14 : COPY --from=build-stage /app /app
05-18-2025 06:36:52 PM [PreRun]  ---> f9ae3653595a
05-18-2025 06:36:52 PM [PreRun] Step 10/14 : WORKDIR /app//configs/internal
05-18-2025 06:36:52 PM [PreRun]  ---> Running in 4d183e5c7492
05-18-2025 06:36:52 PM [PreRun] Removing intermediate container 4d183e5c7492
05-18-2025 06:36:52 PM [PreRun]  ---> 5618d557eb3d
05-18-2025 06:36:52 PM [PreRun] Step 11/14 : RUN pip3 install pipenv
05-18-2025 06:36:52 PM [PreRun]  ---> Running in b485af5eeb2d
05-18-2025 06:36:52 PM [PreRun] Collecting pipenv
05-18-2025 06:36:52 PM [PreRun]   Downloading pipenv-2025.0.2-py3-none-any.whl.metadata (17 kB)
05-18-2025 06:36:52 PM [PreRun] Collecting certifi (from pipenv)
05-18-2025 06:36:52 PM [PreRun]   Downloading certifi-2025.4.26-py3-none-any.whl.metadata (2.5 kB)
05-18-2025 06:36:52 PM [PreRun] Collecting packaging>=22 (from pipenv)
05-18-2025 06:36:52 PM [PreRun]   Downloading packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
05-18-2025 06:36:52 PM [PreRun] Collecting setuptools>=67 (from pipenv)
05-18-2025 06:36:52 PM [PreRun]   Downloading setuptools-80.7.1-py3-none-any.whl.metadata (6.6 kB)
05-18-2025 06:36:52 PM [PreRun] Collecting virtualenv>=20.24.2 (from pipenv)
05-18-2025 06:36:52 PM [PreRun]   Downloading virtualenv-20.31.2-py3-none-any.whl.metadata (4.5 kB)
05-18-2025 06:36:52 PM [PreRun] Collecting distlib<1,>=0.3.7 (from virtualenv>=20.24.2->pipenv)
05-18-2025 06:36:52 PM [PreRun]   Downloading distlib-0.3.9-py2.py3-none-any.whl.metadata (5.2 kB)
05-18-2025 06:36:52 PM [PreRun] Collecting filelock<4,>=3.12.2 (from virtualenv>=20.24.2->pipenv)
05-18-2025 06:36:52 PM [PreRun]   Downloading filelock-3.18.0-py3-none-any.whl.metadata (2.9 kB)
05-18-2025 06:36:52 PM [PreRun] Collecting platformdirs<5,>=3.9.1 (from virtualenv>=20.24.2->pipenv)
05-18-2025 06:36:52 PM [PreRun]   Downloading platformdirs-4.3.8-py3-none-any.whl.metadata (12 kB)
05-18-2025 06:36:52 PM [PreRun] Downloading pipenv-2025.0.2-py3-none-any.whl (3.0 MB)
05-18-2025 06:36:52 PM [PreRun]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 119.9 MB/s eta 0:00:00
05-18-2025 06:36:52 PM [PreRun] Downloading packaging-25.0-py3-none-any.whl (66 kB)
05-18-2025 06:36:52 PM [PreRun]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 66.5/66.5 kB 16.9 MB/s eta 0:00:00
05-18-2025 06:36:52 PM [PreRun] Downloading setuptools-80.7.1-py3-none-any.whl (1.2 MB)
05-18-2025 06:36:52 PM [PreRun]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 113.3 MB/s eta 0:00:00
05-18-2025 06:36:52 PM [PreRun] Downloading virtualenv-20.31.2-py3-none-any.whl (6.1 MB)
05-18-2025 06:36:52 PM [PreRun]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.1/6.1 MB 170.5 MB/s eta 0:00:00
05-18-2025 06:36:52 PM [PreRun] Downloading certifi-2025.4.26-py3-none-any.whl (159 kB)
05-18-2025 06:38:30 PM [PreRun]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 159.6/159.6 kB 40.0 MB/s eta 0:00:00
05-18-2025 06:38:30 PM [PreRun] Downloading distlib-0.3.9-py2.py3-none-any.whl (468 kB)
05-18-2025 06:38:30 PM [PreRun]    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 469.0/469.0 kB 86.7 MB/s eta 0:00:00
05-18-2025 06:38:30 PM [PreRun] Downloading filelock-3.18.0-py3-none-any.whl (16 kB)
05-18-2025 06:38:30 PM [PreRun] Downloading platformdirs-4.3.8-py3-none-any.whl (18 kB)
05-18-2025 06:38:30 PM [PreRun] Installing collected packages: distlib, setuptools, platformdirs, packaging, filelock, certifi, virtualenv, pipenv
05-18-2025 06:38:30 PM [PreRun]   Attempting uninstall: setuptools
05-18-2025 06:38:30 PM [PreRun]     Found existing installation: setuptools 65.5.0
05-18-2025 06:38:30 PM [PreRun]     Uninstalling setuptools-65.5.0:
05-18-2025 06:38:30 PM [PreRun]       Successfully uninstalled setuptools-65.5.0
05-18-2025 06:38:30 PM [PreRun] Successfully installed certifi-2025.4.26 distlib-0.3.9 filelock-3.18.0 packaging-25.0 pipenv-2025.0.2 platformdirs-4.3.8 setuptools-80.7.1 virtualenv-20.31.2
05-18-2025 06:38:30 PM [PreRun] [91mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
05-18-2025 06:38:30 PM [PreRun] [0m[91m
05-18-2025 06:38:30 PM [PreRun] [notice] A new release of pip is available: 24.0 -> 25.1.1
05-18-2025 06:38:30 PM [PreRun] [notice] To update, run: pip3 install --upgrade pip
05-18-2025 06:38:30 PM [PreRun] [0mRemoving intermediate container b485af5eeb2d
05-18-2025 06:38:30 PM [PreRun]  ---> fd5854bc6b7b
05-18-2025 06:38:30 PM [PreRun] Step 12/14 : RUN pipenv install
05-18-2025 06:38:30 PM [PreRun]  ---> Running in 19338c6cc40e
05-18-2025 06:38:30 PM [PreRun] [91mWarning: the environment variable LANG is not set!
05-18-2025 06:38:30 PM [PreRun] We recommend setting this in ~/.profile (or equivalent) for proper expected 
05-18-2025 06:38:30 PM [PreRun] behavior.
05-18-2025 06:38:30 PM [PreRun] [0m[91mCreating a virtualenv for this project
05-18-2025 06:38:30 PM [PreRun] [0m[91mPipfile: /app/configs/internal/Pipfile
05-18-2025 06:38:30 PM [PreRun] [0m[91mUsing /usr/local/bin/python33.11.12 to create virtualenv...
05-18-2025 06:38:30 PM [PreRun] [0m[91mcreated virtual environment CPython3.11.12.final.0-64 in 511ms
05-18-2025 06:38:30 PM [PreRun]   creator CPython3Posix(dest=/root/.local/share/virtualenvs/internal-8t7Xgr26, 
05-18-2025 06:38:30 PM [PreRun] clear=False, no_vcs_ignore=False, global=False)
05-18-2025 06:38:30 PM [PreRun]   seeder FromAppData(download=False, pip=bundle, setuptools=bundle, via=copy, 
05-18-2025 06:38:30 PM [PreRun] app_data_dir=/root/.local/share/virtualenv)
05-18-2025 06:38:30 PM [PreRun]     added seed packages: pip==25.1.1, setuptools==80.3.1
05-18-2025 06:38:30 PM [PreRun]   activators 
05-18-2025 06:38:30 PM [PreRun] BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator
05-18-2025 06:38:30 PM [PreRun] ,PythonActivator
05-18-2025 06:38:30 PM [PreRun] [0m[91m✔ Successfully created virtual environment!
05-18-2025 06:38:30 PM [PreRun] [0m[91mVirtualenv location: /root/.local/share/virtualenvs/internal-8t7Xgr26
05-18-2025 06:38:30 PM [PreRun] [0mrequirements.txt found in /app/configs instead of Pipfile! Converting...
05-18-2025 06:38:30 PM [PreRun] ✔ Success!
05-18-2025 06:38:30 PM [PreRun] Warning: Your Pipfile now contains pinned versions, if your requirements.txt 
05-18-2025 06:38:30 PM [PreRun] did. 
05-18-2025 06:38:30 PM [PreRun] We recommend updating your Pipfile to specify the "*" version, instead.
05-18-2025 06:38:30 PM [PreRun] [91mPipfile.lock not found, creating...
05-18-2025 06:38:30 PM [PreRun] [0m[91mLocking  dependencies...
05-18-2025 06:38:30 PM [PreRun] [0mBuilding requirements...
05-18-2025 06:38:30 PM [PreRun] Resolving dependencies...
05-18-2025 06:38:30 PM [PreRun] ✔ Success!
05-18-2025 06:38:30 PM [PreRun] [91mLocking  dependencies...
05-18-2025 06:38:30 PM [PreRun] [0m[91mUpdated Pipfile.lock 
05-18-2025 06:38:30 PM [PreRun] (326bea8534f6c2407a95b1c8e9213ebb88f99de7eae612b0bbfbf2029725e8ab)!
05-18-2025 06:38:30 PM [PreRun] [0mTo activate this project's virtualenv, run pipenv shell.
05-18-2025 06:38:30 PM [PreRun] Alternatively, run a command inside the virtualenv with pipenv run.
05-18-2025 06:38:30 PM [PreRun] Installing dependencies from Pipfile.lock (25e8ab)...
05-18-2025 06:38:30 PM [PreRun] Removing intermediate container 19338c6cc40e
05-18-2025 06:38:30 PM [PreRun]  ---> 0c390d3faf1b
05-18-2025 06:38:30 PM [PreRun] Step 13/14 : RUN pipenv run python -V
05-18-2025 06:38:30 PM [PreRun]  ---> Running in bbfbb5f8e147
05-18-2025 06:38:30 PM [PreRun] Python 3.11.12
05-18-2025 06:38:30 PM [PreRun] Removing intermediate container bbfbb5f8e147
05-18-2025 06:38:30 PM [PreRun]  ---> 9e0b73e776f0
05-18-2025 06:38:30 PM [PreRun] Step 14/14 : EXPOSE 8000
05-18-2025 06:38:30 PM [PreRun]  ---> Running in 1a7688d3c10c
05-18-2025 06:38:30 PM [PreRun] Removing intermediate container 1a7688d3c10c
05-18-2025 06:38:30 PM [PreRun]  ---> 0ad2aab55f22
05-18-2025 06:38:30 PM [PreRun] Successfully built 0ad2aab55f22
05-18-2025 06:38:30 PM [PreRun] Successfully tagged application-image:latest
05-18-2025 06:38:30 PM [PostBuild] Sending build context to Docker daemon  2.217MB

05-18-2025 06:38:30 PM [PostBuild] Step 1/16 : FROM 082388193175.dkr.ecr.us-east-1.amazonaws.com/awsfusionruntime-python311-build:uuid-python311-20250424-004344-81 AS pre-build-stage
05-18-2025 06:38:30 PM [PostBuild]  ---> 7d84de39bf61
05-18-2025 06:38:30 PM [PostBuild] Step 2/16 : COPY . /app
05-18-2025 06:38:30 PM [PostBuild]  ---> Using cache
05-18-2025 06:38:30 PM [PostBuild]  ---> a1d9f686a91c
05-18-2025 06:38:30 PM [PostBuild] Step 3/16 : WORKDIR /app//configs/internal
05-18-2025 06:38:30 PM [PostBuild]  ---> Using cache
05-18-2025 06:38:30 PM [PostBuild]  ---> 4eae7bbd658f
05-18-2025 06:38:30 PM [PostBuild] Step 4/16 : FROM pre-build-stage as build-stage
05-18-2025 06:38:30 PM [PostBuild]  ---> 4eae7bbd658f
05-18-2025 06:38:30 PM [PostBuild] Step 5/16 : WORKDIR /app//configs/internal
05-18-2025 06:38:30 PM [PostBuild]  ---> Using cache
05-18-2025 06:38:30 PM [PostBuild]  ---> 7be9892ea6a8
05-18-2025 06:38:30 PM [PostBuild] Step 6/16 : RUN pip3 install --upgrade pip
05-18-2025 06:38:30 PM [PostBuild]  ---> Using cache
05-18-2025 06:38:30 PM [PostBuild]  ---> 74a4a93eed2a
05-18-2025 06:38:30 PM [PostBuild] Step 7/16 : RUN pip3 install -r ../requirements.txt
05-18-2025 06:38:30 PM [PostBuild]  ---> Using cache
05-18-2025 06:38:30 PM [PostBuild]  ---> 2e96e0b1fbb4
05-18-2025 06:38:30 PM [PostBuild] Step 8/16 : FROM 082388193175.dkr.ecr.us-east-1.amazonaws.com/awsfusionruntime-python311:uuid-python311-20250424-004344-81 AS packaging-stage
05-18-2025 06:38:30 PM [PostBuild]  ---> c28a917c7624
05-18-2025 06:38:30 PM [PostBuild] Step 9/16 : COPY --from=build-stage /app /app
05-18-2025 06:38:30 PM [PostBuild]  ---> Using cache
05-18-2025 06:38:30 PM [PostBuild]  ---> f9ae3653595a
05-18-2025 06:38:30 PM [PostBuild] Step 10/16 : WORKDIR /app//configs/internal
05-18-2025 06:38:30 PM [PostBuild]  ---> Using cache
05-18-2025 06:38:30 PM [PostBuild]  ---> 5618d557eb3d
05-18-2025 06:38:30 PM [PostBuild] Step 11/16 : RUN pip3 install pipenv
05-18-2025 06:38:30 PM [PostBuild]  ---> Using cache
05-18-2025 06:38:30 PM [PostBuild]  ---> fd5854bc6b7b
05-18-2025 06:38:30 PM [PostBuild] Step 12/16 : RUN pipenv install
05-18-2025 06:38:30 PM [PostBuild]  ---> Using cache
05-18-2025 06:38:30 PM [PostBuild]  ---> 0c390d3faf1b
05-18-2025 06:38:30 PM [PostBuild] Step 13/16 : RUN pipenv run python -V
05-18-2025 06:38:30 PM [PostBuild]  ---> Using cache
05-18-2025 06:38:30 PM [PostBuild]  ---> 9e0b73e776f0
05-18-2025 06:38:30 PM [PostBuild] Step 14/16 : EXPOSE 8000
05-18-2025 06:38:30 PM [PostBuild]  ---> Using cache
05-18-2025 06:38:30 PM [PostBuild]  ---> 0ad2aab55f22
05-18-2025 06:38:30 PM [PostBuild] Step 15/16 : FROM build-stage AS post-build-stage
05-18-2025 06:38:30 PM [PostBuild]  ---> 2e96e0b1fbb4
05-18-2025 06:38:30 PM [PostBuild] Step 16/16 : WORKDIR /app//configs/internal
05-18-2025 06:38:30 PM [PostBuild]  ---> Running in fc2c973d26bc
05-18-2025 06:38:30 PM [PostBuild] Removing intermediate container fc2c973d26bc
05-18-2025 06:38:30 PM [PostBuild]  ---> 18dfb57df8dc
05-18-2025 06:38:30 PM [PostBuild] Successfully built 18dfb57df8dc
05-18-2025 06:39:13 PM [AppRunner] Successfully built your application source code.
05-18-2025 06:41:16 PM [AppRunner] Failed to deploy your application source code.