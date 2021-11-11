from tkinter import *
import os

#2- comando para listar os arquivos dentro do diretorios
pasta = os.path.dirname(__file__)

#2- funções para chamada das janelas que estão no diretorio
def consulta():
    exec(open(pasta+"\\consulta.py").read(), {'c':pasta})
    
def stoke():
    exec(open(pasta+"\\stoke.py").read(), {'c':pasta})
    
def venda():
    exec(open(pasta+"\\vender.py").read(), {'c':pasta})

#criação da janela principal e inicial
root1 = Tk()
root1.geometry('700x500+0+0')
root1.title('tela principal')

#2- titulos e botoes com o nome de cada tela que vai ser chamada
Label(root1,text='petshopp nova era',fg='royal blue',font='arial 40 bold').place(x=135,y=15)
btn_stok= Button(root1,text='STOKE',bg='white smoke',font='arial 20 bold',width='34',command=stoke).place(x=50,y=90)
btn_consulta= Button(root1,text='CONSULTA',bg='white smoke',font='arial 20 bold',width='34',command=consulta).place(x=50,y=160)
btn_vender= Button(root1,text='VENDER',bg='white smoke',font='arial 20 bold',width='34',command=venda).place(x=50,y=230)
btn_sair= Button(root1,text='sair',bg='coral',font='arial 18 bold',width='25',command=root1.destroy).place(x=150,y=300)

root1.mainloop()