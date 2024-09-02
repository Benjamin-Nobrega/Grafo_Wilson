def funcao(x):
    caracteresPermitidos = [".","1","2","3","4","5","6","7","8","9","0","+","*","-","/"]
    for i in x:
        if i not in caracteresPermitidos:
            print("Não permitido")
            return "Banido"
    return eval(x)

def pesquisaBinaria(x):
    lista = []
    numTentativas = 0
    for i in range(10000000):
        lista.append(i)
    while True:

        indice = int(len(lista)/2)
        num = lista[indice]
        #resposta = input(f"{num} é o número certo?\n") == "s"
        resposta = x == num
        if resposta:
            return numTentativas
        #maiorOuMenor = input("É maior ou menor?\n") == "maior"
        maiorOuMenor = x>num
        if maiorOuMenor:
            del lista[0:indice]
        else:
            del lista[indice:-1]
        numTentativas +=1

numero = int(input("Digite um número \n"))
print(f"{pesquisaBinaria(numero)} repetições")
