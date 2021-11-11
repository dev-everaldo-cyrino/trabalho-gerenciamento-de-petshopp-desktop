from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3


banco = sqlite3.connect('petshopp.db')
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS agenda2 (id integer primary key autoincrement , nome text, dataa text, horario text , obs text)")
banco.commit()


root = Tk()
root.geometry('700x500+0+0')
root.title('consulta')

frame1 = Frame(root,borderwidth=2,relief='sunken',bg='snow')
frame1.place(x=300,y=75,width=380,height=280)
tabela = ttk.Treeview( frame1,
columns = (1,2,3),
height = 15,
show = 'headings')
tabela.pack( side = 'left')
tabela.heading(1, text='id')
tabela.heading(2, text='data')
tabela.heading(3, text='horario')
tabela.column(1, width= 40)
tabela.column(2, width = 155 )
tabela.column(3, width = 155 )

barrarolagem = ttk.Scrollbar( frame1,orient='vertical',
command=tabela.yview)
barrarolagem.pack( side = 'right', fill='y')
tabela.configure(yscrollcommand = barrarolagem.set)



def atualizartabela():
    cursor.execute('SELECT * FROM  agenda2')
    id = cursor.fetchall()
    num=0
    tabela.delete(*tabela.get_children())
    for x in range(len(id)):
        tabela.insert("","end",values=(id[num][0],id[num][2],id[num][3]))
        num +=1
        
atualizartabela()


def inserir(nome,data,horario,obs):
    if nome == '' or data == '':
        messagebox.showerror(title='mensagem de erro',message='preencha todos os campos')
    else:
        cursor.execute("INSERT INTO agenda2 (nome, dataa, horario, obs) VALUES('{}','{}','{}','{}')".format(nome,data,horario,obs))
        banco.commit()
        atualizartabela()
        limpar()

def buscar():
    sql = 'SELECT * FROM agenda2 WHERE dataa LIKE "%{}%"'.format(buscare.get())
    lista = cursor.execute(sql)
    tabela.delete(*tabela.get_children())
    for linhas in lista:
        tabela.insert('', 'end',values=(linhas[0],linhas[2],linhas[3]))   
    buscare.delete(0,END)
        
def limpar():
    nomee.delete(0,END)
    datae.delete(0,END)
    obse.delete(1.0,END)
    hora.delete(0,END)
    chave.delete(0,END)

def selecionar():
    #sql = "SELECT * FROM agenda1 WHERE nome=?"
    nomex = tabela.selection()[0]
    
    idd = str(tabela.item(nomex,"values"))
    
    a = [idd]
    
    if a[0][4] == ',':
        a = a[0][2]
    elif a[0][5] == ',':
        a = a[0][2] + a[0][3]
    elif a[0][6] == ',':
        a = a[0][2] + a[0][3] + a[0][4]
    elif a[0][7] == ',':
        a = a[0][2] + a[0][3] + a[0][4] + a[0][5]
    
    limpar()
    cursor.execute('SELECT * FROM agenda2 WHERE id = {}'.format(a))
    valor = cursor.fetchall()
    nomee.insert(0,str(valor[0][1]))
    datae.insert(0,str(valor[0][2]))
    hora.insert(0,str(valor[0][3]))
    obse.insert(1.0,str(valor[0][4]))
    chave.insert(0,str(valor[0][0]))
    
    
    
    
def atualizar(nome,data,horario,obs,chave):
    cursor.execute("UPDATE agenda2 SET nome = '{}' ,dataa = '{}' , horario = '{}' , obs = '{}' WHERE id = {}".format(nome,data,horario,obs,chave))
    banco.commit()
    limpar()
    messagebox.showinfo(title='mensagem de informação',message='consulta atualizada com sucesso !!!')
    
    atualizartabela()
    

Label(root,text='tela de consulta',fg='royal blue',font='Arial 40 bold').place(x=135,y=0)

chave = Entry(root,width=0)
chave.place(x=2000,y=0)
Label(root,text='nome : ',fg='steelblue',font='arial 18 bold').place(x=15,y=50)
nomee = Entry(root,width='30')
nomee.place(x=100,y=60)


Label(root,text='data  :',fg='steelblue',font='arial 18 bold').place(x=15,y=100)
datae = Entry(root,width='30')
datae.place(x=100,y=110)


Label(root,text='horarios :',fg='steelblue',font='arial 18 bold').place(x=15,y=160)
hora = Entry(root)
hora.place(x=130,y=168)


Label(root,text='motivo :',fg='steelblue',font='arial 18 bold').place(x=15,y=205)
obse = Text(root,height='5',width='30')
obse.place(x=15,y=237)




btn_limpar= Button(root,text='limpar',bg='salmon',font='arial 20 bold',height='3',command=limpar)
btn_limpar.place(x=170,y=365)
btn_cadastrar= Button(root,text='cadastrar',bg='dodger blue',font='arial 20 bold',width='8',command=lambda:inserir(nomee.get(),datae.get(),hora.get(),obse.get('1.0',END)))
btn_cadastrar.place(x=10,y=365)
btn_atualizar= Button(root,text='atualizar',bg='royal blue',font='arial 20 bold',width='8',command=lambda:atualizar(nomee.get(),datae.get(),hora.get(),obse.get('1.0',END),chave.get()))
btn_atualizar.place(x=10,y=429)
btn_sair= Button(root,text='sair',bg='coral',font='arial 16 bold',width='5',height='2',command=root.destroy)
btn_sair.place(x=290,y=419)
        
        

        


btn_selecionar = Button(root,text='selecionar',font=('Arial', 17),bg='LightSteelBlue2',command=selecionar)
btn_selecionar.place(x=375,y=420,width=300)
btn_pesquisar= Button(root,text='buscar',font=('Arial', 17),bg='SkyBlue1',command=buscar)
btn_pesquisar.place(x=585,y=358)
buscare = Entry(root,font=('Arial',18),bd=3)
buscare.place(x=300,y=365,width=280,height=30)

root.mainloop()