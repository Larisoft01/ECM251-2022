import streamlit as st 
from models.product import Product

class PController():
    def __init__(self):
        
        if 'cartshop' not in st.session_state:
            st.session_state.cartshop = []
            
        if 'pokeproducts' not in st.session_state:
            
            pb = Product(name = 'PokeBall', price = "$200", url="" )
            gb = Product(name = 'GreatBall', price = "$600", url="" )
            ub = Product(name = 'UltraBall', price = "$1200", url="" )
            po = Product(name = 'PokeBall', price = "$300", url="" )
            sp = Product(name = 'PokeBall', price = "$700", url="" )
            hp = Product(name = 'PokeBall', price = "$1200", url="" )
            
            st.session_state.pokeproducts =[pb, gb, ub, po, sp, hp]

    