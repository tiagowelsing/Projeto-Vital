import sys
from collections import Counter
import tkinter as tk
from tkinter import messagebox

# ===============================================
# CLASSES DE NEGÓCIO (MANTIDAS)
# ===============================================

class Pedido:
    """Gerencia a lista de itens do pedido."""
    def __init__(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def limpar(self):
        self.itens = []

    def gerar_resumo(self):
        """Retorna uma string formatada com o resumo do pedido."""
        if not self.itens:
            return "Você não realizou um pedido."
        
        contagem = Counter(self.itens)
        resumo_lines = ["\n===== Resumo do Pedido ====="]
        for item, qtd in contagem.items():
            resumo_lines.append(f"- {qtd}x {item}")
        resumo_lines.append("\nAté breve!")
        
        return "\n".join(resumo_lines)

# ===============================================
# CLASSE PRINCIPAL DA INTERFACE GRÁFICA (GUI)
# ===============================================

class CardapioGUI:
    def __init__(self, master):
        self.master = master
        master.title("Cardápio Del Polpollo")
        
        self.pedido = Pedido()
        
        # Dicionários que mapeiam opções para os nomes dos itens
        self.MENU_ITENS = {
            "entradas": {
                "1": "Pizza branca", "2": "Palitos de queijo", "3": "Bolinha de queijo"
            },
            "massas": {
                "1": "Pizza", "2": "Lasanha", "3": "Macarrão"
            },
            "bebidas": {
                "1": "Soda limão", "2": "Soda morango", "3": "Soda maracujá",
                "4": "Refrigerante lata", "5": "Água mineral", "6": "Água com gás"
            }
        }
        
        # Configuração da janela principal
        self.main_frame = tk.Frame(master, padx=20, pady=20)
        self.main_frame.pack()
        
        tk.Label(self.main_frame, text="Cardápio Del Polpollo", font=('Arial', 18, 'bold')).pack(pady=10)
        
        # Botões do Menu Principal
        self.create_menu_buttons(self.main_frame)
        
        # Área de exibição do pedido atual
        self.pedido_label = tk.Label(master, text="Pedido Atual: (Vazio)", fg="blue")
        self.pedido_label.pack(pady=10)
        
        self.update_pedido_label()

    def create_menu_buttons(self, frame):
        """Cria os botões principais do cardápio."""
        
        # Mapeamento dos botões para as funções que abrem sub-menus
        menu_options = [
            ("1. Entradas", lambda: self.show_submenu("Entradas", self.MENU_ITENS["entradas"])),
            ("2. Massas", lambda: self.show_submenu("Massas", self.MENU_ITENS["massas"])),
            ("3. Bebidas", lambda: self.show_submenu("Bebidas", self.MENU_ITENS["bebidas"])),
            ("4. Finalizar Pedido", self.encerrar_atendimento)
        ]
        
        for text, command in menu_options:
            tk.Button(frame, text=text, command=command, width=30, height=2).pack(pady=5)
            
    def update_pedido_label(self):
        """Atualiza o label na tela principal com a contagem de itens."""
        if not self.pedido.itens:
            summary_text = "Pedido Atual: (Vazio)"
        else:
            count = Counter(self.pedido.itens)
            # Exibe os 3 primeiros itens com suas quantidades
            summary_text = "Pedido Atual: " + ", ".join([f"{qtd}x {item}" for item, qtd in count.most_common(3)])
            if len(count) > 3:
                summary_text += " e mais..."
                
        self.pedido_label.config(text=summary_text)

    def add_item_to_pedido(self, item_name, window):
        """Adiciona o item ao pedido e fecha a janela do sub-menu."""
        self.pedido.adicionar(item_name)
        messagebox.showinfo("Sucesso", f"'{item_name}' adicionado ao seu pedido!")
        self.update_pedido_label()
        window.destroy()

    def show_submenu(self, title, items_dict):
        """Cria e exibe uma nova janela para o sub-menu (Entradas, Massas, etc.)."""
        
        # Cria a nova janela (TopLevel)
        submenu_window = tk.Toplevel(self.master)
        submenu_window.title(f"Menu - {title}")
        
        tk.Label(submenu_window, text=f"--- {title} ---", font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Cria os botões para cada item do sub-menu
        for key, name in items_dict.items():
            # A função lambda garante que o nome do item correto seja passado
            command = lambda item=name: self.add_item_to_pedido(item, submenu_window)
            tk.Button(submenu_window, text=f"{key}. {name}", command=command, width=40).pack(pady=5, padx=20)
            
        # Botão para fechar o sub-menu sem adicionar nada
        tk.Button(submenu_window, text="Voltar ao Cardápio", command=submenu_window.destroy, bg="red", fg="white", width=40).pack(pady=15, padx=20)
        
        # Centraliza a nova janela
        submenu_window.transient(self.master) # Mantém acima da principal
        submenu_window.grab_set() # Desabilita interação com a principal
        self.master.wait_window(submenu_window) # Espera a nova janela fechar

    def encerrar_atendimento(self):
        """Mostra o resumo do pedido em uma caixa de mensagem e fecha o app."""
        resumo = self.pedido.gener_resumo()
        messagebox.showinfo("Resumo do Pedido", resumo)
        self.master.destroy()


# ===============================================
# INICIALIZAÇÃO
# ===============================================

if __name__ == "__main__":
    # 1. Cria a janela principal do Tkinter (root)
    root = tk.Tk()
    
    # 2. Instancia a classe que configura a GUI, passando a janela principal
    app = CardapioGUI(root)
    
    # 3. Inicia o loop principal do Tkinter
    root.mainloop()