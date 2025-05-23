import pyautogui as py
import pickle as pkl

arquivo = "arquivos-pkl/texto.pkl"

class Escritor:

    def criar_texto(self, texto: str):
        try:
            with open(arquivo, "rb") as file:
                dados = pkl.load(file)
        except FileNotFoundError:
            dados = []

        dados.clear()
        dados.append(texto)

        with open(arquivo, "wb") as file:
            pkl.dump(dados, file)

        print("Texto salvo!")

    def ver_texto(self):
        try:
            with open(arquivo, "rb") as file:
                dados = pkl.load(file)
            print(f"O Texto salvo: \n{dados}")
        except:
            raise FileNotFoundError("O arquivo não existe!")
        
    # pegar o texto no arquivo mas com um return dele
    def pegar_texto(self) -> str:
        try:
            with open(arquivo, "rb") as file:
                dados = pkl.load(file)
        except FileNotFoundError:
            print("O arquivo não existe!")

        return dados

            




        

        


    
