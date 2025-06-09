import streamlit as st

# 🎈 풍선 효과는 한 번만 보여주기
if "balloon_shown" not in st.session_state:
    st.session_state.balloon_shown = False

st.title("🎬 MBTI 기반 수학·과학 영화 추천기 💡")
st.subheader("당신의 성격에 딱 맞는 명작을 찾아드려요! 🧬🧠")

mbti_movies = {
    "INTJ": ["인터스텔라 🌌", "굿 윌 헌팅 🧠"],
    "INTP": ["큐리오시티 🔬", "비트맨 🎭"],
