#https://www.datacamp.com/tutorial/tutorial-postgresql-python

#%%
from dotenv import load_dotenv
import streamlit as st
from langchain_community.utilities import sql_database
import psycopg2

load_dotenv()
st.set_page_config(page_title='Chat With DataBase',)#page_icon='database'
st.title('Chat With DataBase')

# def int_database:
#     db_url=f""

# conn = psycopg2.connect(database = "datacamp_courses", 
#                         user = "datacamp", 
#                         host= 'localhost',
#                         password = "postgresql_tutorial",
#                         port = 5432)

with st.sidebar:
    st.subheader('settings')
    st.text_input("Host", value="localhost", key="Host")
    st.text_input("Port", value="5432", key="Port")
    st.text_input("User", value="postgres", key="User")
    st.text_input("Password", type="password", value="admin", key="Password")
    st.text_input("Database", value="dvdrental", key="Database")
    if st.button('connect'):
        st.spinner('Connecting to database...'):
        conn = psycopg2.connect(database = st.session_state.Database, 
                                user = st.session_state.User, 
                                host= st.session_state.Host,
                                password = st.session_state.Password,
                                port = st.session_state.Port)
        st.success('Connected to database')


#%%
