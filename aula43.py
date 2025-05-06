import tkinter as tk
from tkinter import messagebox as msg

janela = None

def interface():

    quadro = tk.Frame(janela)
    quadro.pack(padx=20, pady=20, fill="both", expand=True)

    label_nome = tk.Label(quadro, text="Nome:")
    label_nome.pack(anchor='w')
    entry_celular = tk.Entry(quadro, width=50)
    entry_celular.pack()

    label_nome = tk.Label(quadro, text="Nome:")
    label_nome.pack(anchor='w')
    entry_celular = tk.Entry(quadro, width=50)
    entry_celular.pack()

    label_nome = tk.Label(quadro, text="Nome:")
    label_nome.pack(anchor='w')
    entry_celular = tk.Entry(quadro, width=50)
    entry_celular.pack()

def main():
    global janela
    janela = tk.Tk()
    janela.title("Agenda de contatos")
    interface()
    janela.mainloop()

main()