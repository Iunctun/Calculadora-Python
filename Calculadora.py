from tkinter import * 
from tkinter import ttk

#cores
cor1 = "#000000"
cor2 = "#0b1da3"
cor3 = "#999999"
cor4 = "#ffffff"
cor5 = "#3696d6"
cor6 = "#cfcfcf"



#criação da janela
janela = Tk()
janela.title("Calculadora") #titulo da janela
janela.geometry("349x455") #tamanho da janela em si, primeiro numero largura, segundo numero altura
janela.config(bg=cor3)



#frames da janela
frame_tela = Frame(janela, width=349, height=100, bg=cor1)#frame do display
frame_tela.grid(row=0, column=0)

frame_quadro = Frame(janela, width=349, height=355)#frame do quadro
frame_quadro.grid(row=1, column=0)


#variavel todos valores
todos_valores = ""

#variavel que entra para o label
valor_texto = StringVar()

#expressões para a calculadora

# Define a função chamada 'calcular'
def entrar_valores(event):
    

    global todos_valores #global esta usando a variavel de fora da função
    
    todos_valores = todos_valores + (str(event)) 

   
    #passar o valor para a tela da calculadora
    valor_texto.set(todos_valores)

#função para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))


#função para limpar tela
def limpar_tela():
   global todos_valores
   todos_valores = ""
   valor_texto.set("")


#"todos valores" será apresentado a "valor_texto", que irá ser apresentado no label "app_label = Label(frame_tela, textvariable=valor_texto" 

#label
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=3,padx=7,relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 27"), bg=cor1, fg=cor4)#texto do label, tamanho do label, padding, estilo, deixar mais no canto inferior direito, também deixa tudo na direita,fonte do label
app_label.place(x=0,y=0)




#botoes
#primeira linha da botões
b_1 = Button(frame_quadro, command = limpar_tela ,text="C", width=16, height=3, bg=cor6, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)#width = largura, height=altura, overrelief=estilo do botão ao passar o mouse por cima
b_1.place(x=0, y=0)
b_2 = Button(frame_quadro, command = lambda: entrar_valores("%"), text="%", width=8, height=3, bg=cor6, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_2.place(x=170, y=0)
b_3 = Button(frame_quadro, command = lambda: entrar_valores("/"), text="/", width=8, height=3, bg=cor2, fg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_3.place(x=260, y=0)
#segunda linha de botões
b_4 = Button(frame_quadro, command = lambda: entrar_valores("7"), text="7", width=8, height=3, bg=cor6, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=71)
b_5 = Button(frame_quadro, command = lambda: entrar_valores("8"), text="8", width=8, height=3, bg=cor6, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_5.place(x=84, y=71)
b_6 = Button(frame_quadro, command = lambda: entrar_valores("9"), text="9", width=8, height=3, bg=cor6, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_6.place(x=170, y=71)
b_7 = Button(frame_quadro, command = lambda: entrar_valores("*"), text="*", width=8, height=3, bg=cor2, fg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_7.place(x=260, y=71)
#terceira linha de botões
b_8 = Button(frame_quadro, command = lambda: entrar_valores("4"), text="4", width=8, height=3, bg=cor6, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=142)
b_9 = Button(frame_quadro, command = lambda: entrar_valores("5"), text="5", width=8, height=3, bg=cor6, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_9.place(x=84, y=142)
b_10 = Button(frame_quadro, command = lambda: entrar_valores("6"), text="6", width=8, height=3, bg=cor6, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_10.place(x=170, y=142)
b_11 = Button(frame_quadro, command = lambda: entrar_valores("-"), text="-", width=8, height=3, bg=cor2, fg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_11.place(x=260, y=142)
#quarta linha de botões
b_12 = Button(frame_quadro, command = lambda: entrar_valores("1"), text="1", width=8, height=3, bg=cor6, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=213)
b_13 = Button(frame_quadro, command = lambda: entrar_valores("2"), text="2", width=8, height=3, bg=cor6, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_13.place(x=84, y=213)
b_14 = Button(frame_quadro, command = lambda: entrar_valores("3"), text="3", width=8, height=3, bg=cor6, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_14.place(x=170, y=213)
b_15 = Button(frame_quadro, command = lambda: entrar_valores("+"), text="+", width=8, height=3, bg=cor2, fg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_15.place(x=260, y=213)
#quinta linha de botões
b_16 = Button(frame_quadro, command = lambda: entrar_valores("0"), text="0", width=16, height=3, bg=cor6, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)#width = largura, height=altura, overrelief=estilo do botão ao passar o mouse por cima
b_16.place(x=0, y=284)
b_17 = Button(frame_quadro, command = lambda: entrar_valores("."), text=".", width=8, height=3, bg=cor6, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_17.place(x=170, y=284)
b_18 = Button(frame_quadro, command = calcular, text="=", width=8, height=3, bg=cor2, fg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_18.place(x=260, y=284)




janela.mainloop()