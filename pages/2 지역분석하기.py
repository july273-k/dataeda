import streamlit as st
import pandas as pd

import folium

from streamlit_folium import st_folium, folium_static

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from folium import plugins
from folium.features import DivIcon
import random

if 'loc' not in st.session_state:
    st.session_state['loc']="관악구"

st.sidebar.caption(f'{st.session_state['loc']} 환경정책과 {st.session_state['name']})


st.image("images/bg.png")
st.header('	:seedling:지역 분석하기', divider="rainbow")
geo_json='https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json'

df = pd.read_csv("./datas/life_trash.csv")
locs = {
    '금천구': (37.46918, 126.875887),
    '강남구': (37.51731, 127.0275),
    '강동구': (37.53013, 127.1238),
    '강북구': (37.63978, 126.9956),
    '관악구': (37.46815, 126.9315),
    '강서구': (37.550937, 126.819642),
    '구로구': (37.495472, 126.857536),
    '송파구': (37.5145636, 127.0959186),
    '서초구': (37.483569, 127.002598),
    '동작구': (37.50245, 126.9195),
    '영등포구': (37.526436, 126.896004),
    '양천구': (37.517016, 126.836642),
    '마포구': (37.5663245, 126.881491),
    '서대문구': (37.579225, 126.9168),
    '은평구': (37.602784, 126.909164),
    '노원구': (37.654358, 127.056473),
    '도봉구': (37.668768, 127.007163),
    '성북구': (37.5894, 127.000749),
    '중랑구': (37.6063242, 127.0725842),
    '동대문구': (37.574524, 127.03965),
    '광진구': (37.538617, 127.062375),
    '성동구': (37.543456, 127.016821),
    '용산구': (37.532527, 126.97049),
    '중구': (37.563843, 126.977602),
    '종로구': (37.6035207, 126.9588345)    
}
df = df.drop(df[df['지역']=="계"].index)
year = st.selectbox("year",list(df["연도"].unique()))
df = df[df["연도"]==year].copy()
select = st.selectbox("그리기",["발생량","재활용품","음식물","소각","매립"])
df2=df[['지역',select]]
df2.columns=['name','values']

m=folium.Map(
    location=[37.566345,127.057893],
    tiles='cartodbpositron',
    zoom_start=10)

choropleth = folium.Choropleth(
    geo_data=geo_json,
    name='choropleth',
    data=df2,
    columns=['name','values'],
    key_on='feature.properties.name',
    fill_color='YlGnBu',
    fill_opacity=0.7,
    line_opacity=0.2
).add_to(m)

for key, value in locs.items():
    folium.map.Marker(
        # 위경도 위치
        [value[0], value[1]+0.007],  

        # DivIcon 을 사용
        # html 태그를 이용해서 text를 올릴 수 있음
        icon=DivIcon(
            # icon px 사이즈
            icon_size=(0, 0),
            # icon 좌 상단 위치 설정
            icon_anchor=(0, 0),

            # html 형식으로 text 추가
            # div 태그 안에 style 형식 추가
            html='<div\
                    style="\
                        font-size: 0.8rem;\
                        color: black;\
                        background-color:rgba(255, 255, 255, 0.2);\
                        width:85px;\
                        text-align:center;\
                        margin:0px;\
                    "><b>'
            + key
            )).add_to(m)
    
#지도 전체화면 추가코드
plugins.Fullscreen(position='topright',
                   title='Click to Expand',
                   title_cancel='Click to Exit',
                   force_separate_button=True).add_to(m)

#지도 스크롤 가능
plugins.MousePosition().add_to(m)

#지도에 원하는 변수 이름 나오게 하는 코드
# choropleth.geojson.add_child(folium.features.GeoJsonTooltip(['tooltip1'], labels=False))
# title_html = '<h3 align="center" style="font-size:20px"><b>people index </b></h3>'
# m.get_root().html.add_child(folium.Element(title_html))

folium.LayerControl().add_to(m)

folium_static(m)

st.write("데이터를 보면서 특이한 점을 찾아봅시다.")
