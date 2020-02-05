from tkinter import * #Criado Por Maurício P.(Shark)
import tkinter as tk  #Coding: UTF-8
from PIL import ImageTk, Image
from functools import partial
import math

#-----------------------------= Master =----------------------------------------
janela = Tk()
janela.title("Teorema de Pitágoras")

largura = 700
altura = 285

largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenheight()

posx = largura_screen/2 - largura/2
posy = altura_screen/2 - largura/2

janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
janela.resizable(False, False)

#------------------------------= BG =------------------------------------------------

image2 = Image.open("formula-pitagoras.jpg")  #<---- Uma forma criativa de usar uma imagem como BackGround.
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
#--------------------------------------------------------------------------------
