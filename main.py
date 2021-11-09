from tkinter import *
import os

 
pasta = os.path.dirname(__file__)

def consulta():
    exec(open(pasta+"\\consulta.py").read(), {'c':pasta})
    
def stoke():
    exec(open(pasta+"\\stoke.py").read())
    
def venda():
    exec(open(pasta+"\\vender.py").read())

root = Tk()
root.geometry('700x500+0+0')
root.title('tela principal')

Label(root,text='petshopp nova era',fg='royal blue',font='arial 40 bold').place(x=135,y=15)
btn_stok= Button(root,text='STOKE',bg='white smoke',font='arial 20 bold',width='34',command=stoke).place(x=50,y=90)
btn_consulta= Button(root,text='CONSULTA',bg='white smoke',font='arial 20 bold',width='34',command=consulta).place(x=50,y=160)
btn_vender= Button(root,text='VENDER',bg='white smoke',font='arial 20 bold',width='34',command=venda).place(x=50,y=230)
btn_sair= Button(root,text='sair',bg='coral',font='arial 18 bold',width='25',command=root.destroy).place(x=150,y=300)

root.mainloop()