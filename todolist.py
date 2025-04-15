import tkinter as tk


#funções

def add_task():
    tarefa = entry_tarefa.get()
    if tarefa:  # Verifica se o campo não está vazio
        listbox_tarefas.insert(tk.END, tarefa)  # Adiciona à Listbox
        entry_tarefa.delete(0, tk.END)  # Limpa o campo de entrada

def remove_task():
    try:
        selecionado = listbox_tarefas.curselection()[0]  # Obtém o índice da seleção
        listbox_tarefas.delete(selecionado)  # Remove a tarefa selecionada
    except IndexError:
        pass  # Evita erro se nada estiver selecionado

# Versão do App
App_version = "1.0."

# Configurações da janela principal
janela = tk.Tk()
janela.title("To Do List--VERSION: 1.0" + App_version)
janela.geometry("500x500")
janela.configure(bg="black", borderwidth=0)

# Frame principal com padding
frame = tk.Frame(janela, padx=30, pady= 15, bg = "black", highlightbackground="black", highlightthickness=0)
frame.grid(column=0, row=0)  # Usando grid para posicionar o frame
frame.configure(bg="black", borderwidth=0)

# Labels e widgets dentro do frame, agora usando grid
#Label de titulo
tk.Label(frame, text="TO-DO LIST", font=("Arial", 16), bg="black", fg="white").grid(row=0, column=0, columnspan=2, pady=10)

#Label de adicionar tarefa
tk.Label(frame, text="Adicionar tarefa:", bg="black", fg="white").grid(row=1, column=0, pady=5, columnspan=2)

#Entrada de tarefa
entry_tarefa = tk.Entry(frame, width=40)
entry_tarefa.grid(row=2, column=0, columnspan=2, pady=5, sticky="ew")


#Label de listas de tarefas(label, listbox, etc)
tk.Label(frame, text="TAREFAS", bg="black", fg="white").grid(row=4, column=0, columnspan=2, pady=10)
listbox_tarefas = tk.Listbox(frame, width=50, height=10, bg="white", fg="black")
listbox_tarefas.grid(row=5, column=0, columnspan=2, pady=5)

# Scrollbar para a Listbox(codeium que fez)
scrollbar = tk.Scrollbar(frame, orient="vertical", command=listbox_tarefas.yview)
scrollbar.grid(row=5, column=2, sticky="nse")


# Botão para adicionar a tarefa
botao_adicionar = tk.Button(frame, text="Adicionar", command= add_task)
botao_adicionar.grid(row=3, column=0, pady=10, padx=5)

#Botao para excluir tarefa
botao_excluir = tk.Button(frame, text="Excluir tarefa", command= remove_task)
botao_excluir.grid(row=3, column=1, pady=10, padx=5)

# Faz a janela aparecer e permanecer aberta
janela.mainloop()
