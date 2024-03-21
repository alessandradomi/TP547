import numpy as np
import matplotlib.pyplot as plt

p = 0.15  #taxa de rejeição de pistões (taxa de sucesso para o evento rejeição)
n = 8  #tamanho do lote testado (nº de tentativas)


def main():
    N = int(input("Digite a quantidade de amostras: "))
    U = np.random.uniform(0, 1, N)  #vetor de valores aleatórios com distribuição uniforme (base para geração da VA)

    X = np.array([])  #vetor para salvar VA com distribuição Binomial

    for u in U:  #gerar valores para VA X
        x = gerar_valor_binomial(u)
        X = np.append(X, x)

    questoes(X, N)
    plotar_histograma(X, N)


def gerar_valor_binomial(i):
    x = 0
    c = p / (1 - p)
    Px0 = pow((1 - p), n)  #propabilidade para x = 0 (inicial)
    Px = Px0
    Fx = Px

    while i >= Fx:  #gera um valor para variável x utilizando a cdf para aproximação
        Px = (c * (n - x) / (x + 1)) * Px  #demais probabilidades de forma recursiva
        Fx = Fx + Px  #calcula Fx acumulando a Px
        x = x + 1  #incrementa x

    return x


def questoes(vetor, n):
    Px0 = calcular_Px(vetor, n, 0)
    Px1 = calcular_Px(vetor, n, 1)
    Px2 = calcular_Px(vetor, n, 2)
    Px6 = calcular_Px(vetor, n, 6)
    Px7 = calcular_Px(vetor, n, 7)
    Px8 = calcular_Px(vetor, n, 8)

    print("a) A probabilidade de não mais que dois pistões serem rejeitados é " + str(Px0 + Px1 + Px2) + "\n")
    print("b) A probabilidade de pelo menos seis pistões serem rejeitados é " + str(Px6 + Px7 + Px8) + "\n")


def calcular_Px(vetor, n, x):
    cont = 0

    for v in vetor:  #percorre vetor
        if v == x:
            cont += 1  #incrementa contador se encontra valor
    Px = cont / n  #probabilidade para valor testado

    return Px


def plotar_histograma(X, m):
    ind = np.arange(m)
    plt.bar(ind, X)
    plt.xlabel('amostra')
    plt.ylabel('X(i)')
    plt.show()



if __name__ == "__main__":
    main()
