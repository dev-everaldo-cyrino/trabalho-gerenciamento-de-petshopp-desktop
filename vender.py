from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
#from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import A7
import os

#1- conectando ao banco de dados sqlite3
banco = sqlite3.connect('petshopp.db')
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS agenda3 (id integer primary key autoincrement , nome text, stoke integer, valor integer , fone text)")
banco.commit()

#2- aqui é onde começa a construção da notinha  de compra
f = open('total.txt','w')
arq = ['        petshopp nova era', 'Rua Natanael Barbosa Alvez - CENTRO','AREIAL - PB - FONE (83) 98888-8888','------------------------------------']
with open('total.txt','w')as arquivo:
    for x in arq:
        arquivo.write(str(x)+'\n')
f.close()


#2 - criação da janela como um top level , para que fique estatica e focada
root = Toplevel()
root.geometry('700x500+0+0')
root.title('tela de vendas')
root.resizable(False,False)
root.focus_force()
root.grab_set()

#2- criação da treeview onde terá 3 colunas , id,produtos,e stoke
frame1 = Frame(root,borderwidth=2,relief='sunken',bg='snow')
frame1.place(x=300,y=70,width=380,height=285)
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

#2-setando a scrollbar da treeview
barrarolagem = ttk.Scrollbar( frame1,orient='vertical',
command=tabela.yview)
barrarolagem.pack( side = 'right', fill='y')
tabela.configure(yscrollcommand = barrarolagem.set)


#2- criação da treeview que armazena os itens comprados onde terá 5 colunas , id, produtos, stoke, quantidade, preço e subtotal
frame2 = Frame(root,borderwidth=2,relief='sunken',bg='snow')
frame2.place(x=0,y=70,width=300,height=150)
tabela1 = ttk.Treeview( frame2,
columns = (1,2,3,4,5),
height = 15,
show = 'headings')
tabela1.pack( side = 'left')
tabela1.heading(1, text='id')
tabela1.heading(2, text='produto')
tabela1.heading(3, text='quant')
tabela1.heading(4, text='preço')
tabela1.heading(5, text='total')
tabela1.column(1, width = 40)
tabela1.column(2, width = 110)
tabela1.column(3, width = 40)
tabela1.column(4, width = 40)
tabela1.column(5, width = 50)

#2-setando a scrollbar da treeview
barrarolagem = ttk.Scrollbar( frame2,orient='vertical',
command=tabela1.yview)
barrarolagem.pack( side = 'right', fill='y')
tabela1.configure(yscrollcommand = barrarolagem.set)


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
    produtoe.delete(0,END)
    stokee.delete(0,END)
    precoe.delete(0,END)
    chave.delete(0,END)
    quante.delete(0,END)

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
    produtoe.insert(0,str(valor[0][1]))
    stokee.insert(0,str(valor[0][2]))
    precoe.insert(0,str(valor[0][3]))
    chave.insert(0,str(valor[0][0]))

#2- esta função recebe valores dos Entrys e os processa para colocar na treeview da notinha de compra    
def add (id,nome,quant,valor,stoke):
    subtotal = float(quant) * float(valor)
    total = totale.get()
    if total == '':
        totale.insert(0,str('0'))
        total = totale.get()
    total = float(total)
    total += subtotal
    totale.delete(0,END)
    totale.insert(0,str(total))
    tabela1.insert("","end",values=(id,nome,quant,valor,subtotal))
    Label(root,text='${}'.format(total),fg='royal blue',font='Arial 18 bold').place(x=80,y=225)
    limpar()
    f=open('total.txt', 'a')
    f.write('   {}: \n'.format(nome))
    f.write('     {}     {} =     {:.2f}\n'.format(quant,valor,subtotal))
    f.close()
    
#1- aqui ele desconta do stoke a quantidade comprada
    novostoke = float(stoke) - float(quant)
    cursor.execute("UPDATE agenda3 SET stoke = {}  WHERE id = {}".format(novostoke,id))
    banco.commit()
    buscar()
     
    
    
#2- esta função processa o total das compras e o valor pago para saber se ta tudo ok
def pagar(pago):
    troco = 0
    a = totale.get()
    a = float(a)
    pago = float(pago)
    if a <= pago :
        troco = pago - a
        Label(root,text='${}'.format(troco),fg='royal blue',font='Arial 18 bold').place(x=80,y=465)
    else:
        messagebox.showerror(title='mensagem de erro',message='valor abaixo do total !!!')
        
