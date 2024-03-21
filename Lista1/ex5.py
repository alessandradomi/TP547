import numpy as np
import matplotlib.pyplot as plt

lambda1 = 1 / 28  #média de passagens compradas em um dia


def main():
    N = int(input("Digite a quantidade de amostras: "))
    U = np.random.uniform(0, 1, N)  #vetor de valores aleatórios com distribuição uniforme (base para geração da VA)

    X = gerar_VA_exponencial(U)  #VA com distribuição Exponencial

    questoes(X, N)
    plotar_funcao(X)


def gerar_VA_exponencial(vetor):
    X = -np.log(vetor) / lambda1

    return X


def questoes(vetor, n):
    x = 4
    cont = 0

    for v in vetor:  #percorre vetor
        if v <= x:
            cont += 1  #incrementa contador se encontra valor
    Px = cont / n  #probabilidade para valor testado

    print("A probabilidade de uma pessoa comprar a passagem com menos de 4 dias de antecedência é " + str(Px) + ".")


def plotar_funcao(X):
    X = np.arange(0, 365, 0.1)
    fx = lambda1 * np.exp(-lambda1 * X)
    plt.plot(X, fx)
    plt.show()

if __name__ == "__main__":
    main()
