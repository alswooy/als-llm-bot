# als-llm-bot
LLM chat bot to use CrewAI

## 1. 프로젝트 세팅 
-  vsc
- Github 연동

## 2. 프로젝트 구성
- 가상환경 설정 =>Docker Container 개념 (공간을 따로 분리해서 관리하겠다.)
- 파이썬 3.8로 개발하였는데 배포할 서버가 3.3 이면->오류-> 환경을 맞춰주기위함
=>로컬에서 작업하는 환경과 호스트 서버에서 작업하는 환경을 일치 시켜주기 위함.
=>Docker(virutal Machine) //venv모듈을 사용해서 환경 설정을 해주도록 하겟습니다.

> python3 -m venv .venv  //가상환경 생성
> source .venv/bin/activate //가상환경 진입(mac)
> .venv/Scripts/activate //가상환경 진입(win)
project based learning

## 3. 프로젝트
### (3-1) Ollama 모델 + CrewAI
    (1) ollama 다운로드
    (2) ollama를 통해  llm 다운로드
        > ollama pull llama3.1
        > ollama run llama3.1
        > ollama pull phi3:3.8b
        > ollama run phi3:3.8b

    (3) CrewAI 설치
    - 언어 모델의 API 관리를 편리하게 도와주는 라이브러리
    - 모델 - 클로드, 젬미니, GTP3.5, GPT4o ....=> import OpenAI // 언어마다 SDK를 다운받아줘야한다.
        => CrewAI, LangChain이 이미 다 SDK 구현을 끝내놓음.
    - LangChain안하고 왜 CrewAi하는 이유 => 가볍다(러닝 커브가 낮아서)

    REST API - 기술 명세
    => 우리 챗봇은 만든 REST API를 기반으로 동작

    >pip install crewai crewai-tools
        - 의존성 관리
    >pip install langchain-ollama
        - langchain-ollama설치
        
    [crewAI ollama 사용법](https://docs.crewai.com/how-to/LLM-Connections/#changing-the-default-llm)

### (3-2) Flack 사용해서 기본적인 챗봇
