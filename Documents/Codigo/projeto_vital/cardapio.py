import sys
from collections import Counter 

class Pedido():
    def __init__(self):
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


class Cardapio():
    def __init__(self):
        self.pedido = Pedido()

    def mostrar_cardapio(self):    
        print("===== Cardápio Del Polpollo =====\n")
        print("1. Entradas")
        print("2. Massas")
        print("3. Bebidas")
        print("4. Sair")

#ENTRADAS

    def entradas(self):
     while True:
        print("\n--- Entradas ---")
        print("1. Pizza branca")
        print("2. Palitos de queijo")
        print("3. Bolinha de queijo")
        print("4. Voltar ao cardapio")
        print("5. Encerrar atendimento")

        op = input("Escolha sua entrada: ")

        if op == "1":
            self.pedido.adicionar("Pizza branca")
        elif op == "2":
            self.pedido.adicionar("Palitos de queijo")
        elif op == "3":
            self.pedido.adicionar("Bolinha de queijo")
        elif op == "4":
            break
        elif op == "5":
            self.pedido.mostrar_pedido()
        else:
            print("Opção inválida.")
            continue

        print("\nItem adicionado!")
        input("\nPressione Enter para continuar...")


#MASSAS

    def massas(self):
     while True:
        print("\n--- Massas ---")
        print("1. Pizza")
        print("2. Lasanha")
        print("3. Macarrão")
        print("4. Voltar ao cardápio")
        print("5. Encerrar atendimento")

        op = input("Escolha sua massa: ")

        if op == "1":
            self.pedido.adicionar("Pizza")
        elif op == "2":
            self.pedido.adicionar("Lasanha")
        elif op == "3":
            self.pedido.adicionar("Macarrão")
        elif op == "4":
            break
        elif op == "5":
            self.pedido.mostrar_pedido()
        else:
            print("Opção inválida.")
            continue

        print("\nItem adicionado!")
        input("\nPressione Enter para continuar...")

#BEBIDAS

    def bebidas(self):
     while True:
        print("\n--- Bebidas ---")        
        print("1. Soda italiana de limão")        
        print("2. Soda italiana de morango")        
        print("3. Soda italian")        
        print("6. Água com gás")        
        print("7. Voltar ao ca de maracujá")        
        print("4. Refrigerante lata")        
        print("5. Água mineralardápio")        
        print("8. Encerrar atendimento")        
    

        op = input("Escolha sua bebida: ")

        if op == "1":
            self.pedido.adicionar("Soda limão")
        elif op == "2":
            self.pedido.adicionar("Soda morango")
        elif op == "3":
            self.pedido.adicionar("Soda maracujá")
        elif op == "4":
            self.pedido.adicionar("Refrigerante lata")
        elif op == "5":
            self.pedido.adicionar("Água mineral")
        elif op == "6":
            self.pedido.adicionar("Água com gás")
        elif op == "7":
            break
        elif op == "8":
            self.pedido.mostrar_pedido()
        else:
            print("Opção inválida.")
            continue

        print("\nItem adicionado!") 
        input("\nPressione Enter para continuar...\n")    
