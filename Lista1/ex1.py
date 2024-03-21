import numpy as np
import matplotlib.pyplot as plt

#xn = ax mod m

a = 5
m = 7


def main():
    N = int(input("Digite a quantidade de amostras: "))

    for s0 in [4, 7]:  # sequências para sementes 4 e 7
        X = calcular_seq(N, s0)
        plotar_histograma(X, N)

def calcular_seq(n, s):
    X = np.array([s])
    x = s

    for i in range(n):
        x = (a * x) % m  #ax mod m
        X = np.append(X, x)

    print("Sequência gerada para semente " + str(s) + ":\n")
    print(X)

    return X


def plotar_histograma(X, n):
    ind = np.arange(n + 1)
    plt.bar(ind, X)
    plt.xlabel('amostra')
    plt.ylabel('X(i)')
    plt.show()


if __name__=="__main__":
    main()
