import os
import json
from datetime import datetime

# 세션 디렉토리 설정
SESSION_DIR = 'sessions'
os.makedirs(SESSION_DIR, exist_ok=True)

def create_session() -> str:
    """새로운 세션을 생성합니다."""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return timestamp

def save_session(session_data: dict) -> None:
    """세션 데이터를 파일로 저장합니다."""
    session_id = session_data['id']
    filename = os.path.join(SESSION_DIR, f'{session_id}.json')
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error saving session: {str(e)}")

def load_session(session_id: str) -> dict:
    """세션 데이터를 파일에서 로드합니다."""
    filename = os.path.join(SESSION_DIR, f'{session_id}.json')
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading session: {str(e)}")
        return None

def list_sessions() -> list:
    """저장된 세션 목록을 반환합니다."""
    try:
        files = os.listdir(SESSION_DIR)
        sessions = [f.replace('.json', '') for f in files if f.endswith('.json')]
        return sorted(sessions, reverse=True)
    except Exception as e:
        print(f"Error listing sessions: {str(e)}")
        return []

def get_session_topic(session_id: str) -> str:
    """세션의 주제를 반환합니다."""
    session_data = load_session(session_id)
    return session_data['topic'] if session_data else ''

def delete_session(session_id: str) -> bool:
    """세션을 삭제합니다."""
    filename = os.path.join(SESSION_DIR, f'{session_id}.json')
    
    try:
        os.remove(filename)
        return True
    except Exception as e:
        print(f"Error deleting session: {str(e)}")
        return False