from models.user import User
import streamlit as st


class UserController():
    def __init__(self):
        
         if 'user' not in st.session_state:
          st.session_state.user = None
         if 'users' not in st.ssesion_state:
            
           dawn = User(name = "Dawn", password = "piplups", email = "Dawn_poketrainer@sinnoh.com"),
           hilda = User(name = "Hilda", password = "N is my lover", email = "Hilda_poketrainer@unova.com"),
           may = User(name = "May", password = "torchic12", email ="May_poketrainer@hoenn.com")
           st.session_state.all_users = [dawn, hilda, may]


    def checkLogin(self, name, password):
        user_teste = None
        for x in st.session_state.all_users:
            if name == x.get_name() and x.check_password(password):
                user_teste = x
                break
        if user_teste == None:
                 st.error("User or Password incorrect")   
                 st.session_state.user = None
        else:
                 st.session_state.user = user_teste    
   

            
        