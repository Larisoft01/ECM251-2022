from cProfile import label
from turtle import onclick
import streamlit as st
with open('style2.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    


  

col1, col2, col3 = st.columns([2,2,2])                          
if st.session_state.user != None:
 with col1:
  with st.form("Pokeball"): 
   st.image("https://i.imgur.com/Y3JsQfP.png", width = 196)
   st.header("Pokeball")
   st.write("$200")
   button1 = st.form_submit_button("Buy")
   if button1:
     st.success("Item in cartshop, please go to payment/cartshop")
     
  with st.form("Potion"): 
   st.image("https://i.imgur.com/Kw0tRPq.png")
   st.header("Potion")
   st.write("$300")
   button2 = st.form_submit_button("Buy")
   if button2:
     st.success("Item in cartshop, please go to payment/cartshop")
     
   
 with col2:
  with st.form("Greatball"):
   st.image("https://i.imgur.com/KWYcRtb.png", width = 206)
   st.header("Greatball")
   st.write('$600')
   button3 = st.form_submit_button("Buy")
   if button3:
     st.success("Item in cartshop, please go to payment/cartshop")
   
  with st.form("Superpotion"):
   st.image("https://i.imgur.com/1NlKU7p.png", width = 163)
   st.header("Superpotion")
   st.write("$700")
   button4 = st.form_submit_button("Buy")
   if button4:
     st.success("Item in cartshop, please go to payment/cartshop")
   

 with col3:
  with st.form("Ultraball"):
   st.image("https://i.imgur.com/QqnE3wA.png", width = 192 )
   st.header("Ultraball")
   st.write("$1200") 
   button5 = st.form_submit_button("Buy")
   if button5:
     st.success("Item in cartshop, please go to payment/cartshop")
   
  with st.form("Hyperpotion"):
   st.image("https://i.imgur.com/JMMPnY0.png", width = 207)
   st.header("Hyperpotion")
   st.write("$1200")
   button6 = st.form_submit_button("Buy")
   if button6:
     st.success("Item in cartshop, please go to payment/cartshop")
else:
  st.error("Please, Log In, before you see this page")  