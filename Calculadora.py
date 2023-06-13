from tkinter import *
from tkinter import ttk

cor1 = "#feffff" # Branco
cor2 = "#38576b" # Azul escuro
cor3 = "#ECEFF1" # Cinza claro
cor4 = '#FFAB40' # Laranja
cor5 = '#ff6854' # Vermelho
cor6 = "#aba6a6" # black

janela = Tk()
janela.title('Calculadora')
janela.geometry('256x310')
janela.configure(bg=cor1)
janela.config(bg=cor6)

# Criando Frames
frame_tela = Frame(janela, width=256, height=50, bg=cor2)
frame_tela.grid(row=0, column=0)

frame_quadro = Frame(janela, width=256, height=268)
frame_quadro.grid(row=1, column=0)

todos_valores = ''

# Criando Funcao
def entrar_valores(valor):
    global todos_valores
    todos_valores = todos_valores + str(valor)

    valor_texto.set(todos_valores)

#Função calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(resultado)

#Função Limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

#Criando Label
valor_texto = StringVar()
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font='Ivy 18', bg=cor2, fg=cor1)
app_label.place(x=0, y=0)


# Criando Botoes
b_1 = Button(frame_quadro, command=limpar_tela, text="C", width=12, height=2, bg=cor5, fg=cor1, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_quadro, command=lambda: entrar_valores('%'), text="%", width=6, height=2, bg=cor6, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=0)
b_3 = Button(frame_quadro, command=lambda: entrar_valores('/'), text="/", width=6, height=2, bg=cor4, fg=cor1, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_3.place(x=186, y=0)

b_4 = Button(frame_quadro, command=lambda: entrar_valores('7'), text="7", width=6, height=2, bg=cor3, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_quadro, command=lambda: entrar_valores('8'), text="8", width=6, height=2, bg=cor3, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_quadro, command=lambda: entrar_valores('9'), text="9", width=6, height=2, bg=cor3, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=52)
b_7 = Button(frame_quadro, command=lambda: entrar_valores('*'), text="*", width=6, height=2, bg=cor4, fg=cor1, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_7.place(x=186, y=52)

b_8 = Button(frame_quadro, command=lambda: entrar_valores('4'), text="4", width=6, height=2, bg=cor3, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_quadro, command=lambda: entrar_valores('5'), text="5", width=6, height=2, bg=cor3, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_quadro, command=lambda: entrar_valores('6'), text="6", width=6, height=2, bg=cor3, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_10.place(x=120, y=104)
b_11 = Button(frame_quadro, command=lambda: entrar_valores('-'), text="-", width=6, height=2, bg=cor4, fg=cor1, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_11.place(x=186, y=104)

b_12 = Button(frame_quadro, command=lambda: entrar_valores('1'), text="1", width=6, height=2, bg=cor3, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_quadro, command=lambda: entrar_valores('2'), text="2", width=6, height=2, bg=cor3, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(frame_quadro, command=lambda: entrar_valores('3'), text="3", width=6, height=2, bg=cor3, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_14.place(x=120, y=156)
b_15 = Button(frame_quadro, command=lambda: entrar_valores('+'), text="+", width=6, height=2, bg=cor4, fg=cor1, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_15.place(x=186, y=156)

b_16 = Button(frame_quadro, command=lambda: entrar_valores('0'), text="0", width=12, height=2, bg=cor3, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_quadro, command=lambda: entrar_valores('.'), text=".", width=6, height=2, bg=cor3, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_17.place(x=120, y=208)
b_18 = Button(frame_quadro, command=calcular, text="=", width=6, height=2, bg=cor4, fg=cor1, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_18.place(x=186, y=208)

janela.mainloop()
