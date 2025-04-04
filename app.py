import streamlit as st
import gemini_api as ai
import six_hats as sh
import session_manager as sm

# 페이지 설정
st.set_page_config(
    page_title="말모말모 - 여섯모자 브레인스토밍",
    page_icon="🎩",
    layout="wide"
)

# 세션 초기화
if 'session_id' not in st.session_state:
    st.session_state.session_id = None
if 'current_hat' not in st.session_state:
    st.session_state.current_hat = None
if 'topic' not in st.session_state:
    st.session_state.topic = ""
if 'responses' not in st.session_state:
    st.session_state.responses = {}

# 사이드바
with st.sidebar:
    st.title("🎩 말모말모")
    st.subheader("여섯모자 브레인스토밍")
    
    if st.session_state.session_id:
        if st.button("새 세션 시작", type="primary"):
            st.session_state.session_id = None
            st.session_state.current_hat = None
            st.session_state.topic = ""
            st.session_state.responses = {}
            st.rerun()
    
    st.markdown("---")
    st.markdown("""
    ### 모자 설명
    - 🤍 하얀모자: 객관적 사실과 정보
    - ❤️ 빨간모자: 감정과 직관
    - 🖤 검은모자: 비판적 판단
    - 💛 노란모자: 긍정적 사고
    - 💚 초록모자: 창의적 대안
    - 💙 파란모자: 사고 과정 통제
    """)

# 메인 화면
if not st.session_state.session_id:
    st.title("새 브레인스토밍 세션 시작")
    topic = st.text_input("주제를 입력하세요:")
    
    if st.button("시작하기", type="primary"):
        if topic.strip():
            st.session_state.session_id = sm.create_session()
            st.session_state.topic = topic
            st.session_state.current_hat = "blue"
            st.rerun()
        else:
            st.error("주제를 입력해주세요.")

    # 이전 세션 불러오기
    st.markdown("---")
    st.subheader("이전 세션 불러오기")
    sessions = sm.list_sessions()
    if sessions:
        selected_session = st.selectbox(
            "세션 선택:",
            options=sessions,
            format_func=lambda x: f"세션 {x} - {sm.get_session_topic(x)}"
        )
        if st.button("불러오기"):
            session_data = sm.load_session(selected_session)
            st.session_state.session_id = selected_session
            st.session_state.topic = session_data['topic']
            st.session_state.current_hat = session_data['current_hat']
            st.session_state.responses = session_data['responses']
            st.rerun()
    else:
        st.info("저장된 세션이 없습니다.")

else:
    # 현재 세션 표시
    st.title(f"주제: {st.session_state.topic}")
    
    # 모자 선택
    cols = st.columns(6)
    hat_emojis = {
        "white": "🤍", "red": "❤️", "black": "🖤",
        "yellow": "💛", "green": "💚", "blue": "💙"
    }
    
    for i, (hat, emoji) in enumerate(hat_emojis.items()):
        with cols[i]:
            if st.button(
                f"{emoji} {hat.capitalize()}",
                type="primary" if hat == st.session_state.current_hat else "secondary"
            ):
                st.session_state.current_hat = hat
                st.rerun()
    
    st.markdown("---")
    
    # 현재 모자 섹션
    current_hat = st.session_state.current_hat
    hat_name = current_hat.capitalize()
    hat_emoji = hat_emojis[current_hat]
    
    st.header(f"{hat_emoji} {hat_name} Hat Thinking")
    st.markdown(sh.get_hat_description(current_hat))
    
    # 이전 응답 표시
    if current_hat in st.session_state.responses:
        with st.expander("이전 생각 보기"):
            st.markdown(st.session_state.responses[current_hat])
    
    # 사용자 입력
    user_input = st.text_area("생각을 입력하세요:")
    
    if st.button("생각 발전시키기", type="primary"):
        if user_input.strip():
            with st.spinner("AI가 생각을 발전시키는 중..."):
                response = ai.get_hat_response(
                    topic=st.session_state.topic,
                    hat=current_hat,
                    user_input=user_input
                )
                st.session_state.responses[current_hat] = response
                
                # 세션 저장
                sm.save_session({
                    'id': st.session_state.session_id,
                    'topic': st.session_state.topic,
                    'current_hat': current_hat,
                    'responses': st.session_state.responses
                })
                
                st.rerun()
        else:
            st.error("생각을 입력해주세요.")
    
    # 최종 결과 내보내기
    st.markdown("---")
    if st.button("최종 결과 정리"):
        if len(st.session_state.responses) > 0:
            with st.spinner("최종 결과를 정리하는 중..."):
                final_summary = ai.get_final_summary(
                    topic=st.session_state.topic,
                    responses=st.session_state.responses
                )
                st.markdown("### 최종 결과")
                st.markdown(final_summary)
        else:
            st.error("아직 기록된 생각이 없습니다.")