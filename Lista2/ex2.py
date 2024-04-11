import numpy as np
import random

N = 100000
n = 5

dado = [1, 2, 3, 4, 5, 6]
lista_experimentos = []
cont = 0

for i in range(N):
    vetor_valores_sorteados = np.array([])

    for j in range(n):
        vetor_valores_sorteados = np.append(vetor_valores_sorteados, random.choice(dado))

    lista_experimentos.append(vetor_valores_sorteados)

for experimento in lista_experimentos:
    if np.isin(6, experimento):
        cont += 1

print('A probabilidade de se obter pelo menos um dado com 6 ao jogar 5 dados é ' + str(cont/N) + '.')
