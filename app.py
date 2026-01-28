import streamlit as st

# 페이지 설정
st.set_page_config(page_title="감성 뮤직 큐레이터", page_icon="🎧", layout="wide")

# 1. 테마 설정 데이터
themes = {
    "기본": {"bg": "#1E2321", "text": "#FFFFFF", "accent": "#A3C6AE", "effect": ""},
    "☀️ 화창한 날": {"bg": "#FFF9C4", "text": "#5D4037", "accent": "#FBC02D", "effect": "☀️ 눈부신 햇살 아래서"},
    "☔ 비 오는 날": {"bg": "#37474F", "text": "#ECEFF1", "accent": "#81D4FA", "effect": "🌧️ 창밖의 빗소리와 함께"},
    "☁️ 흐린 날": {"bg": "#78909C", "text": "#FFFFFF", "accent": "#CFD8DC", "effect": "☁️ 차분한 구름 아래"},
    "⛄ 눈 오는 날": {"bg": "#E3F2FD", "text": "#1565C0", "accent": "#90CAF9", "effect": "❄️ 하얗게 내리는 눈송이"},
    "🌸 봄": {"bg": "#FCE4EC", "text": "#880E4F", "accent": "#F06292", "effect": "🌸 흩날리는 벚꽃 잎"},
    "☀️ 여름": {"bg": "#E0F7FA", "text": "#006064", "accent": "#26C6DA", "effect": "🌊 시원한 파도 소리"},
    "🍂 가을": {"bg": "#EFEBE9", "text": "#4E342E", "accent": "#A1887F", "effect": "🍂 바스락거리는 낙엽"},
    "❄️ 겨울": {"bg": "#B0BEC5", "text": "#263238", "accent": "#546E7A", "effect": "❄️ 시린 겨울 밤의 온기"},
    "😊 기쁨": {"bg": "#FFFDE7", "text": "#F57F17", "accent": "#FFF59D", "effect": "🎉 세상을 다 가진 기분!"},
    "😢 슬픔": {"bg": "#263238", "text": "#90A4AE", "accent": "#546E7A", "effect": "💧 조용히 흐르는 눈물"},
    "🔥 열정": {"bg": "#FFEBEE", "text": "#B71C1C", "accent": "#EF5350", "effect": "🔥 멈추지 않는 에너지"},
    "🌿 차분함": {"bg": "#D7CCC8", "text": "#3E2723", "accent": "#8D6E63", "effect": "🌿 고요한 명상의 시간"},
    "🎸 밴드": {"bg": "#424242", "text": "#E0E0E0", "accent": "#616161", "effect": "🎸 차가운 도시의 밴드 사운드"},
    "🎤 힙합": {"bg": "#1A1A1A", "text": "#00E676", "accent": "#333333", "effect": "🎤 Swag 넘치는 비트"},
    "🎹 재즈": {"bg": "#3E2723", "text": "#D7CCC8", "accent": "#5D4037", "effect": "🎹 깊이 있는 선율"},
    "✨ K-POP": {"bg": "#F3E5F5", "text": "#7B1FA2", "accent": "#CE93D8", "effect": "✨ 빛나는 아이돌 무대"}
}

# 2. 세션 상태 초기화
if "current_theme" not in st.session_state:
    st.session_state.current_theme = "기본"
if "selected_list" not in st.session_state:
    st.session_state.selected_list = []

t = themes.get(st.session_state.current_theme, themes["기본"])

