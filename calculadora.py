#Calculadora como portofolio
#Calculadora com interface
import tkinter as tk

#Configurações da janela
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x300")
janela.config(bg="black")


#Frames(os quadradinhos man)

frame = tk.Frame(janela, height=50, width=300, padx= 10, pady= 10, bg= "black")
frame.grid(row=0, column=0)

#Corpo da calculado(botoes, etc. basicamente posicionamento)

frame_corpo = tk.Frame(janela, height=250, width=300, padx= 10, pady= 10)
frame_corpo.grid(row=1, column=0)

#botões
botao_1 = tk.Button(frame_corpo, text="C", width=7, height=3)
botao_1.place(x=0, y=0)

#mantem a janela aberta
janela.mainloop()