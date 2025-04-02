import customtkinter as ctk
from view.venda_view import VendaView
from controller.venda_controller import VendaController
from service.sheet_handler import SheetHandler

def main():
    ctk.set_appearance_mode("Dark") 
    ctk.set_default_color_theme("dark-blue")
    
    root = ctk.CTk()
    root.title("Cadastro de Vendas")
    root.geometry("500x400")
    
    # Inicializa as dependências
    sheet_handler = SheetHandler()
    
    # Cria a view e o controller
    view = VendaView(root)
    controller = VendaController(view, sheet_handler)
    
    # Configura a view com o controller
    view.set_controller(controller)
    
    root.mainloop()

if __name__ == "__main__":
    main()