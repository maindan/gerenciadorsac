import customtkinter as ctk
ctk.set_default_color_theme("dark-blue")

# app = ctk.CTk()
# app.geometry("500x400")
# app.title("Gerenciador de RATs")
# app.minsize(500, 400)

# # FUNÇÃO

# def login():
#     print(username, password)

# label = ctk.CTkLabel(text="Gerenciador de Rats", width=30)
# username = ctk.CTkEntry(placeholder_text="Login")
# password = ctk.CTkEntry(placeholder_text="Senha", show="*")
# button = ctk.CTkButton(#                                  text="Entrar",
#                                  command=login
#                                  )


# label.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)
# username.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)
# password.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)
# button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)



# app.mainloop()

class TelaLogin(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gerenciador de Rats")
        self.parent = parent
        self.geometry("400x400")
        self.label = ctk.CTkLabel(self, text="Gerenciador de Rats", width=30, height=30)
        self.label.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)
        self.username = ctk.CTkEntry(self, placeholder_text="Login")
        self.username.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)
        self.password = ctk.CTkEntry(self, placeholder_text="Senha", show="*")
        self.password.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)
        self.bt_login = ctk.CTkButton(self, text="Entrar", command=self.verifyLogin)
        self.bt_login.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    def verifyLogin(self):
        self.destroy()
        self.parent.tela_principal()

class TelaPrincipal(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Tela Principal")
        self.geometry("800x500")


def main():
    root = ctk.CTk()
    root.withdraw()

    def tela_principal():
        TelaPrincipal(root)

    login = TelaLogin(root)
    login.parent.tela_principal = tela_principal


    root.mainloop()

if __name__ == "__main__":
    main()