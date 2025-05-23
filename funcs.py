import pyautogui as py
import pickle as pkl
from time import sleep

arquivo = "arquivos-pkl/posicao.pkl"

class Mouse:
    # pegar a posição do mouse
    def posicao(self) -> None:
        sleep(5.0) # tempo de espera de 5 segundos
        posi = py.position() # pegar a posição do mouse
        posi = str(posi)
        # Salvar a posição em um .pkl
        print(posi)

        with open(arquivo, "wb") as file:
            pkl.dump(posi, file)

    # salvar a posição no arquivo
    def add_posi(self, x, y) -> None:
        try:
            with open(arquivo, "rb") as file:
                pkl.load(file)
        except FileNotFoundError:
            print("Arquivo não encontrado para salvar a posição!")

        posi = f"{x}, {y}"

        with open(arquivo, "wb") as file:
            pkl.dump(posi, file)
        print("Posição salva!")


    # retorna a posição salva
    def mostrar_loc(self) -> str:
        with open(arquivo, "rb") as file:
            posi = pkl.load(file)
        return posi

    # acha a localização salva e aplica 
    def clique(self, input_cliques, tempo) -> None:
        with open(arquivo, "rb") as file:
            localizacao = pkl.load(file)
        # aviso de inicio
        print("Início em:")
        for i in range(5, 0, -1):
            print(f"Segundos: {i}", end="\r")
            sleep(1.0)
                

        cliques = 0

        while cliques != input_cliques:
            sleep(tempo)
            py.click(localizacao)
            cliques += 1

