# 3. CSS 적용 (버튼 크기 통일)
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {t['bg']} !important;
        transition: all 0.8s ease;
    }}
    section[data-testid="stSidebar"] {{
        background-color: rgba(0,0,0,0.5) !important;
    }}
    section[data-testid="stSidebar"] * {{
        color: #FFFFFF !important;
        text-shadow: 1px 1px 3px rgba(0,0,0,1);
    }}
    h1, h2, h3, p, span, div, li {{
        color: {t['text']} !important;
    }}
    .main-title {{
        font-size: 55px !important;
        font-weight: 900;
        text-align: center;
        padding-top: 30px;
    }}
    /* ⭐ 버튼 크기 통일 핵심 CSS */
    div.stButton > button {{
        width: 100% !important;
        height: 70px !important;
        border-radius: 15px;
        background-color: {t['accent']} !important;
        color: {t['text']} !important;
        border: 2px solid rgba(255,255,255,0.1);
        font-weight: bold;
        font-size: 18px;
        margin-bottom: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

# 4. 음악 데이터셋
music_data = {
    "날씨": {
        "☀️ 화창한 날": ["Dynamite - BTS", "여행 - 볼빨간사춘기"],
        "☔ 비 오는 날": ["비도 오고 그래서 - 헤이즈", "Rain - 태연"],
        "☁️ 흐린 날": ["Lonely - 2NE1", "포커페이스 - 씨잼"],
        "⛄ 눈 오는 날": ["눈 - 자이언티", "첫눈처럼 너에게 가겠다 - 에일리"]
    },
    "계절": {
        "🌸 봄": ["벚꽃 엔딩 - 버스커 버스커", "봄 안녕 봄 - 아이유"],
        "☀️ 여름": ["Hot Summer - f(x)", "여름안에서 - 듀스"],
        "🍂 가을": ["가을 타나 봐 - 바이브", "가을 아침 - 아이유"],
        "❄️ 겨울": ["첫 눈 - 엑소", "Must have love - SG워너비, 브라운아이드걸스"]
    },
    "감정": {
        "😊 기쁨": ["Celebrity - 아이유", "Happy - Pharrell Williams"],
        "😢 슬픔": ["끝사랑 - 김범수", "어른 - Sondia"],
        "🔥 열정": ["불타오르네 - BTS", "Bang Bang Bang - BIGBANG"],
        "🌿 차분함": ["비오는 거리 - 이승훈", "나비와 고양이 - 볼빨간사춘기"]
    },
    "장르": {
        "🎸 밴드": ["Big Void - 실리카겔", "Get Back - Touched" , "월드투어 - 해밍웨이,보수동쿨러"],
        "🎤 힙합": ["Public Enemy - Lil moshpit, Sik-k", "skid mark - sikkoo", "25 - Kid Milli"],
        "🎹 재즈": ["Fly Me To The Moon", "Take Five"],
        "✨ K-POP": ["Seven - 정국", "LOVE DIVE - IVE", "Hype Boy - NewJeans"]
    }
}

# 5. 메인 화면 구성
st.markdown(f'<p class="main-title">🎵 {st.session_state.current_theme}</p>', unsafe_allow_html=True)
if t['effect']:
    st.markdown(f"<h3 style='text-align: center; opacity: 0.8;'>{t['effect']}</h3>", unsafe_allow_html=True)

# 그리드 레이아웃 (4열 고정)
for category, items in music_data.items():
    st.markdown(f"### 📌 {category}")
    cols = st.columns(4) # 모든 카테고리를 4열로 고정하여 버튼 크기 통일
    for i, (name, songs) in enumerate(items.items()):
        with cols[i % 4]:
            if st.button(name):
                st.session_state.current_theme = name
                st.session_state.selected_list = songs
                st.rerun()

# 6. 사이드바
with st.sidebar:
    st.markdown("<h1>🎧 PLAYLIST</h1>", unsafe_allow_html=True)
    st.write("---")
    if st.session_state.selected_list:
        for song in st.session_state.selected_list:
            st.markdown(f"**{song}**")
            url = f"https://www.youtube.com/results?search_query={song.replace(' ', '+')}"
            st.markdown(f"[Youtube 검색 🔗]({url})")
            st.write("---")
        
        if st.button("🔄 초기화"):
            st.session_state.current_theme = "기본"
            st.session_state.selected_list = []
            st.rerun()
    else:
        st.markdown("<b style='font-size: 18px;'>원하는 카테고리를 선택하세요!</b>", unsafe_allow_html=True)