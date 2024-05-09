import numpy as np
import matplotlib.pyplot as plt
import random


# receptor MPAM
# M = 2**k, k >= 1
# com ruído

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
    print(lista)
    return lista


def mapear_bits():
    # mapear palavras binárias a seus respectivos níveis

    mapeamento = dict()
    indice = 0
    for palavra in lista_palavras:
        mapeamento[tuple(palavra)] = lista_niveis[indice]
        indice += 1

    return mapeamento


def gerar_trem_impulsos():
    sequencia = []
    n_impulsos = int(comprimento_dados / comprimento_palavras)
    n_zeros = fator_expansao * comprimento_palavras - 1

    for impulso in range(n_impulsos):
        sequencia.append(1)

        for i in range(n_zeros): sequencia.append(0)

    return sequencia


def gerar_sinal_recebido():
    # gera o sinal recebido com adição de ruído

    n_simbolos = int(comprimento_dados / comprimento_palavras)
    sequencia_niveis_transmitida = np.array([])
    for i in range(n_simbolos):
        # gerar valores aleatórios da lista de níveis
        sequencia_niveis_transmitida = np.append(sequencia_niveis_transmitida, random.choice(lista_niveis))

    sequencia_niveis_transmitida = np.repeat(sequencia_niveis_transmitida, fator_expansao * comprimento_palavras)
    sequencia_impulsos_transmitida = sequencia_niveis_transmitida * trem_impulsos
    sequencia_recebida = sequencia_impulsos_transmitida + ruido

    return sequencia_niveis_transmitida, sequencia_impulsos_transmitida, sequencia_recebida


def extrair_dados():
    # extrai os níveis e os bits do sinal recebido

    n_simbolos = int(comprimento_dados / comprimento_palavras)
    indice = 0
    sequencia_bits = []
    sequencia_niveis = []

    for i in range(n_simbolos):
        valor_recebido = sinal_recebido[indice]
        nivel_aprox = min(lista_niveis, key=lambda x: abs(x - valor_recebido))  # decide pelo nível mais próximo
        indice += fator_expansao * comprimento_palavras

        for palavra, nivel in mapeamento_palavra_nivel.items():  # extrai os bits de cada nível
            if nivel == nivel_aprox:
                sequencia_niveis.append(nivel)
                for bit in palavra: sequencia_bits.append(bit)
                break

    sequencia_bits = np.repeat(sequencia_bits, fator_expansao)
    sequencia_niveis = np.repeat(sequencia_niveis, fator_expansao * comprimento_palavras)

    return sequencia_bits, sequencia_niveis


def plotar_figuras():
    t = np.linspace(0, comprimento_vetor_dados, comprimento_vetor_dados)  # eixo do tempo

    plt.figure(1)
    plt.title('Sinal transmitido')
    plt.plot(t, sinal_transmitido, 'g')

    plt.figure(2)
    plt.title('Sinal recebido')
    plt.plot(t, sinal_recebido, 'b')

    plt.figure(3)
    plt.title('Dados extraidos')
    plt.plot(t, dados_extraidos, 'r')

    plt.figure(4)
    plt.title('Níveis de símbolos transmitidos / recebidos')
    plt.plot(t, niveis_transmitidos, 'g')
    plt.plot(t, niveis_extraidos, 'b--')
    plt.legend(('Transmitidos', 'Recebidos'), loc='lower left')
    
    plt.show()


# parâmetros da modulação
M = 4
comprimento_palavras = int(np.log2(M))  # nº de bits de cada simbolo

# dicionário de palavras binárias
lista_palavras = gerar_lista_palavras()  # escopo de palavras binárias para a modulação escolhida
lista_niveis = gerar_lista_niveis()  # escopo de níveis correspondentes aos símbolos da modulação
mapeamento_palavra_nivel = mapear_bits()  # mapeamento entre as palavras binárias e os níveis da modulação

comprimento_dados = 50 * comprimento_palavras  # comprimento do fluxo de bits para transmissão
fator_expansao = 10  # fator de expansão para construção do sinal quadrado
comprimento_vetor_dados = comprimento_dados * fator_expansao  # comprimento do vetor de dados

# ruído
fator_ruido = 0.5
distancia_niveis = 2 * min(n for n in lista_niveis if n > 0)
ruido = np.random.uniform(0, distancia_niveis * fator_ruido, comprimento_vetor_dados)

# sinal recebido
trem_impulsos = gerar_trem_impulsos()
niveis_transmitidos, sinal_transmitido, sinal_recebido = gerar_sinal_recebido()

# demodulação
dados_extraidos, niveis_extraidos = extrair_dados()

# erro de simbolo na recepção, pode-se variar o fator de ruído ou o M para se observar diferentes desempenhos
erro = ((niveis_transmitidos == niveis_extraidos) == False).sum() / (comprimento_vetor_dados)
print('Erro de simbolo: ' + str(erro) + '%')

plotar_figuras()
