from tkinter import *
from tkinter import messagebox

#cores---------------------
cor0 = "#444466"  # Preta
cor1 = "#feffff"  # branca
cor2 = "#004338"

#Janela
janela = Tk()
janela.geometry("530x205")
janela.configure(bg=cor1)
janela.title("Cores")

#Configuração da janela
tela = Label(janela, bg=cor0, width=40, height=10)
tela.grid(row=0, column=0)

frame_direito = Frame(janela, bg=cor1)
frame_direito.grid(row=0, column=1, padx=5)

frame_baixo = Frame(janela, bg=cor1)
frame_baixo.grid(row=1, column=0, columnspan=2, pady=15)

#Função scale
def escala(valor):
    r=s_red.get()
    g=s_green.get()
    b=s_blue.get()

    rgb = f'{r},{g},{b}'
    hexadecimal = "#%02x%02x%02x" % (r, g, b)

    #Alterando a cor do fundo da tela
    tela['bg'] = hexadecimal

    #Alterando a entry
    e_cor.delete(0,END)
    e_cor.insert(0,hexadecimal)

#Função clicar/deslizar
# Função clicar/deslizar
def onClick(entry_cor):
    # Informar se já foi copiado
    messagebox.showinfo('Cor', "A cor foi copiada")

    # Serve para criar botão copiar
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(entry_cor.get())
    clip.destroy()

#Configuração do Frame direito
l_red = Label(frame_direito, text='Red', bg=cor1, width=7, fg='red', anchor='nw', font=("Time New Roman", 12, "bold"))
l_red.grid(row=0, column=0)
s_red = Scale(frame_direito, command=escala, from_= 0, to=255, length=150, bg=cor1, fg='red', orient=HORIZONTAL)
s_red.grid(row=0, column=1)

l_green = Label(frame_direito, text='Green', bg=cor1, width=7, fg='green', anchor='nw', font=("Time New Roman", 12, "bold"))
l_green.grid(row=1, column=0)
s_green = Scale(frame_direito, command=escala, from_= 0, to=255, length=150, bg=cor1, fg='green', orient=HORIZONTAL)
s_green.grid(row=1, column=1)

l_blue = Label(frame_direito, text='Blue', bg=cor1, width=7, fg='blue', anchor='nw', font=("Time New Roman", 12, "bold"))
l_blue.grid(row=2, column=0)
s_blue = Scale(frame_direito, command=escala, from_= 0, to=255, length=150, bg=cor1, fg='blue', orient=HORIZONTAL)
s_blue.grid(row=2, column=1)

#Configurando a parte de baixo
l_rgb = Label(frame_baixo, text='CÓDIGO HEX :', bg=cor1, font=("Ivy", 10, "bold"))
l_rgb.grid(row=0, column=0, padx=5)

#Entry
e_cor = Entry(frame_baixo, width=12, font=("Ivy", 10, "bold"), justify=CENTER)
e_cor.grid(row=0, column=1, padx=5)

#Nome do seletor de cores
l_nome = Label(frame_baixo, text='Seletor de Cores', bg=cor1, font=("Ivy", 15, "bold"))
l_nome.grid(row=0, column=3, padx=40)

# Botão para copiar as cores
l_copiar = Button(frame_baixo, text='Copiar cor', bg=cor1, font=("Ivy", 8, "bold"), relief=RAISED, overrelief=RIDGE, command=lambda: onClick(e_cor))
l_copiar.grid(row=0, column=2, padx=5)

janela.mainloop()