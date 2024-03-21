import numpy as np

p = 0.4  #probabilidade de sucesso (retirar bola preta)
evento_sucesso = 6  #posição do primeiro evento de sucesso


def main():
    N = int(input("Digite a quantidade de experimentos: "))

    lista_VA_bernoulli = []  #Lista para salvar VAs (experimentos) com distribuição Bernoulli

    for i in range(N):
        X = gerar_VA_bernoulli()
        lista_VA_bernoulli.append(X)

    questoes(lista_VA_bernoulli, N)


def gerar_VA_bernoulli():
    U = np.random.uniform(0, 1, 100)  #vetor de 100 valores aleatórios com distribuição uniforme (base para geração da VA)
    X = np.array([])  #vetor para salvar VA com distribuição de Bernoulli

    for u in U:  #gerar valores para VA X
        if u > p:  #decide por 0 (bola branca) se valor superior a probabilidade de sucesso
            x = 0
            X = np.append(X, x)

        else:  #caso contrário, decide por 1
            x = 1
            X = np.append(X, x)

    return X


def questoes(lista, n):
    Px = calcular_Px(lista, n)

    print("A probabilidade de a 6ª bola retirada seja preta é " + str(Px) + ".")


def calcular_Px(lista, n):
    cont_experimentos_sucesso = 0  # experimentos que tiveram 5 bolas brancas e 1 bola preta no início

    for vetor in lista:  # percorre lista de VAs (experimentos)
        cont0 = 0  # contador de 0s

        for i in range(evento_sucesso - 1):  # verifica valores dos 5 primeiros eventos
            if vetor[i] == 0:
                cont0 += 1

        if cont0 == 5:  # verifica se os 5 primeiros eventos foram 0 (bola branca)
            if vetor[6] == 1:  #se o próximo evento é 1 (bola preta), contabiliza como um experimento de sucesso
                cont_experimentos_sucesso += 1

    Px = cont_experimentos_sucesso / n  # probabilidade para valor testado

    return Px

if __name__ == "__main__":
    main()
