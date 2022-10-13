
import streamlit as st


class Product():
    def __init__(self, name, price, url) -> None:
         self.name = name
         self.price = price
         self.url = url
         
    def get_name(self):
        return self._name
    
    def get_name(self):
        return self._price
    
    def get_name(self):
        return self._url
      
    def __str__(self) -> str:
        return("Product(name:{name}, prince:{price}, url:{url})")