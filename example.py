import streamlit as st
from streamlit.report_thread import get_report_ctx
import logging
import warnings
import streamlit_text_like as st_like
from __init__ import start_tracking

#start tracking
x=start_tracking(exclude_key=['is_hello','is_terr'])

warnings.filterwarnings('ignore')
logging.basicConfig(level=logging.INFO)
ctx = get_report_ctx()

st.write(f"Current session is -- {ctx.session_id}")
r1=st_like.streamlit_text_like('He is good boy',key='is_rcb')
st.write(r1)
st.markdown("---")

select_territory = st.sidebar.selectbox("Select Param1",["Session_id","Show all"],key='is_terr')
select_territory = st.sidebar.selectbox(label="Select Param1", options=['a', 'b'], key='is_hello')
select_territory = st.sidebar.selectbox(label="Select Param1",options=["ab", "cd"],key='is_abc')
enable_mean_line = st.checkbox(label='Show Average Line',key='is_how')
normalize_trend = st.checkbox(label='Normalized Trend',key='is_when')
multiselect=st.multiselect(label="select",options=['a','b','c'],key='is_cool')
multiselect2=st.multiselect(label="select",options=['d','e','f'],key='is_cool2')
text_input=st.text_input(label="write text",key='is_text')
text_input=st.sidebar.text_input(label="write text",key='is_text_sidebar')

st.markdown("---")
st.write("Here is your tracker info")
st.write(x)

