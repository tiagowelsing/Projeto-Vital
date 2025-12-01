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
