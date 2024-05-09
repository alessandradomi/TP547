import numpy as np
import matplotlib.pyplot as plt


# transmissor MPAM
# M = 2**k, k >= 1

def gerar_lista_palavras():
    # converter decimal para binário

    lista = []
    for i in range(M):
        palavra = []

        quociente, resto = divmod(i, 2)
        palavra.append(resto)
        if quociente == 1: palavra.append(quociente)

        while quociente >= 2:
            quociente, resto = divmod(quociente, 2)
            palavra.append(resto)
            if quociente == 1: palavra.append(quociente)

        while len(palavra) < comprimento_palavras: palavra.append(0)

        palavra.reverse()
        lista.append(palavra)  # palavra binária

    return lista


def gerar_lista_niveis():
    # calcular níveis PAM

    lista = []
    for i in range(M):
        nivel = i - (M - 1) / 2
        lista.append(nivel)

    return lista


def mapear_bits():
    # mapear palavras binárias a seus respectivos níveis

    mapeamento = dict()
    indice = 0
    for palavra in lista_palavras:
        mapeamento[tuple(palavra)] = lista_niveis[indice]
        indice += 1

    return mapeamento


def gerar_sequencia_bits():
    # sequencia de bits para transmissão

    sequencia = (0.5 < np.random.rand(comprimento_dados))
    sequencia = np.repeat(sequencia, fator_expansao)

    return sequencia


def gerar_sequencia_niveis():
    # converter bits em símbolos (níveis)

    n_simbolos = int(comprimento_dados / comprimento_palavras)
    sequencia = []
    palavra = []
    indice = 0
    for i in range(n_simbolos):
        for j in range(comprimento_palavras):  # monta a palavra binária
            palavra.append(sequencia_bits[indice])
            indice += 10

        sequencia.append(mapeamento_palavra_nivel[tuple(palavra)])  # seleciona nível correspondente
        palavra.clear()

    sequencia = np.repeat(sequencia, fator_expansao * comprimento_palavras)

    return sequencia


def gerar_trem_impulsos():
    sequencia = []
    n_impulsos = int(comprimento_dados / comprimento_palavras)
    n_zeros = fator_expansao * comprimento_palavras - 1

    for impulso in range(n_impulsos):
        sequencia.append(1)

        for i in range(n_zeros): sequencia.append(0)

    return sequencia


def plotar_figuras():
    t = np.linspace(0, comrpimento_vetor_dados, comrpimento_vetor_dados)  # eixo do tempo

    plt.figure(1)
    plt.title('Etapas da transmissão em ' + str(M) + 'PAM')
    plt.plot(t, sequencia_bits, 'b--')
    plt.plot(t, sequencia_niveis, 'r--')
    plt.plot(t, entrada_filtro, 'g*')
    plt.legend(('Dados', 'Níveis dos símbolos', 'Sinal transmitido'), loc='lower left')

    plt.figure(2)
    plt.title('Dados')
    plt.plot(t, sequencia_bits, 'b')
  
    plt.figure(3)
    plt.title('Níveis dos símbolos')
    plt.plot(t, sequencia_niveis, 'r')
  
    plt.figure(4)
    plt.title('Sinal transmitido')
    plt.plot(t, entrada_filtro, 'g')
  
    plt.show()


# parâmetros da modulação
M = 4
comprimento_palavras = int(np.log2(M))  # nº de bits de cada simbolo

# dicionário de palavras binárias
lista_palavras = gerar_lista_palavras()  # escopo de palavras binárias para a modulação escolhida
lista_niveis = gerar_lista_niveis()  # escopo de níveis correspondentes aos símbolos da modulação
mapeamento_palavra_nivel = mapear_bits()  # mapeamento entre as palavras binárias e os níveis da modulação

# dados
comprimento_dados = 50 * comprimento_palavras  # comprimento do fluxo de bits para transmissão
fator_expansao = 10  # fator de expansão para construção do sinal quadrado
comrpimento_vetor_dados = comprimento_dados * fator_expansao  # comprimento do vetor de dados
sequencia_bits = gerar_sequencia_bits()  # fluxo de bits para transmissão

# modulação
sequencia_niveis = gerar_sequencia_niveis()  # fluxo de níveis de símbolos para a transmissão
trem_impulsos = gerar_trem_impulsos()
entrada_filtro = sequencia_niveis * trem_impulsos  # combinação do fluxo de níveis de símbolos com o trem de impulsos

plotar_figuras()
