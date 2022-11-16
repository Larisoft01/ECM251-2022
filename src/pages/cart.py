import streamlit as st 
import pandas as pd

with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Payment")
    
st.subheader("How are you going to pay?")
payment = st.radio ("Metods:", ('PIX', 'Credit Card', 'Debit Card', 'Bank Slip'))

with st.expander("Locations to Pickup Your Product"): 
     locations = pd.read_csv("./data/Locations2.csv")
     options = st.multiselect(label="Select a Region to Pick Up The Product", options=locations['Region'].unique(), default=locations['Region'].unique())
     st.dataframe(locations.query(f"Region in {options}"))

done = st.button("Finish")