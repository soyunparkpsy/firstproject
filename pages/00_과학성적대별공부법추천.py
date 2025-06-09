import streamlit as st

st.set_page_config(page_title="🎈과학 공부법 추천기🎈", page_icon="🎓")

st.title("🎆 과학 성적별 공부법 & 교재 추천 프로그램 🎇")
st.markdown("""
    🧪 **당신의 과학 성적에 맞는 공부법과 추천 교재를 알려드릴게요!**
    
    점수를 선택해 주세요! 🎯
""")

score = st.selectbox("📊 과학 점수를 선택하세요", options=list(range(0, 101, 10)))

st.markdown("---")

if score < 40:
    st.subheader("📘 입문자용 추천 🎈")
    st.markdown("""
    - 🧠 **공부법:** 기초 개념 위주로 천천히, 하루 30분씩 꾸준히 공부해요.
    - 📕 **추천 교재:** '쉽게 배우는 중학 과학', '개념 잡는 과학 기초'
    - 🔍 **팁:** 유튜브 개념 설명 영상과 카드뉴스 활용 추천!
    """)
    st.image("https://cdn.pixabay.com/photo/2020/04/21/13/30/book-5077899_1280.jpg", caption="기초 개념 도서")

elif score < 70:
    st.subheader("📗 중급자용 추천 🎈🎈")
    st.markdown("""
    - 🧠 **공부법:** 단원별 요점 정리 + 문제풀이 병행
    - 📘 **추천 교재:** '오투 과학', '완자 과학'
    - 🔍 **팁:** 오답노트를 꼭 만들고, 문제마다 이유를 써보세요!
    """)
    st.image("https://cdn.pixabay.com/photo/2015/09/05/21/51/reading-925589_1280.jpg", caption="문제풀이와 개념 정리")

else:
    st.subheader("📕 고득점자용 추천 🎈🎈🎈")
    st.markdown("""
    - 🧠 **공부법:** 고난도 문제 위주로 실력 다지기 + 최신 기출 분석
    - 📗 **추천 교재:** '백발백중 과학', '탑클래스 과학'
    - 🔍 **팁:** 친구에게 설명하면서 개념 정리, 실전처럼 모의고사 풀기!
    """)
    st.image("https://cdn.pixabay.com/photo/2016/11/29/02/01/adult-1868750_1280.jpg", caption="고득점 전략")

st.markdown("""
    ---
    🚀 **꾸준히만 하면 누구나 과학 100점!** 오늘도 공부 파이팅입니다! 💪🎉
""")
