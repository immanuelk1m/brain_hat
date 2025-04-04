# 말모말모 사용자 가이드

## 설치 방법

1. Python 3.9 이상이 설치되어 있는지 확인하세요.
2. 프로젝트를 클론합니다:
   ```bash
   git clone https://github.com/immanuelk1m/brain_hat.git
   cd brain_hat
   ```
3. 가상환경을 생성하고 활성화합니다:
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```
4. 필요한 패키지를 설치합니다:
   ```bash
   pip install -r requirements.txt
   ```
5. `.env.example` 파일을 복사하여 `.env` 파일을 만들고 필요한 값을 설정합니다:
   ```
   GEMINI_API_KEY=your_api_key_here
   SESSION_SECRET_KEY=your_session_secret_here
   ```

## 실행 방법

1. 가상환경이 활성화되어 있는지 확인합니다.
2. 다음 명령어로 애플리케이션을 실행합니다:
   ```bash
   streamlit run app.py
   ```
3. 웹 브라우저에서 `http://localhost:8501`로 접속합니다.

## 사용 방법

### 1. 브레인스토밍 세션 시작
- 메인 페이지에서 '새 세션 시작' 버튼을 클릭합니다.
- 주제를 입력하고 시작합니다.

### 2. 모자 선택
- 6가지 모자 중 하나를 선택합니다:
  - 흰색 모자: 객관적 사실과 정보
  - 빨간색 모자: 감정과 직관
  - 검은색 모자: 비판적 판단
  - 노란색 모자: 긍정적 사고
  - 초록색 모자: 창의적 대안
  - 파란색 모자: 사고 과정 통제

### 3. 아이디어 발전
- 선택한 모자의 관점에서 아이디어를 입력합니다.
- AI의 피드백을 받아 아이디어를 발전시킵니다.

### 4. 세션 관리
- 진행 중인 세션을 저장할 수 있습니다.
- 이전 세션을 불러와 계속 진행할 수 있습니다.
- 완료된 세션의 결과를 내보낼 수 있습니다.

## 문제 해결

### API 키 관련 문제
- `.env` 파일이 올바르게 설정되어 있는지 확인하세요.
- API 키가 유효한지 확인하세요.

### 세션 저장 문제
- `sessions` 디렉토리의 권한을 확인하세요.
- 디스크 공간이 충분한지 확인하세요.

### 기타 문제
- 로그 파일을 확인하세요.
- 이슈를 GitHub에 보고해주세요.

## 피드백 및 기여

- 버그 리포트나 기능 제안은 GitHub 이슈를 통해 해주세요.
- 풀 리퀘스트는 언제나 환영합니다.

## 라이선스

MIT License