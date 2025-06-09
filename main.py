import streamlit as st

if "balloon_shown" not in st.session_state:
    st.session_state.balloon_shown = False

st.title("🎬 MBTI 기반 수학·과학 영화 추천기 💡")
st.subheader("당신의 성향에 맞는 영화, 풍부하게 소개해드릴게요! 🎓🧬")

mbti_movies = {
    "INTJ": [
        {
            "title": "인터스텔라 🌌",
            "poster": "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
            "description": "지구의 자원이 고갈된 미래, 우주로 인류의 희망을 찾아 떠나는 과학자들의 이야기. 블랙홀과 시공간의 경계를 넘나드는 걸작.",
            "characters": "쿠퍼(매튜 맥커너히), 브랜드 박사(앤 해서웨이)"
        },
        {
            "title": "굿 윌 헌팅 🧠",
            "poster": "https://upload.wikimedia.org/wikipedia/en/5/52/Good_Will_Hunting.png",
            "description": "MIT에서 일하는 청소부 윌은 놀라운 수학적 재능을 가졌지만 마음의 상처로 세상과 벽을 쌓고 살아간다. 한 심리학자의 따뜻한 접근이 그의 삶을 바꾼다.",
            "characters": "윌 헌팅(맷 데이먼), 숀 매과이어(로빈 윌리엄스)"
        }
    ], 
    "ISTJ": [
        {
            "title": "소셜 네트워크 🌐",
            "poster": "https://upload.wikimedia.org/wikipedia/en/7/7a/The_Social_Network_film_poster.png",
            "description": "페이스북을 창업한 마크 저커버그의 천재성과 그 이면의 법적, 인간적 갈등.",
            "characters": "마크 저커버그(제시 아이젠버그), 에두아르도 세버린(앤드류 가필드)"
        },
        {
            "title": "천재들의 수수께끼 🎲",
            "poster": "https://upload.wikimedia.org/wikipedia/en/b/b0/Proof_poster.jpg",
            "description": "수학적 재능을 가진 딸과 천재였던 아버지의 유산 사이의 갈등과 사랑.",
            "characters": "캐서린(기네스 팰트로), 로버트(앤서니 홉킨스)"
        }
    ],
    "ESTJ": [
        {
            "title": "스티브 잡스 🍏",
            "poster": "https://upload.wikimedia.org/wikipedia/en/f/fa/Steve_Jobs_2015_film_poster.jpg",
            "description": "애플 창립자 스티브 잡스의 혁신과 집착을 세 장면으로 담아낸 전기 영화.",
            "characters": "스티브 잡스(마이클 패스벤더), 조안나(케이트 윈슬렛)"
        },
        {
            "title": "디스커버리 과학특집 🔍",
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Discovery_Channel_Logo.svg/320px-Discovery_Channel_Logo.svg.png",
            "description": "과학과 기술의 경이로움을 보여주는 디스커버리 채널의 인기 다큐멘터리 시리즈.",
            "characters": "해설자, 과학 전문가들"
        }
    ],
    "ESFJ": [
        {
            "title": "드림걸즈 🎤",
            "poster": "https://upload.wikimedia.org/wikipedia/en/9/9f/Dreamgirls_film_poster.jpg",
            "description": "1960년대 흑인 여성 보컬 그룹의 성공과 우정, 그리고 음악 산업의 현실.",
            "characters": "디나(비욘세 놀스), 에피(제니퍼 허드슨)"
        },
        {
            "title": "패신저스 ✨",
            "poster": "https://upload.wikimedia.org/wikipedia/en/8/8e/Passengers_2016_film_poster.jpg",
            "description": "우주여행 중 깨어난 두 남녀의 운명과 사랑을 그린 SF 로맨스.",
            "characters": "짐(크리스 프랫), 오로라(제니퍼 로렌스)"
        }
    ],
    "ENTJ": [
        {
            "title": "오펜하이머 💣",
            "poster": "https://upload.wikimedia.org/wikipedia/en/7/7f/Oppenheimer_%282023%29_poster.jpg",
            "description": "원자폭탄의 아버지 로버트 오펜하이머의 천재성과 정치적 고뇌.",
            "characters": "오펜하이머(킬리언 머피), 스트로스(로버트 다우니 주니어)"
        },
        {
            "title": "킹스맨 🕴️",
            "poster": "https://upload.wikimedia.org/wikipedia/en/8/8b/Kingsman_The_Secret_Service_poster.jpg",
            "description": "비밀 요원 양성 학교 '킹스맨'에서 벌어지는 스타일리시한 첩보 액션.",
            "characters": "에그시(태런 에저튼), 해리(콜린 퍼스)"
        }
    ],
    "ESTP": [
        {
            "title": "엣지 오브 투모로우 ⏳",
            "poster": "https://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg",
            "description": "시간을 되돌리는 능력을 얻은 병사가 외계 침략에 맞서는 SF 전쟁 영화.",
            "characters": "케이지(톰 크루즈), 리타(에밀리 블런트)"
        },
        {
            "title": "인셉션 🌀",
            "poster": "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
            "description": "꿈을 설계하고 침투하는 전문가들의 위험한 임무.",
            "characters": "돔 코브(레오나르도 디카프리오), 아서(조셉 고든 레빗)"
        }
    ],
    "ISTP": [
        {
            "title": "메멘토 🧠",
            "poster": "https://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg",
            "description": "단기 기억상실증을 앓는 남자의 미스터리한 복수극.",
            "characters": "레너드(가이 피어스), 나탈리(캐리앤 모스)"
        },
        {
            "title": "인디펜던스 데이 🛸",
            "poster": "https://upload.wikimedia.org/wikipedia/en/b/bb/Independence_day_movieposter.jpg",
            "description": "외계인의 지구 침공에 맞서 전 세계가 단결해 싸우는 블록버스터.",
            "characters": "힐러(윌 스미스), 휘트모어 대통령(빌 풀먼)"
        }
    ],
    "ISFP": [
        {
            "title": "라라랜드 🎶",
            "poster": "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
            "description": "꿈을 좇는 두 예술가의 낭만적이고 현실적인 러브 스토리.",
            "characters": "미아(엠마 스톤), 세바스찬(라이언 고슬링)"
        },
        {
            "title": "트루먼 쇼 🎥",
            "poster": "https://upload.wikimedia.org/wikipedia/en/8/82/Truman_Show_Poster.jpg",
            "description": "자신의 삶이 리얼리티 쇼임을 알게 된 남자의 자아 찾기 여정.",
            "characters": "트루먼 버뱅크(짐 캐리), 크리스토프(에드 해리스)"
        }
    ],
    "ESFP": [
        {
            "title": "나우 유 씨 미 🎩",
            "poster": "https://upload.wikimedia.org/wikipedia/en/3/3d/Now_You_See_Me_Poster.jpg",
            "description": "마술을 이용해 범죄를 저지르는 천재 마술사 팀의 스릴 넘치는 이야기.",
            "characters": "J. 다니엘 애틀라스(제시 아이젠버그), 딜런(마크 러팔로)"
        },
        {
            "title": "백 투 더 퓨처 ⏰",
            "poster": "https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg",
            "description": "타임머신을 탄 소년이 과거로 돌아가 벌어지는 해프닝과 시간여행의 모험.",
            "characters": "마티(마이클 J. 폭스), 브라운 박사(크리스토퍼 로이드)"
        }
    ]
    # 다른 MBTI도 필요하면 추가해줄게
}

selected_mbti = st.selectbox("🧭 MBTI를 선택하세요!", options=list(mbti_movies.keys()), index=0)

if selected_mbti:
    st.success(f"💡 {selected_mbti} 유형에게 추천하는 수학·과학 명작 영화 🎥")

    for movie in mbti_movies[selected_mbti]:
        st.markdown(f"## {movie['title']}")
        st.image(movie["poster"], width=250)
        st.markdown(f"**📖 줄거리**: {movie['description']}")
        st.markdown(f"**🧑‍🔬 주요 등장인물**: {movie['characters']}")
        st.markdown("---")

    if not st.session_state.balloon_shown:
        st.balloons()
        st.session_state.balloon_shown = True
