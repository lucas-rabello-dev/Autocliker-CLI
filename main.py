import customtkinter as ctk
from funcs import Mouse
from escritor import Escritor

m = Mouse()
e = Escritor()

def add_posi_main():
    x = input("Digite a posição x: ")
    y = input("Digite a posição y: ")

    x = int(x)
    y = int(x)

    m.add_posi(x=x, y=y)

def mostrar_loc_main():
    loc = m.mostrar_loc()
    print(loc)

def clique_main():
    try:
        numero_cliques = input("Digite o numero de cliques: ").strip()
        numero_cliques = int(numero_cliques)

        tempo = input("Digite o tempo de pausa em segundos e numero inteiro: ").strip()
        tempo = int(tempo)
    except ValueError as err:
        print(f"Ouve um erro: {err}")
        return


    m.clique(input_cliques=numero_cliques, tempo=tempo)


opcoes = {
    "posi":m.posicao,
    "see-loc":mostrar_loc_main,
    "click":clique_main,
    "create-text":e.criar_texto,
    "see-text":e.ver_texto,
}

while True:
    user = input("AutoClicker prompt ->>> ").strip()
    if user == "sair":
        break
    elif user in opcoes:
        opcoes[user]()
    elif user == "add-posi":
        add_posi_main()
    else:
        print("Comando inválido!")

    




