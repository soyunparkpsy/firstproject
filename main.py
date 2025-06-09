import streamlit as st

# 🎈 풍선 효과는 딱 한 번만 등장하게 하자!
if "balloon_shown" not in st.session_state:
    st.session_state.balloon_shown = False

st.title("🎬 MBTI 기반 수학·과학 영화 추천기 💡")
st.subheader("당신의 성격에 딱 맞는 명작을 찾아드려요! 🧬🧠")

mbti_input = st.text_input("👉 MBTI 4글자를 입력하세요 (예: INFP, ESTJ 등)", max_chars=4)

mbti_movies = {
    "INTJ": ["인터스텔라 🌌", "굿 윌 헌팅 🧠"],
    "INTP": ["큐리오시티 🔬", "비트맨 🎭"],
    "ENTP": ["매트릭스 🕶️", "아이로봇 🤖"],
    "ENFP": ["마션 🚀", "히든 피겨스 👩‍🚀"],
    "INFJ": ["어벤져스: 엔드게임 🔮", "인셉션 🌀"],
    "INFP": ["월-E 🤖", "컨택트 👽"],
    "ISFJ": ["아름다운 마음 🧮", "체르노빌 ⚠️"],
    "ISTJ": ["소셜 네트워크 🌐", "천재들의 수수께끼 🎲"],
    "ESTJ": ["스티브 잡스 🍏", "디스커버리 과학특집 🔍"],
    "ESFJ": ["드림걸즈 🎤", "패신저스 ✨"],
    "ENTJ": ["오펜하이머 💣", "킹스맨 🕴️"],
    "ESTP": ["인셉션 🌀", "엣지 오브 투모로우 ⏳"],
    "ISTP": ["메멘토 🧠", "인디펜던스 데이 🛸"],
    "ISFP": ["라라랜드 🎶", "트루먼 쇼 🎥"],
    "ESFP": ["나우 유 씨 미 🎩", "백 투 더 퓨처 ⏰"],
    "ENFJ": ["인터스텔라 🌌", "소셜 딜레마 📱"]
}

mbti_input_clean = mbti_input.strip().upper()

if mbti_input_clean in mbti_movies:
    st.success(f"💡 {mbti_input_clean} 유형에게 추천하는 영화는... 🎉")
    for movie in mbti_movies[mbti_input_clean]:
        st.markdown(f"- {movie}")
    
    # 한 번만 풍선 효과 🎈
    if not st.session_state.balloon_shown:
        st.balloons()
        st.session_state.balloon_shown = True
else:
    if mbti_input:
        st.warning("😥 올바른 MBTI 4글자를 입력해주세요! (예: INFP, ENTJ 등)")
