import pickle as pkl


arquivo = "arquivos-pkl/comandos.pkl"


class Funcs:
    def comandos(self) -> str:
        try:
            with open(arquivo, "rb") as file:
                texto = pkl.load(file)
        except FileNotFoundError:
            print("Arquivo não encontrado!")

        return texto


