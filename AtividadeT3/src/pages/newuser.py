
from cProfile import label
from turtle import onclick
import streamlit as st
from models.user import User

with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if st.session_state.user !=None:
 
    st.markdown("### Register to the Site")      
    name=st.text_input("Name", placeholder = "Name")
    password=st.text_input("password", type = "password")  
    email=st.text_input("Email") 
        
    button =st.button("Register")
    
    if button:
        user = User(name, password, email)
        
        st.success("Your registration is completed!")
    else:
        st.error("Please, complete yhe registration")
    
        
    
else:
    st.error("Please, Log In, before you see this page") 