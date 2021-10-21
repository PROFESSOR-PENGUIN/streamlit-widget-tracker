import streamlit as st
from streamlit_widget_tracker import start_tracking

#start tracking
x=start_tracking(exclude_key=['is_hello','is_terr'])

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

