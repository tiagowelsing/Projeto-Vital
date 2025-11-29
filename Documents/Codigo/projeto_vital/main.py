from cardapio import CardapioGUI   


def main():
    sistema = CardapioGUI()       

    while True:
        sistema.mostrar_cardapio()
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            sistema.entradas()
        elif opcao == "2":
            sistema.massas()
        elif opcao == "3":
            sistema.bebidas()
        elif opcao == "4":
            sistema.pedido.mostrar_pedido()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")    

if __name__ == "__main__":
    main()
