from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

#1- conectando ao banco de dados sqlite3
banco = sqlite3.connect('petshopp.db')
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS agenda2 (id integer primary key autoincrement , nome text, dataa text, horario text , obs text)")
banco.commit()

#2 - criação da janela como um top level , para que fique estatica e focada
root = Toplevel()
root.geometry('700x500+0+0')
root.title('consulta')
root.resizable(False,False)
root.focus_force()
root.grab_set()

#2- criação da treeview onde terá 3 colunas , id, data,e hora
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

#2- setando a scrollbar da treeview
barrarolagem = ttk.Scrollbar( frame1,orient='vertical',
command=tabela.yview)
barrarolagem.pack( side = 'right', fill='y')
tabela.configure(yscrollcommand = barrarolagem.set)


#1- esta função conecta a tabela no banco de dados e joga na treeview os respectivos dados para manter sempre atualizada
def atualizartabela():
    cursor.execute('SELECT * FROM  agenda2')
    id = cursor.fetchall()
    num=0
    tabela.delete(*tabela.get_children())
    for x in range(len(id)):
        tabela.insert("","end",values=(id[num][0],id[num][2],id[num][3]))
        num +=1
        
atualizartabela()

#1- esta função inseri valores no banco de dados, junto com o botão de cadastro
def inserir(nome,data,horario,obs):
    if nome == '' or data == '':
        messagebox.showerror(title='mensagem de erro',message='preencha todos os campos')
    else:
        cursor.execute("INSERT INTO agenda2 (nome, dataa, horario, obs) VALUES('{}','{}','{}','{}')".format(nome,data,horario,obs))
        banco.commit()
        atualizartabela()
        limpar()

#1- esta função busca no banco de dados algo semelhante ao digitado no entry e inseri na treeview , como se fosse um filtro de informações
def buscar():
    sql = 'SELECT * FROM agenda2 WHERE dataa LIKE "%{}%"'.format(buscare.get())
    lista = cursor.execute(sql)
    tabela.delete(*tabela.get_children())
    for linhas in lista:
        tabela.insert('', 'end',values=(linhas[0],linhas[2],linhas[3]))   
    buscare.delete(0,END)

#2- a função de limpeza dos Entrys     
def limpar():
    nomee.delete(0,END)
    datae.delete(0,END)
    obse.delete(1.0,END)
    hora.delete(0,END)
    chave.delete(0,END)

#2- função de calcular o id retirado da treeview
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
    
#1- depois de coletado o id, usamos ele para conectar a tabela no banco e coletar os dados do respectivo id, e então inserimos estes dados nas suas respectivas Entrys para facilitar a atualização de dados pelo usuario
    cursor.execute('SELECT * FROM agenda2 WHERE id = {}'.format(a))
    valor = cursor.fetchall()
    nomee.insert(0,str(valor[0][1]))
    datae.insert(0,str(valor[0][2]))
    hora.insert(0,str(valor[0][3]))
    obse.insert(1.0,str(valor[0][4]))
    chave.insert(0,str(valor[0][0]))
    
#1- aqui é onde atualizamos os dados que foram inseridos nos Entrys     
def atualizar(nome,data,horario,obs,chave):
    cursor.execute("UPDATE agenda2 SET nome = '{}' ,dataa = '{}' , horario = '{}' , obs = '{}' WHERE id = {}".format(nome,data,horario,obs,chave))
    banco.commit()
    limpar()
    messagebox.showinfo(title='mensagem de informação',message='consulta atualizada com sucesso !!!')
    
    atualizartabela()
    

#2- aqui onde se encontão a maioria dos widgets , foram feitos com um Label e em sua frente um Entry, foram usados um foreground de cor royal blue, e steelblue, a fonte usada é a arial e o weight é o bold para não ficar muito grossa as linhas
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


#2- aqui é onde ficam todos os buttons que aparecem em baixo na tela, eles chamam as funções sitadas
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