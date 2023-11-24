import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
import time
from streamlit_extras.switch_page_button import switch_page 

st.image("images/bg.png")
st.header('	:seedling:서울특별시 :blue[환경 데이터] 플랫폼', divider="rainbow")

st.divider()

if 'name' not in st.session_state:
    st.session_state['name'] = ''
    
    
if 'pw' not in st.session_state:
    st.session_state['pw'] = ''


with st.form("로그인"):
    col1, col2 = st.columns(2)
    with col1 : 
        st.session_state['name'] = st.text_input("이름", key="a")
    with col2 : 
        st.session_state['pw'] = st.text_input("비밀번호", key="b", type="password")
    submitted = st.form_submit_button("로그인")

if submitted:
    with st.spinner('로그인중입니다...'):
        time.sleep(2)
    if len(st.session_state['pw'])>7:
        st.caption(f"{st.session_state['name']}님 로그인 되었습니다.")
   
    
        conn = st.connection("gsheets", type=GSheetsConnection)

        df = conn.read(
            worksheet="Sheet1",
            ttl="10m",
            usecols=[0, 1],
            nrows=100
        )
        df = df.dropna(axis=0)

        df_new = pd.DataFrame([{"name": st.session_state['name'],
                            "pw": st.session_state['pw']
                            }])
        df_copy = df.copy()
        df_result = pd.concat([df_copy,df_new], ignore_index=True)
        conn.update(worksheet="Sheet1", data=df_result)


        my_bar = st.progress(0, text='잠시후 페이지를 이동합니다.')

        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text='잠시후 페이지를 이동합니다.')
        
        switch_page("데이터 살펴보기")

    else:
        st.caption("8자 보다 긴 비밀번호를 설정하세요.")


# if st.button("new sheet"):
#     df1 = pd.DataFrame({"A":[1,2,3],
#                    "B":[3,4,5],
#                    "C":[7,8,9]})
#     conn.create(worksheet="abcd", data=df1)
#     st.success("Done")
    
# if st.button("Calculate Total Orders Sum"):
#     sql = 'SELECT SUM("age") as "ass" FROM "Sheet1";'
#     total_orders = conn.query(sql=sql)
#     st.write(total_orders)
        
# name = st.text_input("name", "name")
# pet = st.text_input("pet","pet")
# age = st.slider("age",min_value=0, step=1)
        
# if st.button("insert"):
#     df_copy = df.copy()
#     df_new = pd.DataFrame([{"name": name,
#                            "pet": pet,
#                            "age": age}])
#     df_new
#     df_result = pd.concat([df_copy,df_new], ignore_index=True)
#     conn.update(worksheet="Sheet1", data=df_result)
#     st.success("Worksheet Updated 🤓")