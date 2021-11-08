from tkinter import *

root = Tk()
root.geometry('700x500+0+0')
root.title('tela de vendas')


Label(root,text='tela de vendas',fg='royal blue',font='Arial 40 bold').place(x=135,y=0)

Label(root,text='produto:',fg='royal blue',font='Arial 18 bold').place(x=5,y=210)
produtoe = Entry(root,bd=3,font='Arial 15')
produtoe.place(x=110,y=212,width=160)
Label(root,text='stoke    :',fg='royal blue',font='Arial 18 bold').place(x=8,y=240)
stokee = Entry(root,bd=3,font='Arial 15')
stokee.place(x=110,y=242,width=73)
Label(root,text='valor     :',fg='royal blue',font='Arial 18 bold').place(x=5,y=270)
precoe = Entry(root,bd=3,font='Arial 15')
precoe.place(x=110,y=272,width=73)
Label(root,text='quantidade:',fg='royal blue',font='Arial 18 bold').place(x=5,y=300)
quante = Entry(root,bd=3,font='Arial 15')
quante.place(x=148,y=302,width=60)

btn_adicionar = Button(root,bg='royal blue',font='Arial 18 bold',text='ADD')
btn_adicionar.place(x=220,y=270,width=70,height=60)


Label(root,text='total :',fg='royal blue',font='Arial 18 bold').place(x=5,y=370)
Label(root,text='pagar :',fg='royal blue',font='Arial 18 bold').place(x=5,y=410)
pagare = Entry(root,bd=3,font='Arial 18')
pagare.place(x=90,y=415,width=73)
Label(root,text='troco :',fg='royal blue',font='Arial 18 bold').place(x=5,y=450)
btn_finalizar= Button(root,text='finalizar',bg='dodger blue',font='arial 16 bold',width='7',height='2')
btn_finalizar.place(x=180,y=419)
btn_sair= Button(root,text='sair',bg='coral',font='arial 16 bold',width='5',height='2',command=root.destroy)
btn_sair.place(x=290,y=419)


frame1 = Frame(root,borderwidth=2,relief='sunken',bg='snow')
frame1.place(x=300,y=55,width=380,height=300)

frame2 = Frame(root,borderwidth=2,relief='sunken',bg='snow')
frame2.place(x=10,y=55,width=250,height=150)


btn_selecionar = Button(root,text='selecionar',font=('Arial', 17),bg='LightSteelBlue2')
btn_selecionar.place(x=375,y=420,width=300)
btn_pesquisar= Button(root,text='buscar',font=('Arial', 17),bg='SkyBlue1')
btn_pesquisar.place(x=585,y=358)
buscare = Entry(root,font=('Arial',18),bd=3)
buscare.place(x=300,y=365,width=280,height=30)


root.mainloop()