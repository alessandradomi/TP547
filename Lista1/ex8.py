import numpy as np
import matplotlib.pyplot as plt


def main():
    N = int(input("Digite a quantidade de amostras: "))
    X = np.array([])

    for i in range(N):
        x1 = np.random.uniform(-1, 1)
        x2 = np.random.uniform(0, 1)

        while (x2 >= pow(x1, 2)):  #função fx/cgx
            x1 = np.random.uniform(-1, 1)
            x2 = np.random.uniform(0, 1)
        X = np.append(X, x1)

    plotar_histograma(X)


def plotar_histograma(seq):
    X = np.arange(-1, 1, 0.05)
    fx = 1.5 * pow(X, 2)
    plt.plot(X, fx)
    plt.hist(seq, bins=100, density=True)
    plt.show()


if __name__ == "__main__":
    main()
