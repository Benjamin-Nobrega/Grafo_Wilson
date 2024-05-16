import random


def acharCaminho(pInicial, pFinal, matriz, indicesUsados, caminho):
    """
    Pegar caminhos diferentes
    Mostrar o caminho que pegou (feito +-)
    
    """
    contador = 0
    if pInicial == pFinal:
        
        return 0
    for _ in matriz[pInicial]:

        if matriz[pInicial][contador] == 0:
            ...
        elif contador not in indicesUsados:
            indicesUsados.append(contador)
            var = acharCaminho(contador, pFinal, matriz, indicesUsados, caminho)
            if not(var == None):
                caminho.insert(0, contador+1)
                return matriz[pInicial][contador] + var
        contador += 1
    return None


def iniciarMatriz():
    # numRange = int(input("range: "))
    # lista = [[0 for _ in range(numRange)] for _ in range(numRange)]
    # for i in range(numRange):
    # for j in range(numRange):
    # if i == j:
    # lista[i][j] = 0
    # else:
    # lista[i][j] = 0
    lista = [
        [0, 12, 4, 0, 0, 0],
        [0, 0, 6, 6, 0, 0],
        [0, 0, 0, 0, 2, 0],
        [0, 0, 8, 0, 0, 6],
        [0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0],
    ]
    return lista


def main():
    matriz = 0
    while True:
        escolha = int(
            input(
                "\n1: Iniciar a Matriz\n2: Mostrar a Matriz\n3: Editar a Matriz\n4: Números Aleatórios\n5: Excluir a Matriz\n6: Achar caminho\n"
            )
        )

        if escolha == 1:
            matriz = iniciarMatriz()
        elif escolha == 2 and isinstance(matriz, list):
            for i in matriz:
                print(i)
        elif escolha == 3 and isinstance(matriz, list):
            x = int(input("Primeiro valor: ")) - 1
            y = int(input("Segundo valor: ")) - 1
            if y == x:
                print("Os índice não podem ser iguais")
            else:
                valor = int(input("Valor: "))
                matriz[y][x] = valor

        elif escolha == 4 and isinstance(matriz, list):
            lenght = len(matriz)
            for i in range(lenght):
                for j in range(lenght):
                    if not i == j:
                        matriz[j][i] = random.randrange(0, 10)
        elif escolha == 5 and isinstance(matriz, list):
            matriz = 0
            print("Matriz apagada")
        elif escolha == 6 and isinstance(matriz, list):
            pInicial = int(input("Ponto inicial: "))
            pFinal = int(input("Ponto final: "))
            indicesUsados = []
            caminho = []
            var = acharCaminho(pInicial - 1, pFinal - 1, matriz, indicesUsados.copy(), caminho)
            caminho.insert(0,pInicial)
            if var:
                print(f"{caminho}: {var}")

        else:
            if not isinstance(matriz, list):
                print("Inicialize a matriz")
            else:
                print("Escolha uma opção válida")


if __name__ == "__main__":
    main()
