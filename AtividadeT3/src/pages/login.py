
from cProfile import label
from turtle import onclick
import streamlit as st
from controllers.usercontroller import UserController
from models.user import User


with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background: #FFFFFF url("https://i.imgur.com/9zFlKFo.png") no-repeat scroll 100% 50%;

[data-testid="stHeader"] {
    background: transparent none repeat fixed 50% 50%;
}

[data-testid="stToolbar"] {
    right: 2rem;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html = True) 
if 'user' not in st.session_state:
           st.session_state.user = None


col1, col2, col3 = st.columns([35,1,1])

with col1: 
 
    st.markdown("### Painel de Login")   
    if st.session_state.user == None:
        email=st.text_input("Name", placeholder = "Name")
        password=st.text_input("Password", placeholder = "Password", type ="password")
        remember=st.checkbox("Remember Me")
        button =st.button("Login")
        if button:
            UserController().checkLogin(email, password)
    else:
        st.success("You are Logged! Go to the Products Page!")
          
    
      
       

