import streamlit as st
from streamlit_folium import st_folium, folium_static
import pandas as pd
import random


st.image("images/bg.png")
st.header('	:seedling:변화 살펴보기', divider="rainbow")

if 'data' not in st.session_state:
    st.session_state['data'] = pd.read_csv("datas/life_trash.csv")
if 'loc' not in st.session_state:
    st.session_state['loc'] = "관악구"

st.sidebar.caption(f'{st.session_state['loc']} 환경정책과 {st.session_state['name']})


df = st.session_state['data']

with st.form("정보입력"):
    loc = st.selectbox("지역",list(df["지역"].unique()))

    df = df[df["지역"]==loc].copy()
    df["연도"] = df["연도"].astype(str)
    select = st.multiselect("그리기",["발생량","재활용품","음식물","소각","매립","1인당 배출량","주민수" ])
    submitted = st.form_submit_button("Submit")
if submitted:
    
    st.line_chart(data=df, x="연도", y=select, height = 500, use_container_width=True)

