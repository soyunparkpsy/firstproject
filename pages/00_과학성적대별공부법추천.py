import streamlit as st

st.set_page_config(page_title="🎈과학 공부법 추천기🎈", page_icon="🎓")

st.title("🎆 과학 성적별 공부법 & 교재 추천 프로그램 🎇")
st.markdown("""
    🧪 **당신의 과학 성적에 맞는 공부법과 추천 교재를 알려드릴게요!**
    
    점수를 선택해 주세요! 🎯
""")

score = st.slider("📊 과학 점수를 선택하세요 (0~100, 10점 간격)", 0, 100, 50, step=10)

st.markdown("---")

recommendations = {
    0: ("🌱 완전 기초부터 시작!",
        "- 🧠 **공부법:** 과학 용어부터 익히기\n- 📘 **추천 교재:** '기초부터 배우는 과학', '과학 첫걸음'",
        "https://contents.kyobobook.co.kr/sih/fit-in/458x0/pdt/9791192146065.jpg"),
    10: ("📘 개념 잡기 단계",
         "- 🧠 **공부법:** 단원별 핵심 키워드 정리\n- 📘 **추천 교재:** '개념 플러스 유형', '과학이 쉬워지는 책'",
         "https://contents.kyobobook.co.kr/sih/fit-in/458x0/pdt/7070016000919.jpg"),
    20: ("📗 기본 개념 정복!",
         "- 🧠 **공부법:** 개념 + 간단한 문제로 연습\n- 📘 **추천 교재:** 'EBS 중학 과학 스타트', '셀파 과학 기본편'",
         "https://contents.kyobobook.co.kr/sih/fit-in/458x0/pdt/9788954789233.jpg"),
    30: ("📙 개념 + 문제 연습 단계",
         "- 🧠 **공부법:** 각 단원별 문제로 실전 감각 키우기\n- 📘 **추천 교재:** '소년소녀, 과학하라!'",
         "https://contents.kyobobook.co.kr/sih/fit-in/458x0/pdt/9791187050186.jpg"),
    40: ("📕 중간 점수 도전!",
         "- 🧠 **공부법:** 자주 틀리는 단원 반복 학습\n- 📘 **추천 교재:** '우공비 과학', '백점 과학'",
         "https://contents.kyobobook.co.kr/sih/fit-in/458x0/pdt/9788928350612.jpg"),
    50: ("📒 중위권 상승 준비!",
         "- 🧠 **공부법:** 문제 유형별 접근법 익히기\n- 📘 **추천 교재:** '오투 과학', '완자 과학'",
         "https://contents.kyobobook.co.kr/sih/fit-in/458x0/pdt/9791169409483.jpg"),
    60: ("📔 실력 다지기 단계",
         "- 🧠 **공부법:** 단원 간 개념 연결하며 공부\n- 📘 **추천 교재:** '탑클래스 과학', '내공의 힘 과학'",
         "https://cdn.pixabay.com/photo/2018/04/18/18/56/desk-3335409_1280.jpg"),
    70: ("📙 상위권 진입!",
         "- 🧠 **공부법:** 기출문제 분석 + 시간관리 연습\n- 📘 **추천 교재:** '백발백중 과학', '기출의 미래'",
         "https://cdn.pixabay.com/photo/2016/11/29/02/01/adult-1868750_1280.jpg"),
    80: ("📗 고난도 문제 도전!",
         "- 🧠 **공부법:** 오답노트로 자기 약점 파악\n- 📘 **추천 교재:** '자이스토리 과학', '마더텅 과학 고난도'",
         "https://cdn.pixabay.com/photo/2016/10/25/13/42/classroom-1763661_1280.jpg"),
    90: ("📕 고득점 마무리",
         "- 🧠 **공부법:** 실전 모의고사 풀이 + 친구에게 설명하며 정리\n- 📘 **추천 교재:** '숨마쿰라우데 최상위편', '리더스 과학'",
         "https://cdn.pixabay.com/photo/2016/11/19/20/56/adult-1839369_1280.jpg"),
    100: ("🎓 만점 완성 전략!",
          "- 🧠 **공부법:** 시간 배분 연습 + 기출 최종 정리\n- 📘 **추천 교재:** '만점왕 과학', '최종점검 과학특강'",
          "https://cdn.pixabay.com/photo/2020/01/04/07/58/graduation-4740088_1280.jpg")
}

title, content, image_url = recommendations.get(score)

st.subheader(f"{title} 🎈")
st.markdown(content)
st.image(image_url, caption="추천 이미지")

st.markdown("""
    ---
    🚀 **꾸준히만 하면 누구나 과학 100점!** 오늘도 공부 파이팅입니다! 💪🎉
""")
