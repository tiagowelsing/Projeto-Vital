from cardapio import Cardapio

class Main:
    def _init_(self):
        self.sistema = Cardapio()

    def executar(self):
        while True:
            self.sistema.mostrar_cardapio()

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.sistema.entradas()
            elif opcao == "2":
                self.sistema.massas()
            elif opcao == "3":
                self.sistema.bebidas()
            elif opcao == "4":
                print("\nEncerrando atendimento...")
                self.sistema.pedido.mostrar_pedido()
            else:
                print("Opção inválida! Tente novamente.")

if _name_ == "_main_":
    app = Main()
    app.executar()
