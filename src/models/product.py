import streamlit as st


class Product():
    def __init__(self, name, price) -> None:
         self.name = name
         self.price = price
         
         
    def get_name(self):
        return self._name
    
    def get_price(self):
        return self._price

      
    def __str__(self) -> str:
        return("Product(name:{name}, prince:{price}")