import os
import google.generativeai as genai
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# Gemini API 설정
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

def get_hat_response(topic: str, hat: str, user_input: str) -> str:
    """특정 모자의 관점에서 사용자의 생각을 발전시킵니다."""
    
    # 모자별 프롬프트 템플릿
    hat_prompts = {
        'white': f"""주제: {topic}
사용자의 생각: {user_input}

당신은 하얀모자 관점의 전문가입니다. 객관적 사실과 정보에 집중하여 위 생각을 발전시켜주세요.

다음 관점에서 분석해주세요:
1. 현재 알려진 사실들
2. 필요한 추가 정보
3. 객관적 데이터와 통계
4. 검증 가능한 정보원

분석 결과를 마크다운 형식으로 작성해주세요.""",
        
        'red': f"""주제: {topic}
사용자의 생각: {user_input}

당신은 빨간모자 관점의 전문가입니다. 감정과 직관에 집중하여 위 생각을 발전시켜주세요.

다음 관점에서 분석해주세요:
1. 즉각적인 감정 반응
2. 직관적 판단
3. 감정적 영향
4. 본능적 선호도

분석 결과를 마크다운 형식으로 작성해주세요.""",
        
        'black': f"""주제: {topic}
사용자의 생각: {user_input}

당신은 검은모자 관점의 전문가입니다. 비판적 판단에 집중하여 위 생각을 발전시켜주세요.

다음 관점에서 분석해주세요:
1. 잠재적 위험요소
2. 논리적 문제점
3. 현실적 제약사항
4. 부정적 영향

분석 결과를 마크다운 형식으로 작성해주세요.""",
        
        'yellow': f"""주제: {topic}
사용자의 생각: {user_input}

당신은 노란모자 관점의 전문가입니다. 긍정적 사고에 집중하여 위 생각을 발전시켜주세요.

다음 관점에서 분석해주세요:
1. 장점과 혜택
2. 성공 가능성
3. 긍정적 영향
4. 기회 요소

분석 결과를 마크다운 형식으로 작성해주세요.""",
        
        'green': f"""주제: {topic}
사용자의 생각: {user_input}

당신은 초록모자 관점의 전문가입니다. 창의적 대안에 집중하여 위 생각을 발전시켜주세요.

다음 관점에서 분석해주세요:
1. 새로운 아이디어
2. 대안적 접근방식
3. 혁신적 해결책
4. 발전 가능성

분석 결과를 마크다운 형식으로 작성해주세요.""",
        
        'blue': f"""주제: {topic}
사용자의 생각: {user_input}

당신은 파란모자 관점의 전문가입니다. 사고 과정 통제에 집중하여 위 생각을 발전시켜주세요.

다음 관점에서 분석해주세요:
1. 현재 진행상황
2. 다음 단계
3. 사고 프로세스
4. 결론 도출 방향

분석 결과를 마크다운 형식으로 작성해주세요."""
    }
    
    try:
        response = model.generate_content(hat_prompts[hat])
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def get_final_summary(topic: str, responses: dict) -> str:
    """모든 모자의 관점을 종합하여 최종 결론을 도출합니다."""
    
    # 응답 내용 정리
    hat_contents = []
    for hat, response in responses.items():
        hat_contents.append(f"### {hat.capitalize()} Hat\n{response}")
    
    prompt = f"""주제: {topic}

각 모자별 생각:
{'\n\n'.join(hat_contents)}

위 내용을 종합하여 다음 형식으로 최종 결론을 도출해주세요:

1. 핵심 인사이트
2. 주요 고려사항
3. 제안된 해결책
4. 다음 단계

결과를 마크다운 형식으로 작성해주세요."""
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"