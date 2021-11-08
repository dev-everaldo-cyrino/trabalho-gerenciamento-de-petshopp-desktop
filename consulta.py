from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

banco = sqlite3.connect('petshopp.db')
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS agenda1 (nome text, dataa text, horario text , obs text)")
banco.commit()

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
horario1 = Radiobutton(root,text='7h-9h',value='7h-9h' ,variable=hora)
horario1.place(x=10,y=190)
horario2 = Radiobutton(root,text='9h30m-11h',value='9h30m-11h' ,variable=hora)
horario2.place(x=80,y=190)
horario3 = Radiobutton(root,text='13h-15h',value='13h-15h' ,variable=hora)
horario3.place(x=10,y=210)
horario4 = Radiobutton(root,text='15h30m-17h',value='15h30m-17h' ,variable=hora)
horario4.place(x=80,y=210)


Label(root,text='motivo :',fg='steelblue',font='arial 18 bold').place(x=15,y=230)
obse = Text(root,height='5',width='30')
obse.place(x=15,y=270)


def inserir():
    nome = nomee.get()
    data = datae.get()
    
    obs = obse.get('1.0',END)
    if nome == '' or data == '':
         messagebox.showerror(title='mensagem de erro',message='preencha todos os campos')
    else:
        cursor.execute("INSERT INTO agenda1 VALUES('{}','{}','{}','{}')".format(nome,data,hora.get(),obs))
        banco.commit()

btn_limpar= Button(root,text='limpar',bg='salmon',font='arial 20 bold',height='3')
btn_limpar.place(x=170,y=365)
btn_cadastrar= Button(root,text='cadastrar',bg='dodger blue',font='arial 20 bold',width='8',command=inserir)
btn_cadastrar.place(x=10,y=365)
btn_atualizar= Button(root,text='atualizar',bg='royal blue',font='arial 20 bold',width='8')
btn_atualizar.place(x=10,y=429)
btn_sair= Button(root,text='sair',bg='coral',font='arial 16 bold',width='5',height='2',command=root.destroy)
btn_sair.place(x=290,y=419)


frame1 = Frame(root,borderwidth=2,relief='sunken',bg='snow')
frame1.place(x=300,y=65,width=380,height=290)
tabela = ttk.Treeview( frame1,
columns = (1,2),
height = 15,
show = 'headings')
tabela.pack( side = 'left')
tabela.heading(1, text='data')
tabela.heading(2, text='horario')
tabela.column(1, width = 180 )
tabela.column(2, width = 180 )

barrarolagem = ttk.Scrollbar( frame1,orient='vertical',
 command=tabela.yview)
barrarolagem.pack( side = 'right', fill='y')
tabela.configure(yscrollcommand = barrarolagem.set)

cursor.execute('SELECT * FROM  agenda1')
id = cursor.fetchall()
num=0
for x in range(len(id)):
    tabela.insert("","end",values=(id[num][1],id[num][2]))
    num +=1


btn_selecionar = Button(root,text='selecionar',font=('Arial', 17),bg='LightSteelBlue2')
btn_selecionar.place(x=375,y=420,width=300)
btn_pesquisar= Button(root,text='buscar',font=('Arial', 17),bg='SkyBlue1')
btn_pesquisar.place(x=585,y=358)
buscare = Entry(root,font=('Arial',18),bd=3)
buscare.place(x=300,y=365,width=280,height=30)

root.mainloop()