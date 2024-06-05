import random
import threading


qtde = 0
menorValor = 0
caminhoMaisRapido = ""
matriz = 0
threads = []
primeiraVezPassando = True


def acharCaminho(
    pInicial,
    pFinal,
    caminho,
    valorAresta=0,
):
    global matriz
    contador = 0
    if pInicial == pFinal:
        global qtde, menorValor, caminhoMaisRapido, primeiraVezPassando
        caminho = [x + 1 for x in caminho]
        caminho = " -> ".join(map(str, caminho))
        if primeiraVezPassando:
            primeiraVezPassando = False
            menorValor = valorAresta
        elif menorValor > valorAresta:
            menorValor = valorAresta
            caminhoMaisRapido = caminho

        qtde += 1
        print(f"{caminho}: {valorAresta}\n")
        return 0
    for _ in matriz[pInicial]:
        valor = matriz[pInicial][contador]

        if contador not in caminho and valor > 0:

            global threads
            thread = threading.Thread(
                target=acharCaminho,
                args=(
                    contador,
                    pFinal,
                    caminho.copy() + [contador],
                    valorAresta + valor,
                ),
            )
            threads.append(thread)
            thread.start()

        contador += 1


def iniciarMatriz():
    numRange = int(input("range: "))
    lista = [[0 for _ in range(numRange)] for _ in range(numRange)]
    for i in range(numRange):
        for j in range(numRange):
            if i == j:
                lista[i][j] = 0
            else:
                lista[i][j] = 0
    return lista


def main():
    global matriz
    while True:
        escolha = int(
            input(
                "\n1: Iniciar a Matriz\n2: Mostrar a Matriz\n3: Editar a Matriz\n4: Números Aleatórios\n5: Achar caminho\n6: Excluir a Matriz\n"
            )
        )

        if escolha == 1:
            matriz = iniciarMatriz()
        elif escolha == 2 and isinstance(matriz, list):
            for i in matriz:
                print(i)
        elif escolha == 3 and isinstance(matriz, list):
            orientadoBool = input("É orientado ou não? (Y/N)").upper() == "Y"
            arestas = int(input("Quantas arestas?\n"))
            for i in range(arestas):
                # Escrever no formato p1,p2,valor
                x, y, valor = map(int, input("Índices e valor: ").split(","))
                if y == x:
                    print("Os índice não podem ser iguais")
                else:
                    matriz[x - 1][y - 1] = valor
                    if not orientadoBool:
                        matriz[y - 1][x - 1] = valor

        elif escolha == 4 and isinstance(matriz, list):
            lenght = len(matriz)
            for i in range(lenght):
                for j in range(lenght):
                    if not i == j:
                        matriz[j][i] = random.randrange(0, 10)
        elif escolha == 5 and isinstance(matriz, list):
            pInicial = int(input("Ponto inicial: ")) - 1
            pFinal = int(input("Ponto final: ")) - 1
            caminho = [pInicial]
            global threads
            acharCaminho(pInicial, pFinal, caminho.copy())
            for i in threads:
                i.join()
            print(
                f"De {qtde} repetições, o caminho mais rápido é {caminhoMaisRapido} com valor {menorValor}\n"
            )

        elif escolha == 6 and isinstance(matriz, list):
            matriz = 0
            print("Matriz apagada")

        else:
            if not isinstance(matriz, list):
                print("Inicialize a matriz")
            else:
                print("Escolha uma opção válida")


if __name__ == "__main__":
    main()
