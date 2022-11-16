import streamlit as st 
from AtividadeT3.src.models.product import Product
from AtividadeT3.src.dao.product import ProductDAO

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
            
class ItemController:
    def __init__(self) -> None:
        pass

    def pickup_product(self, id) -> Product:
        product = ProductDAO.get_instance().pickup_product(id)
        return product

    def insert_product(self, product) -> bool:
        try:
            ProductDAO.get_instance().inserir_item(product)
        except:
            return False
        return True

    def pickup_all_products(self) -> list[Product]:
        items = ProductDAO.get_instance().get_all()
        return items

    