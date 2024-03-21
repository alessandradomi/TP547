import numpy as np

def main():
    N = int(input("Digite a quantidade de amostras: "))
    X = np.array([])

    U = np.random.uniform(0, 1, N)  #vetor de valores aleatórios com distribuição uniforme (base para geração da VA)

    for u in U:  #gerar valores para VA X
        x = np.log((np.exp(2) - 1) * u + 1)  #função inversa de Fx
        X = np.append(X, x)

    print(X)

if __name__ == "__main__":
    main()
