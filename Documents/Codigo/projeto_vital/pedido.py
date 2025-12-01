import sys
from collections import Counter

class Pedido:
    def _init_(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def mostrar_pedido(self):
        print("\n===== Resumo do pedido =====")
        if not self.itens:
            print("Você não realizou um pedido.")
        else:
            contagem = Counter(self.itens)
            for item, qtd in contagem.items():
                print(f"- {qtd}x {item}")

        print("\nAté breve!")
        sys.exit()
