# Brain_Hat - 여섯모자 브레인스토밍 도구

## 프로젝트 개요

이 프로젝트는 Edward de Bono의 여섯모자 기법(Six Thinking Hats)을 활용한 브레인스토밍 도구입니다. [네이버 해커톤에서 우수상을 수상한 프로젝트](https://www.youtube.com/watch?v=6_VXrumJwfQ)에 착안하여, 더 많은 사용자들에게 브레인스토밍 도구를 제공하고자 개발되었습니다. Google의 Gemini 2.5 API를 활용하여 사용자의 아이디어를 6가지 다른 관점에서 발전시키는 것을 돕는 파이썬 기반 애플리케이션입니다.

## 프로젝트 구조

```
malmo_project/
├── app.py                  # 메인 애플리케이션 (Streamlit UI)
├── gemini_api.py           # Gemini API 연동 모듈
├── six_hats.py             # 여섯모자 기법 로직
├── session_manager.py      # 세션 관리 및 데이터 저장
├── requirements.txt        # 필요한 패키지 목록
├── .env                    # 환경 변수 설정 (API 키)
├── USER_GUIDE.md           # 사용자 가이드
├── run_tests.py            # 테스트 실행 스크립트
└── tests/                  # 테스트 모듈
    ├── __init__.py
    └── test_modules.py     # 단위 테스트
```

## 설치 및 실행 방법

자세한 설치 및 실행 방법은 `USER_GUIDE.md` 파일을 참조하세요.

## 주요 기능

- 여섯모자 기법을 활용한 브레인스토밍
- 개별 모자 선택 또는 순차적 진행 모드
- 브레인스토밍 세션 저장 및 관리
- 결과 내보내기 기능

## 기술 스택

- Python 3.9+
- Streamlit (UI 프레임워크)
- Google Gemini 2.5 API
- 기타 Python 라이브러리 (requirements.txt 참조)

## 라이선스

MIT License

## 개발자 정보

- 개발자: Manus
- 버전: 1.0.0
- 개발일: 2025년 4월
