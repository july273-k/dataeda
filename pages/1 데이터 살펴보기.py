import streamlit as st
import pandas as pd
from streamlit_folium import st_folium, folium_static
import time

st.image("images/bg.png")
st.header('	:seedling:데이터 살펴보기', divider="rainbow")

df = pd.read_csv("./datas/life_trash.csv")

if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame()
    
st.session_state['data'] = st.data_editor(df, use_container_width=True)

st.write("데이터 사이에는 어떤 관계가 있나요:question::question:")

time.sleep(20)

st.image("./images/q1.png", width=300)


st.write("어떤 데이터가 잘못되었는지 찾을 수 있나요:question::question:")

# with st.form("정보입력"):
#     loc = st.selectbox("year",list(df["지역"].unique()))

#     df = df[df["지역"]==loc].copy()
#     df["연도"] = df["연도"].astype(str)
#     select = st.multiselect("그리기",["발생량","재활용품 재활용","음식물 재활용","소각","매립"])
#     submitted = st.form_submit_button("Submit")
    
# if submitted:
    
#     st.line_chart(data=df, x="연도", y=select, height = 500, use_container_width=True)
