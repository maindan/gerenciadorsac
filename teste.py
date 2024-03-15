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
    
    
    
    
#include <stdio.h>
#define MAX 50

typedef int TIPOCHAVE;

typedef struct {
    TIPOCHAVE chave;
} REGISTRO;

typedef struct {
    REGISTRO A[MAX+1];
    int nrElem;
} LISTA;

void inicializar(LISTA* l) {
    l->nrElem = 0;
}

void qtdElementos(LISTA* l) {
    printf("numero de elementos da lista = %i", l->nrElem);
}

void exibirLista(LISTA* l) {
    int i;
    for(i = 0; i < l->nrElem; i++)
        printf("%i ", l->A[i].chave);

    printf("\n");
}

void adcElem(LISTA* l, TIPOCHAVE ele) {
    if(l->nrElem == 0)
        l->A[0].chave = ele;
    else 
        l->A[l->nrElem].chave = ele;
    l->nrElem++;
    printf("elemento %i adicionado na posição %i da lista \n", ele, l->nrElem - 1);
}

int buscarElem(LISTA* l, TIPOCHAVE ch) {
    int i = 0;
    while(i < l->nrElem){
        if(l->A[i].chave == ch)
            return i;
        else 
            i++;
    }
    return -1;
}

void insercaoOrd(LISTA* l, REGISTRO reg, TIPOCHAVE ch) {
    if(l->nrElem != MAX || i < 0)
        
}

void exclusão(LISTA* l, REGISTRO reg){

}

void reiniciarLista(LISTA* l) {
    l->nrElem = 0;
}


int main() {
    LISTA numeros;
    inicializar(&numeros);
    adcElem(&numeros, 2);
    adcElem(&numeros, 7);
    adcElem(&numeros, 4);
    adcElem(&numeros, 3);
    exibirLista(&numeros);
    printf("posição do elemento: %i", buscarElem(&numeros, 7));
    return 0;
}