import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root_tk = tkinter.Tk()
root_tk.geometry("500x500")
root_tk.title("GRat")


def buttonClick():
    print('clicou')

button = customtkinter.CTkButton(master=root_tk,
                                 border_color="white",
                                 text_color="white",
                                 corner_radius=10,
                                 command=buttonClick
                                 )
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root_tk.mainloop()