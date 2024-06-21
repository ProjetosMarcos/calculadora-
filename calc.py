import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        self.resultado = tk.StringVar()

        self.criar_interface()

    def criar_interface(self):
        entrada = tk.Entry(self.root, textvariable=self.resultado, font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=4)
        entrada.grid(row=0, column=0, columnspan=4)

        botoes = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        linha = 1
        coluna = 0

        for botao in botoes:
            self.criar_botao(botao, linha, coluna)
            coluna += 1
            if coluna > 3:
                coluna = 0
                linha += 1

    def criar_botao(self, valor, linha, coluna):
        comando = lambda: self.on_click(valor)
        botao = tk.Button(self.root, text=valor, padx=20, pady=20, font=('Arial', 18), command=comando)
        botao.grid(row=linha, column=coluna)

    def on_click(self, valor):
        if valor == "=":
            try:
                resultado = str(eval(self.resultado.get()))
                self.resultado.set(resultado)
            except Exception as e:
                self.resultado.set("Erro")
        elif valor == "C":
            self.resultado.set("")
        else:
            self.resultado.set(self.resultado.get() + valor)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
