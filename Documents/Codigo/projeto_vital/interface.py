import tkinter as tk
from tkinter import messagebox
from collections import Counter


class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def resumo(self):
        if not self.itens:
            return "Você não realizou um pedido."

        contagem = Counter(self.itens)
        texto = "===== Resumo do Pedido =====\n"
        for item, qtd in contagem.items():
            texto += f"- {qtd}x {item}\n"

        return texto


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
        self.janela_generica("Entradas", [
            "Pizza branca",
            "Palitos de queijo",
            "Bolinha de queijo"
        ])

    def janela_massas(self):
        self.janela_generica("Massas", [
            "Pizza",
            "Lasanha",
            "Macarrão"
        ])

    def janela_bebidas(self):
        self.janela_generica("Bebidas", [
            "Soda limão",
            "Soda morango",
            "Soda maracujá",
            "Refrigerante lata",
            "Água mineral",
            "Água com gás"
        ])

    # --------------------------
    # FUNÇÕES PRINCIPAIS
    # --------------------------

    def adicionar_item(self, item):
        self.pedido.adicionar(item)
        messagebox.showinfo("Item adicionado", f"{item} foi adicionado ao pedido!")

    def finalizar(self):
        texto = self.pedido.resumo()
        messagebox.showinfo("Resumo do Pedido", texto)


# --------------------------
# INICIAR A APLICAÇÃO
# --------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceCardapio(root)
    root.mainloop()
