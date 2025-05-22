import pyautogui as py
import pickle
from time import sleep

arquivo = "arquivos-pkl/posicao.pkl"

class Mouse:

    def posicao(self) -> None:
        sleep(5.0) # tempo de espera de 5 segundos
        posi = py.position() # pegar a posição do mouse
        posi = str(posi)
        # Salvar a posição em um .pkl
        print(posi)

        with open(arquivo, "wb") as file:
            pickle.dump(posi, file)

    def mostrar_loc(self) -> str:
        with open(arquivo, "rb") as file:
            posi = pickle.load(file)

        
        return posi


    def clique(self) -> None:
        with open(arquivo, "rb") as file:
            localizacao = pickle.load(file)

        sleep(5.0) # tempo para iniciar

        cliques = 0

        while cliques != 100:
            py.click(localizacao)
            cliques += 1

























