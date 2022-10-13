import streamlit as st 
import pandas as pd

with open('src/style.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def view_product(product):
    
    st.write({product.get_name()})
    st.write({product.get_price()})



if st.session_state.user != None:
    for product in st.session_state.cartshop:
        view_product(product)
    st.markdown("Payment")
    
    total = sum([product.get_price()for product in st.session_state.cartshop])
    st.write("Total Price: ${total}")
    st.markdown("How are you going to pay?")
    payment = st.radio ("Metods:", ('PIX', 'Credit Card', 'Debit Card', 'Bank Slip'))
    
    with st.expander("Locations"): 
     locations = pd.read_csv("./src/data/Locations2.csv")
     options = st.multiselect(label="Select a Region to Pick Up The Product", options=locations['Region'].unique(), default=locations['Region'].unique())
     st.dataframe(locations.query(f"Region in {options}"))
    