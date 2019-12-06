from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from functools import partial
import math

#-----------------------------= Master =----------------------------------------
janela = Tk()
janela.geometry("700x285")
janela.title("Teorema de Pitágoras")
image2 = Image.open("dicas-de-fórmula-de-pitágoras.jpg")
image1 = ImageTk.PhotoImage(image2)
background_label = Label(janela, image=image1)
background_label.image1=image1
background_label.place(x=0, y=0, width=700, height=285)

#---------------------------------------------------------------------------

#-----------------------------= Funções =---------------------------------
def Pitagoras(hip):
	cat1 = int(ed1.get())
	cat2 = int(ed2.get())
	lb["text"] = math.hypot(cat1, cat2)

#--------------------------------------------------------------------------

#-------------------------------= Labels =-------------------------------------
ed1 = Entry(janela)
ed1.pack()

ed2 = Entry(janela)
ed2.pack()

lb = Label(janela, text="")
lb.pack()
#---------------------------------------------------------------------------


#------------------------------= Botôes =-------------------------------------
bt = Button(janela, text="Pitagoras")
bt["command"] = partial(Pitagoras, bt)
bt.pack()

#-----------------------------------------------------------------------------

janela.mainloop() 
