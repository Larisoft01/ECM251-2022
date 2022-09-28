
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage

base = ttk.Window(
    title ="Minha GUI Mauá",
    size=(1024,400),
    position=(100,100),
    minsize=(600,300),
    maxsize= (1800,900),
    alpha=(0.75)
)
base.iconphoto(False, PhotoImage(file='pokemart.png.png'))

def acao_botao():
    print("click!")
#Criando um botão

ttk.Button(
    base,
    text='olá mundo',
    bootstyle='danger',
    command = acao_botao
    ).pack(side=LEFT, padx=15,pady=15)

#Ponto de entrada da Interface

base.mainloop()