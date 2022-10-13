from calendar import c
import streamlit as st 
import pandas as pd

 
with open('src/style3.css') as f:
  st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    

st.title("Welcome to Pokemart")
col1, col2 = st.columns([2,2]) 
with col1:
    st.subheader("About Us")
    st.write(" It is a convenience store that sells supplies necessary for Pokémon training. All Poké Marts will sell standard adventure supplies (such as HP and status condition healing items and Poké Balls), but some stores will also sell special items that are often unique to the store. ")
 
 
with col2:
    st.image('https://i.imgur.com/n8tWqv8.png')
    
with st.expander("Locations"): 
    locations = pd.read_csv("./src/data/Locations2.csv")
    options = st.multiselect(label="Select a Region", options=locations['Region'].unique(), default=locations['Region'].unique())
    st.dataframe(locations.query(f"Region in {options}"))
