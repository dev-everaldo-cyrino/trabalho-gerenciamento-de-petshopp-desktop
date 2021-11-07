from tkinter import *

root = Tk()
root.geometry('700x500+0+0')
root.title('consulta')

hora = StringVar()

Label(root,text='tela de consulta',fg='royal blue',font='Arial 40 bold').place(x=135,y=0)


Label(root,text='nome : ',fg='steelblue',font='arial 18 bold').place(x=15,y=50)
nomee = Entry(root,width='30')
nomee.place(x=100,y=60)


Label(root,text='data  :',fg='steelblue',font='arial 18 bold').place(x=15,y=100)
datae = Entry(root,width='30')
datae.place(x=100,y=110)


Label(root,text='horarios :',fg='steelblue',font='arial 18 bold').place(x=15,y=160)
horario1 = Radiobutton(root,text='7h-9h',value='manha1' ,variable=hora)
horario1.place(x=10,y=190)
horario2 = Radiobutton(root,text='9h30m-11hh',value='manha2' ,variable=hora)
horario2.place(x=80,y=190)
horario3 = Radiobutton(root,text='13h-15h',value='manha3' ,variable=hora)
horario3.place(x=10,y=210)
horario4 = Radiobutton(root,text='15h30m-17h',value='manha4' ,variable=hora)
horario4.place(x=80,y=210)


Label(root,text='motivo :',fg='steelblue',font='arial 18 bold').place(x=15,y=230)
obs = Text(root,height='5',width='30')
obs.place(x=15,y=270)


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