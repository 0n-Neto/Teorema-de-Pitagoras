from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from functools import partial
import math

#-----------------------------= Master =----------------------------------------
janela = Tk()
janela.geometry("700x285")
janela.title("Teorema de Pitágoras")
image2 = Image.open("formula-pitagoras.jpg")
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
ed1.place(x=75, y=250)

ed2 = Entry(janela)
ed2.place(x=200, y=250)

lb = Label(janela, text="")
lb.place(x=330, y=250)
#---------------------------------------------------------------------------


#------------------------------= Botôes =-------------------------------------
bt = Button(janela, text="Pitagoras")
bt["command"] = partial(Pitagoras, bt)
bt.place(x=12, y=245)

#-----------------------------------------------------------------------------

janela.mainloop() 
