import matplotlib.pyplot as plt

comprimento_polinomios = 9
comprimento_sequencia = 2 ** comprimento_polinomios - 1

G1 = [1 for i in range(comprimento_polinomios)]  # inicialização em 1
G2 = [1 for i in range(comprimento_polinomios)]  # inicialização em 1
sequencia = []

indice_saida_G1 = [9]
indice_saida_G2 = [3, 6]
indice_retorno_G1 = [4, 9]
indice_retorno_G2 = [3, 4, 6, 9]

for j in range(comprimento_sequencia):
    saida_G1 = sum([G1[i - 1] for i in indice_saida_G1]) % 2  # operação xor para saída do registrador G1
    saida_G2 = sum([G2[i - 1] for i in indice_saida_G2]) % 2  # operação xor para saída do registrador G2
    sequencia.append(saida_G1 ^ saida_G2)  # saída do gerador

    retorno_G1 = sum([G1[i - 1] for i in indice_retorno_G1]) % 2  # operação xor para retorno do registrador G1
    retorno_G2 = sum([G2[i - 1] for i in indice_retorno_G2]) % 2  # operação xor para retorno do registrador G2

    for k in reversed(range(1, comprimento_polinomios)):  # desloca elementos dos registradores
        G1[k] = G1[k - 1]
        G2[k] = G2[k - 1]

    # inclui os retornos
    G1[0] = retorno_G1
    G2[0] = retorno_G2

for i in range(len(sequencia)):
    if sequencia[i] == 0: sequencia[i] = 1
    else: sequencia[i] = -1
    i += 1

print(sequencia)

X = range(0, comprimento_sequencia)
plt.plot(X, sequencia)
plt.grid()
plt.show()
