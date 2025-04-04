def get_hat_description(hat: str) -> str:
    """특정 모자의 생각 방식에 대한 설명을 반환합니다."""
    
    descriptions = {
        'white': """하얀모자는 객관성과 중립성을 상징합니다.

이 모자를 쓰면서 다음에 집중해주세요:
- 사실과 정보만을 객관적으로 바라봅니다
- 개인적인 해석이나 의견은 배제합니다
- 검증 가능한 데이터에 집중합니다
- 추가로 필요한 정보를 파악합니다""",
        
        'red': """빨간모자는 감정과 직관을 상징합니다.

이 모자를 쓰면서 다음에 집중해주세요:
- 즈각적인 감정과 느낌을 표현합니다
- 논리적 정당화 없이 직관을 표현합니다
- 감정이 주는 영향을 고려합니다
- 본능적인 선호도를 표현합니다""",
        
        'black': """검은모자는 주의와 비판을 상징합니다.

이 모자를 쓰면서 다음에 집중해주세요:
- 잠재적 위험과 문제점을 파악합니다
- 논리적 취약점을 발견합니다
- 현실적 제약사항을 고려합니다
- 부정적 결과를 예측합니다""",
        
        'yellow': """노란모자는 긍정과 희망을 상징합니다.

이 모자를 쓰면서 다음에 집중해주세요:
- 장점과 혜택을 찾습니다
- 성공 가능성을 탐구합니다
- 긍정적 결과를 예측합니다
- 기회 요소를 발견합니다""",
        
        'green': """초록모자는 창의성과 성장을 상징합니다.

이 모자를 쓰면서 다음에 집중해주세요:
- 새로운 아이디어를 제안합니다
- 대안적 해결책을 모색합니다
- 혁신적 방법을 탐구합니다
- 발전 가능성을 탐색합니다""",
        
        'blue': """파란모자는 통제와 관리를 상징합니다.

이 모자를 쓰면서 다음에 집중해주세요:
- 현재 상황을 점검합니다
- 다음 단계를 계획합니다
- 사고 과정을 관리합니다
- 결론 도출을 준비합니다"""
    }
    
    return descriptions.get(hat, "")

def get_next_hat(current_hat: str) -> str:
    """현재 모자 다음의 모자를 반환합니다."""
    
    hat_sequence = ['blue', 'white', 'red', 'black', 'yellow', 'green']
    current_index = hat_sequence.index(current_hat)
    next_index = (current_index + 1) % len(hat_sequence)
    
    return hat_sequence[next_index]