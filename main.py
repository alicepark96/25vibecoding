import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="MBTI 담임 유형 테스트 🧑‍🏫", page_icon="🧠", layout="centered")

st.title("당신의 MBTI는 어떤 담임쌤일까요? 🤔👩‍🏫👨‍🏫")
st.subheader("MBTI를 선택하면 그에 맞는 교사 캐릭터가 짠!✨")

mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

user_mbti = st.selectbox("당신의 MBTI를 선택하세요 👇", mbti_list)

# MBTI별 교사 캐릭터 사전
mbti_teacher_profiles = {
    "ISTJ": "📋 **ISTJ 담임쌤** - '규칙은 소중해요' 📏\n✅ 출석부는 늘 정확히 체크\n🕘 5분 전에 출근, 5분 전에 종례 준비 완료\n📎 시험지 3번 검토하는 꼼꼼함!",
    "ISFJ": "🧸 **ISFJ 담임쌤** - '우리 애들 잘 챙겨야죠' 💖\n🍪 간식 나눠주는 천사 쌤\n📌 상
