import streamlit as st

with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
 
    st.markdown("### Register a New Product")      
    nameoftheproduct=st.text_input("Name", placeholder = "Name")
    priceoftheproduct=st.number_input("Price", min_value=1.00)       
    button =st.button("Register")
    
    if button:
        product = Product(nameoftheproduct, priceoftheproduct)
        st.success("Your registration is completed!")
    else:
        st.error("please complete your registration")
    