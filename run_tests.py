import pytest
import os

def main():
    # 테스트 디렉토리 경로 설정
    test_dir = os.path.join(os.path.dirname(__file__), 'tests')
    
    # pytest 실행
    pytest.main(['-v', test_dir])

if __name__ == '__main__':
    main()