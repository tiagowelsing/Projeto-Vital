import tkinter as tk
from tkinter import messagebox

from pedido import Pedido
from cardapio import Cardapio

class InterfaceCardapio:
    def __init__(self, root):
        self.root = root
        self.root.title("Del Polpollo - Cardápio")
        self.root.geometry("400x350")

        self.pedido = Pedido()

        self.titulo = tk.Label(root, text="Cardápio Del Polpollo", font=("Arial", 18))
        self.titulo.pack(pady=10)

        tk.Button(root, text="Entradas", width=20, command=self.janela_entradas).pack(pady=5)
        tk.Button(root, text="Massas", width=20, command=self.janela_massas).pack(pady=5)
        tk.Button(root, text="Bebidas", width=20, command=self.janela_bebidas).pack(pady=5)

        tk.Button(root, text="Finalizar Pedido", width=20, command=self.finalizar).pack(pady=20)

    # --------------------------
    # JANELAS DE CATEGORIAS
    # --------------------------

    def janela_generica(self, titulo, itens):
        janela = tk.Toplevel(self.root)
        janela.title(titulo)
        janela.geometry("300x300")

        tk.Label(janela, text=titulo, font=("Arial", 14)).pack(pady=10)

        for item in itens:
            tk.Button(janela, text=item, width=20,
                      command=lambda nome=item: self.adicionar_item(nome)).pack(pady=5)

    def janela_entradas(self):
        self.janela_generica("Entradas", Cardapio.ENTRADAS)

    def janela_massas(self):
        self.janela_generica("Massas", Cardapio.MASSAS)

    def janela_bebidas(self):
        self.janela_generica("Bebidas", Cardapio.BEBIDAS)

    # --------------------------
    # FUNÇÕES PRINCIPAIS
    # --------------------------

    def adicionar_item(self, item):
        self.pedido.adicionar(item)
        messagebox.showinfo("Item adicionado", f"{item} foi adicionado ao pedido!")

    def finalizar(self):
        texto = self.pedido.resumo()
        messagebox.showinfo("Resumo do Pedido", texto)