#2-esta função processa se tudo deu certo e então finaliza a compra gerando um documento com todos os itens comprados quantidade e dinheiro total e pago alem do troco
def finalizar(pago,total):
    troco = 0
    total = float(total)
    pago = float(pago)
    troco = pago - total
    f = open('total.txt','a')
    arq=['------------------------------------','total    :                     {} '.format(total),'dinheiro :                     {}'.format(pago),'------------------------------------','troco    :                     {}'.format(troco),'-------------------------------------','            obrigado','     V O L T E     S E M P R E']
    with open('total.txt','a')as arquivo:
          for x in arq:
            arquivo.write(str(x)+'\n')
    arq1 = ['','','','        petshopp nova era', 'Rua Natanael Barbosa Alvez - CENTRO','AREIAL - PB - FONE (83) 98888-8888','------------------------------------']
    with open('total.txt','a')as arquivo:
        for x in arq1:
            arquivo.write(str(x)+'\n')
    f.close()
    Label(root,text='$0.00',fg='royal blue',font='Arial 18 bold').place(x=80,y=465)
    Label(root,text='$0.00',fg='royal blue',font='Arial 18 bold').place(x=80,y=225)
    totale.insert(0,str('0'))
    
      
#2- aqui ficam os widgets superiores onde acontece a compra
Label(root,text='tela de vendas',fg='royal blue',font='Arial 40 bold').place(x=135,y=0)
chave = Entry(root,width='0',font=('Arial',15))
chave.place(x=2000,y=0)
totale = Entry(root,width='0',font=('Arial',15))
totale.place(x=1900,y=0)
Label(root,text='produto:',fg='royal blue',font='Arial 15 bold').place(x=5,y=285)
produtoe = Entry(root,bd=3,font='Arial 15')
produtoe.place(x=110,y=287,width=160)
Label(root,text='stoke :',fg='royal blue',font='Arial 18 bold').place(x=8,y=315)
stokee = Entry(root,bd=3,font='Arial 15')
stokee.place(x=110,y=317,width=73)
Label(root,text='valor  :',fg='royal blue',font='Arial 18 bold').place(x=5,y=345)
precoe = Entry(root,bd=3,font='Arial 15')
precoe.place(x=110,y=347,width=73)
Label(root,text='quantidade:',fg='royal blue',font='Arial 18 bold').place(x=5,y=375)
quante = Entry(root,bd=3,font='Arial 15')
quante.place(x=148,y=377,width=60)

#2- aqui ficam os widgets inferiores onde fica os botoes de pagar e finalizar alem de busca e inseir do banco de dados 
btn_adicionar = Button(root,bg='royal blue',font='Arial 18 bold',text='ADD',command=lambda:add(chave.get(),produtoe.get(),quante.get(),precoe.get(),stokee.get()))
btn_adicionar.place(x=220,y=345,width=70,height=60)
Label(root,text='total :',fg='royal blue',font='Arial 18 bold').place(x=5,y=225)
Label(root,text='pagar :',fg='royal blue',font='Arial 18 bold').place(x=5,y=425)
pagare = Entry(root,bd=3,font='Arial 18')
pagare.place(x=90,y=430,width=73)
Label(root,text='troco :',fg='royal blue',font='Arial 18 bold').place(x=5,y=465)
btn_pagar= Button(root,text='pagar',bg='dodger blue',font='arial 16 bold',width='5',height='2',command=lambda:pagar(pagare.get()))
btn_pagar.place(x=180,y=419)
btn_finalizar= Button(root,text='finalizar',bg='coral',font='arial 16 bold',width='7',height='2',command=lambda:finalizar(pagare.get(),totale.get()))
btn_finalizar.place(x=260,y=419)
btn_selecionar = Button(root,text='selecionar',font=('Arial', 17),bg='LightSteelBlue2',command=selecionar)
btn_selecionar.place(x=375,y=420,width=300)
btn_pesquisar= Button(root,text='buscar',font=('Arial', 17),bg='SkyBlue1',command=buscar)
btn_pesquisar.place(x=585,y=358)
buscare = Entry(root,font=('Arial',18),bd=3)
buscare.place(x=300,y=365,width=280,height=30)


root.mainloop()