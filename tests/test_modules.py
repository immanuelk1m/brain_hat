import pytest
import os
import json
from datetime import datetime

# 테스트할 모듈 가져오기
import six_hats
import session_manager as sm

# 세션 관리 테스트
def test_session_management():
    # 세션 생성
    session_id = sm.create_session()
    assert isinstance(session_id, str)
    assert len(session_id) > 0
    
    # 세션 데이터 저장
    test_data = {
        'id': session_id,
        'topic': '테스트 주제',
        'current_hat': 'blue',
        'responses': {}
    }
    sm.save_session(test_data)
    
    # 세션 로드
    loaded_data = sm.load_session(session_id)
    assert loaded_data == test_data
    
    # 세션 목록
    sessions = sm.list_sessions()
    assert session_id in sessions
    
    # 세션 주제 가져오기
    topic = sm.get_session_topic(session_id)
    assert topic == '테스트 주제'
    
    # 세션 삭제
    assert sm.delete_session(session_id)
    assert session_id not in sm.list_sessions()

# 여섯모자 로직 테스트
def test_six_hats():
    # 모자 설명 가져오기
    for hat in ['white', 'red', 'black', 'yellow', 'green', 'blue']:
        description = six_hats.get_hat_description(hat)
        assert isinstance(description, str)
        assert len(description) > 0
    
    # 다음 모자 가져오기
    assert six_hats.get_next_hat('blue') == 'white'
    assert six_hats.get_next_hat('white') == 'red'
    assert six_hats.get_next_hat('red') == 'black'
    assert six_hats.get_next_hat('black') == 'yellow'
    assert six_hats.get_next_hat('yellow') == 'green'
    assert six_hats.get_next_hat('green') == 'blue'