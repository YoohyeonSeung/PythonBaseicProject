#맥북에서 가상환경 사용법
-------------------------------
## 설치되어 있는 가상환경 확인 명령어
* pyenv versions
## 설치 가능한 파이썬 버전 확인
* pyenv install --list
## 가상환경 설치 전 사용할 파이썬(버전별) 설치
* pyenv install [파이썬 버전]
* ex) pyenv install 3.7.7
## 가상환경 설치
* pyenv virtualenv [파이썬버전] [가상환경 이름]
* ex) pyenv virtualenv 3.7.7 test_env
## 설치된 가상환경 위치
* /usr/local/pyenv/versions/[가상환경 이름]/bin/python3.7
