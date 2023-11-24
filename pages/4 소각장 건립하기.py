import streamlit as st
import pandas as pd
import time
from gspread.exceptions import APIError


from streamlit_gsheets import GSheetsConnection

st.image("images/bg.png")
st.header('	:seedling:소각장 건립하기', divider="rainbow")

if 'name' not in st.session_state:
    st.session_state['name'] = 'noname'
if 'data' not in st.session_state:
    st.session_state['data'] = pd.read_csv("datas/life_trash.csv")

df = st.session_state['data']

df = df.drop(df[df['지역']=="계"].index)

st.write("다음은 현재 운영중인 소각장입니다.")
st.image("images/sogag.png")

st.write("소각장을 추가로 건립할 지역은")
loc1 = st.selectbox("지역",list(df["지역"].unique()))
st.write("입니다.")
st.write("분석의 근거는")
reason = st.text_area("  ", label_visibility='hidden')

conn = st.connection("gsheets", type=GSheetsConnection)

df1 = pd.DataFrame({"name":st.session_state['name'],
                    "loc":loc1,
                    "reason":reason}, index=[0])

button = st.button("제출하기")
if button:
    try:
        conn.create(worksheet=st.session_state['name'], data=df1)
    except APIError as e:
        if e.response.status_code == 400 and 'already exists' in str(e):
            conn.update(worksheet=st.session_state['name'], data=df1)
        else:
            raise  # 다른 APIError의 경우, 예외를 다시 발생시킴
    
    with st.spinner('저장중입니다...'):
        time.sleep(2)
        st.caption("저장이 완료되었습니다.")