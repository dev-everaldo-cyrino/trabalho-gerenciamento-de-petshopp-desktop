from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

#1- conectando o banco e a tabela de dados
banco = sqlite3.connect('petshopp.db')
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS agenda3 (id integer primary key autoincrement , nome text, stoke integer, valor integer , fone text)")
banco.commit()

#2 - criação da janela como um top level , para que fique estatica e focada
root = Toplevel()
root.geometry('700x500+0+0')
root.title('consulta')
root.resizable(False,False)
root.focus_force()
root.grab_set()


#2- criação da treeview onde terá 3 colunas , id,produtos,e stoke
frame1 = Frame(root,borderwidth=2,relief='sunken',bg='snow')
frame1.place(x=300,y=70,width=380,height=280)
tabela = ttk.Treeview( frame1,
columns = (1,2,3),
height = 15,
show = 'headings')
tabela.pack( side = 'left')
tabela.heading(1, text='id')
tabela.heading(2, text='produto')
tabela.heading(3, text='stoke')
tabela.column(1, width= 50)
tabela.column(2, width = 180 )
tabela.column(3, width = 135 )

#2- fazendo o scrollbar da treeview
barrarolagem = ttk.Scrollbar( frame1,orient='vertical',
command=tabela.yview)
barrarolagem.pack( side = 'right', fill='y')
tabela.configure(yscrollcommand = barrarolagem.set)


#1- esta função conecta a tabela no banco de dados e joga na treeview os respectivos dados para manter sempre atualizada
def atualizartabela():
    cursor.execute('SELECT * FROM  agenda3')
    id = cursor.fetchall()
    num=0
    tabela.delete(*tabela.get_children())
    for x in range(len(id)):
        tabela.insert("","end",values=(id[num][0],id[num][1],id[num][2]))
        num +=1
        
atualizartabela()

#1- esta função inseri valores no banco de dados, junto com o botão de cadastro
def inserir(nome,stoke,valor,fone):
    if nome == '' or stoke == '' or valor == '':
        messagebox.showerror(title='mensagem de erro',message='preencha todos os campos')
    else:
        cursor.execute("INSERT INTO agenda3 (nome, stoke, valor, fone) VALUES('{}',{},{},'{}')".format(nome,stoke,valor,fone))
        banco.commit()
        atualizartabela()
        limpar()
        
#1- esta função busca no banco de dados algo semelhante ao digitado no entry e inseri na treeview , como se fosse um filtro de informações 
def buscar():
    sql = 'SELECT * FROM agenda3 WHERE nome LIKE "%{}%"'.format(buscare.get())
    lista = cursor.execute(sql)
    tabela.delete(*tabela.get_children())
    for linhas in lista:
        tabela.insert('', 'end',values=(linhas[0],linhas[1],linhas[2]))   
    buscare.delete(0,END)
    
#2- a função de limpeza dos Entrys    
def limpar():
    nomee.delete(0,END)
    stokee.delete(0,END)
    valore.delete(0,END)
    fonee.delete(0,END)
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
    cursor.execute('SELECT * FROM agenda3 WHERE id = {}'.format(a))
    valor = cursor.fetchall()
    nomee.insert(0,str(valor[0][1]))
    stokee.insert(0,str(valor[0][2]))
    valore.insert(0,str(valor[0][3]))
    fonee.insert(0,str(valor[0][4]))
    chave.insert(0,str(valor[0][0])) 
    
#1- aqui é onde atualizamos os dados que foram inseridos nos Entrys    
def atualizar(nome,stoke,valor,fone,chave):
    cursor.execute("UPDATE agenda3 SET nome = '{}' ,stoke = {} , valor = {} , fone = '{}' WHERE id = {}".format(nome,stoke,valor,fone,chave))
    banco.commit()
    limpar()
    messagebox.showinfo(title='mensagem de informação',message='consulta atualizada com sucesso !!!')
    
    atualizartabela()


#2- aqui onde se encontão a maioria dos widgets , foram feitos com um Label e em sua frente um Entry, foram usados um foreground de cor royal blue, e steelblue, a fonte usada é a arial e o weight é o bold para não ficar muito grossa as linhas
Label(root,text='tela de stoke',fg='royal blue',font='Arial 40 bold').place(x=135,y=0)
chave = Entry(root,width='0',font=('Arial',15))
chave.place(x=2000,y=0)

Label(root,text='produto : ',fg='steelblue',font='arial 16 bold').place(x=5,y=70)
nomee = Entry(root,width='17',font=('Arial',15))
nomee.place(x=105,y=75)


Label(root,text='stoke    :',fg='steelblue',font='arial 16 bold').place(x=5,y=120)
stokee = Entry(root,width='5',font=('Arial',15))
stokee.place(x=105,y=125)

Label(root,text='valor    :',fg='steelblue',font='arial 16 bold').place(x=5,y=170)
valore = Entry(root,width='5',font=('Arial',15))
valore.place(x=105,y=175)

Label(root,text='fone    :',fg='steelblue',font='arial 15 bold').place(x=5,y=220)
fonee = Entry(root,width='17',font=('Arial',15))
fonee.place(x=105,y=225)

#2- aqui é onde ficam todos os buttons que aparecem em baixo na tela, eles chamam as funções sitadas
btn_limpar= Button(root,text='limpar',bg='salmon',font='arial 20 bold',height='3',command=limpar)
btn_limpar.place(x=170,y=365)
btn_cadastrar= Button(root,text='cadastrar',bg='dodger blue',font='arial 20 bold',width='8',command=lambda:inserir(nomee.get(),stokee.get(),valore.get(),fonee.get()))
btn_cadastrar.place(x=10,y=365)
btn_atualizar= Button(root,text='atualizar',bg='royal blue',font='arial 20 bold',width='8',command=lambda:atualizar(nomee.get(),stokee.get(),valore.get(),fonee.get(),chave.get()))
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