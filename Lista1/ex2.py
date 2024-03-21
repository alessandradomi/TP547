import numpy as np
import math

lambda1 = 6  #média de chamadas por hora


def main():
    N = int(input("Digite a quantidade de amostras: "))
    U = np.random.uniform(0, 1, N)  #vetor de valores aleatórios com distribuição uniforme (base para geração da VA)

    X = np.array([])  #vetor para salvar VA com distribuição de Poisson

    for u in U:  #gerar valores para VA X
        x = gerar_valor_poisson(u)
        X = np.append(X, x)

    questoes(X, N)


def gerar_valor_poisson(i):
    x = 0
    Px0 = np.exp(-lambda1)  #propabilidade para x = 0 (inicial)
    Px = Px0
    Fx = Px

    while i >= Fx:  #gera um valor para variável x utilizando a cdf para aproximação
        Px = lambda1 / (x + 1) * Px  #demais probabilidades de forma recursiva
        Fx = Fx + Px  #calcula Fx acumulando a Px
        x += 1  #incrementa x

    return x


def questoes(vetor, n):
    Px0 = calcular_Px(vetor, n, 0)
    Px1 = calcular_Px(vetor, n, 1)
    Px2 = calcular_Px(vetor, n, 2)
    Px3 = calcular_Px(vetor, n, 3)
    Px4 = calcular_Px(vetor, n, 4)
    Px5 = calcular_Px(vetor, n, 5)
    Px6 = calcular_Px(vetor, n, 6)
    Px7 = calcular_Px(vetor, n, 7)

    print("a) A probabilidade de o suporte técnico não receber chamadas em uma hora é " + str(Px0) + ".\n")
    print("b) A probabilidade de o suporte técnico receber menos que 8 chamadas é " +
          str(Px0 + Px1 + Px2 + Px3 + Px4 + Px5 + Px6 + Px7) + ".\n")
    print("c) O número médio de chamadas por hora é " + str(lambda1) + ".\n")
    print("d) A variância de C é " + str(lambda1) + ".\n")
    print("e) O desvio padrão de C é " + str(math.sqrt(lambda1)) + ".\n")


def calcular_Px(vetor, n, x):
    cont = 0

    for v in vetor:  #percorre vetor
        if v == x:
            cont += 1  #incrementa contador se encontra valor
    Px = cont / n  #probabilidade para valor testado

    return Px


def plotar_histograma(X, n):
    ind = np.arange(n)
    plt.bar(ind, X)
    plt.xlabel('amostra')
    plt.ylabel('X(i)')
    plt.show()


if __name__ == "__main__":
    main()
