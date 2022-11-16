from models.user import User
from dao.user import UserDAO
import streamlit as st


class UserController():
        
    def __init__(self) -> None:
        pass

    def pickup_user(self, id) -> User:
        user = UserDAO.get_instance().get_user(id)
        return user

    def insert_user(self, user) -> bool:
        try:
            UserDAO.get_instance().insert_item(user)
        except:
            return False
        return True

    def pickup_all_users(self):
        users = UserDAO.get_instance().get_all()
        return users
    
    def verify_user(self, name, password):
        user = UserDAO.get_instance().get.user(name) 
        if user != None:
            return user.verify_user(password)
        else:
            return False
        
    def __init__(self):
        
         if 'user' not in st.session_state:
          st.session_state.user = None
         if 'users' not in st.session_state:
            
           dawn = User(name = "Dawn", password = "piplups", email = "Dawn_poketrainer@sinnoh.com"),
           hilda = User(name = "Hilda", password = "N", email = "Hilda_poketrainer@unova.com"),
           may = User(name = "May", password = "torchic12", email ="May_poketrainer@hoenn.com")
           st.session_state.all_users = [dawn, hilda, may] 
                  
    def checkLogin(self, name, password):
        user_teste = None
        for x in st.session_state.all_users:
            if name == "Dawn" and password == "piplups":
                user_teste = x
                break
            if name == "Hilda" and password == "N":
                user_teste = x
                break
            if name == "May" and password == "torchic12":
                user_teste = x
                break
        if user_teste == None:
                 st.error("User or Password incorrect")   
                 st.session_state.user = None
        else:
                 st.session_state.user = user_teste  
   

            
        