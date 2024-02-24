import customtkinter as tk

class TelaLogin(tk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Login")
        self.parent = parent
        self.geometry("500x500")

        self.label_usuario = tk.CTkLabel(self, text="Usuário:")
        self.label_usuario.pack()
        self.entry_usuario = tk.CTkEntry(self)
        self.entry_usuario.pack()

        self.label_senha = tk.CTkLabel(self, text="Senha:")
        self.label_senha.pack()
        self.entry_senha = tk.CTkEntry(self, show="*")
        self.entry_senha.pack()

        self.botao_login = tk.CTkButton(self, text="Login", command=self.verificar_login)
        self.botao_login.pack()

    def verificar_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        if usuario == "VentoNorte" and senha == "Valores@21":
            self.destroy()  # Fecha a tela de login
            self.parent.tela_principal()  # Chama a tela principal
        else:
            tk.CTkmessagebox.showerror("Erro de login", "Usuário ou senha incorretos")

class TelaPrincipal(tk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Tela Principal")

        self.label_bem_vindo = tk.CTkLabel(self, text="Bem-vindo à tela principal!")
        self.label_bem_vindo.pack()

def main():
    root = tk.CTk()
    root.withdraw()  # Esconde a janela principal padrão

    def tela_principal():
        TelaPrincipal(root)

    login = TelaLogin(root)
    login.parent.tela_principal = tela_principal  # Adiciona uma referência à função da tela principal

    root.mainloop()

if __name__ == "__main__":
    main()