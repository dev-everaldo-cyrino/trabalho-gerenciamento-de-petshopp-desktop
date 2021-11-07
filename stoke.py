from tkinter import *

root = Tk()
root.geometry('700x500+0+0')
root.title('consulta')

hora = StringVar()

Label(root,text='tela de stoke',fg='royal blue',font='Arial 40 bold').place(x=135,y=0)


Label(root,text='produto : ',fg='steelblue',font='arial 16 bold').place(x=5,y=50)
nomee = Entry(root,width='17',font=('Arial',15))
nomee.place(x=105,y=55)


Label(root,text='quant    :',fg='steelblue',font='arial 16 bold').place(x=5,y=100)
datae = Entry(root,width='5',font=('Arial',15))
datae.place(x=105,y=105)

Label(root,text='stoke    :',fg='steelblue',font='arial 16 bold').place(x=5,y=150)
datae = Entry(root,width='5',font=('Arial',15))
datae.place(x=105,y=155)

Label(root,text='preço    :',fg='steelblue',font='arial 16 bold').place(x=5,y=200)
datae = Entry(root,width='5',font=('Arial',15))
datae.place(x=105,y=205)

Label(root,text='fone     :',fg='steelblue',font='arial 16 bold').place(x=5,y=250)
datae = Entry(root,width='17',font=('Arial',15))
datae.place(x=100,y=255)









btn_cadastrar= Button(root,text='limpar',bg='salmon',font='arial 20 bold',height='3')
btn_cadastrar.place(x=170,y=365)
btn_cadastrar= Button(root,text='cadastrar',bg='dodger blue',font='arial 20 bold',width='8')
btn_cadastrar.place(x=10,y=365)
btn_cadastrar= Button(root,text='atualizar',bg='royal blue',font='arial 20 bold',width='8')
btn_cadastrar.place(x=10,y=429)


frame1 = Frame(root,borderwidth=2,relief='sunken',bg='snow')
frame1.place(x=300,y=55,width=380,height=300)


btn_selecionar = Button(root,text='selecionar',font=('Arial', 17),bg='LightSteelBlue2')
btn_selecionar.place(x=350,y=420,width=300)
btn_pesquisar= Button(root,text='buscar',font=('Arial', 17),bg='SkyBlue1')
btn_pesquisar.place(x=585,y=358)
buscare = Entry(root,font=('Arial',18),bd=3)
buscare.place(x=300,y=365,width=280,height=30)

root.mainloop()