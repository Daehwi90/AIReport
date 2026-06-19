import streamlit as st
import streamlit.components.v1 as components
import os

# 페이지 기본 설정
st.set_page_config(
    page_title="TrendPulse - 맞춤형 기술 트렌드 큐레이터",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Streamlit 기본 UI 요소 숨기기 및 여백 최소화 (프리미엄 디자인 유지)
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
        iframe {
            display: block;
            border: none;
            width: 100%;
        }
        div[data-testid="stConnectionStatus"] {
            display: none !important;
        }
        </style>
        """
st.html(hide_menu_style)

# index.html 파일 경로 탐색 및 로드
html_path = os.path.join(os.path.dirname(__file__), "index.html")

if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # Streamlit components를 통해 HTML 서빙 (데스크탑/모바일 화면에서 스크롤 지원)
    components.html(html_content, height=980, scrolling=True)
else:
    st.error("index.html 파일을 찾을 수 없습니다. 프로젝트 폴더 구성을 확인해 주세요.")
