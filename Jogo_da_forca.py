import os
from unicodedata import normalize


def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')


secreto = input("Escreva a palavra secreta: ").upper().strip()
secreto = remover_acentos(secreto)
os.system("cls")
vetor = []
a = 1
while True:
    print("Você tem {} tentativas".format(6-a))
    if a > 5:
        print("Você perdeu")
        s = input("Quer tentar denovo?[S]im ou [N]ão ").upper().strip()
        if s == 'S':
            secreto = input("Escreva a palavra secreta: ").upper().strip()
            os.system("cls")
            vetor.clear()
            saida = []
            saida.clear()
            a = 1
            continue
        elif s == 'N':
            print("Foi bom jogar com você espero que volte noavamente ")
            break
        else:
            print("Vai se fuder então, thau!")
            break

    inp = input("Digite uma letra: ").upper().strip()
    inp = remover_acentos(inp)
    if inp == secreto:
        print(inp.upper())
        print("Parabens você venceu!")
        s = input("Quer tentar denovo?[S]im ou [N]ão ").upper().strip()
        if s == 'S':
            secreto = input("Escreva a palavra secreta: ").upper().strip()
            os.system("cls")
            vetor.clear()
            saida = []
            saida.clear()
            a = 1
            continue
        elif s == 'N':
            print("Foi bom jogar com você espero que volte noavamente ")
            break
        else:
            print("Vai se fuder então, thau!")
            break

    elif len(inp) > 1:
        print("UMA letra apenas meu querido!")
        continue

    # 2
    vetor.append(inp)
    # 3
    if inp not in secreto:
        a += 1
    saida = []
    # 1
    for letra in secreto:
        if letra in vetor:
            saida.append(letra)

        else:
            saida.append(" _")
    # 4
    verificador = "".join(saida)
    if secreto == verificador:
        print(verificador.upper())
        print("Parabens você venceu!")
        s = input("Quer tentar denovo?[S]im ou [N]ão ").upper().strip()
        if s == 'S':
            secreto = input("Escreva a palavra secreta: ").upper().strip()
            os.system("cls")
            vetor.clear()
            saida = []
            saida.clear()
            a = 1
            continue
        elif s == 'N':
            print("Foi bom jogar com você espero que volte noavamente ")
            break
        else:
            print("Vai se fuder então, thau!")
            break
    os.system("cls")
    print(verificador)
