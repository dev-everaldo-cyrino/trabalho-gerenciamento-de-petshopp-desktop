from tkinter import *

root = Tk()
root.geometry('700x500+0+0')
root.title('tela principal')

Label(root,text='petshopp nova era',fg='royal blue',font='arial 40 bold').place(x=135,y=15)
btn_stok= Button(root,text='STOKE',bg='white smoke',font='arial 20 bold',width='34').place(x=50,y=90)
btn_stok= Button(root,text='CONSULTA',bg='white smoke',font='arial 20 bold',width='34').place(x=50,y=160)
btn_stok= Button(root,text='VENDER',bg='white smoke',font='arial 20 bold',width='34').place(x=50,y=230)

root.mainloop()