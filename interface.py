import customtkinter as ctk

app = ctk.CTk()
app.geometry("1050x600")
app.minsize(1050, 600)
app.maxsize(1050, 600)


ctk.set_appearance_mode("dark")

tabview = ctk.CTkTabview(master=app,
                        width=800,
                        height=580,
                        segmented_button_fg_color="#00339b"
                        )
tabview.place(x=10, y=10)

tabview.add("Início")
tabview.add("Rats")
tabview.set("Início")

def handle_bt_inicio():
    tabview.set("Início")

def handle_bt_rats():
    tabview.set("Rats")

def showtab():
    print(tabview.get())

button_inicio = ctk.CTkButton(master=app, command=handle_bt_inicio, width=220, height=50, text="Início", font=("Arial bold", 20), fg_color="#00339b")
button_inicio.place(x=820, y=110)
button_rats = ctk.CTkButton(master=app, command=handle_bt_rats, width=220, height=50, text="Rats", font=("Arial bold", 20), fg_color="#00339b")
button_rats.place(x=820, y=170)
button_novaRat = ctk.CTkButton(master=app, command=handle_bt_rats, width=220, height=50, text="Rats", font=("Arial bold", 20), fg_color="#00339b")
button_novaRat.place(x=820, y=230)


frame_inicio = ctk.CTkFrame(master=tabview.tab("Início"), width=780, height=520, fg_color="#2a3c6e")
frame_inicio.pack(anchor=ctk.CENTER)

frame_inicio_rt1 = ctk.CTkFrame(master=frame_inicio, width=150, height=150, fg_color="grey")
frame_inicio_rt1.place(y=10, x=15)
frame_inicio_rt2 = ctk.CTkFrame(master=frame_inicio, width=150, height=150, fg_color="grey")
frame_inicio_rt2.place(y=10, x=210)
frame_inicio_rt3 = ctk.CTkFrame(master=frame_inicio, width=150, height=150, fg_color="grey")
frame_inicio_rt3.place(y=10, x=410)
frame_inicio_rt4 = ctk.CTkFrame(master=frame_inicio, width=150, height=150, fg_color="grey")
frame_inicio_rt4.place(y=10, x=610)

frame_inicio_table = ctk.CTkScrollableFrame(master=frame_inicio, width=740, height=300, fg_color="grey")
frame_inicio_table.place(y=180, x=10)


app.mainloop()

# frame = ctk.CTkFrame(master=app, width=390, height=390, fg_color="white")
# label = ctk.CTkLabel(master=frame, pady=20, text="Gerenciador de Rats", font=("Arial", 20))
# username = ctk.CTkEntry(master=frame, placeholder_text="Login")
# password = ctk.CTkEntry(master=frame, placeholder_text="Senha", show="*")
# button = ctk.CTkButton(master=frame, text="Entrar", command=clickButton)


# frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
# label.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)
# username.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)
# password.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
# button.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)