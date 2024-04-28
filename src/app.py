#https://www.datacamp.com/tutorial/tutorial-postgresql-python
#%%
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
st.set_page_config(page_title='Chat With DataBase',)#page_icon='database'
st.title('Chat With DataBase')

with st.sidebar:
    st.subheader('settings')
    st.text_input("Host", value="localhost", key="Host")
    st.text_input("Port", value="5432", key="Port")
    st.text_input("User", value="postgres", key="User")
    st.text_input("Password", type="password", value="admin", key="Password")
    st.text_input("Database", value="dvdrental", key="Database")