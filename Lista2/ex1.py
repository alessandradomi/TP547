import numpy as np
import random

vetor_chapeu = ['RO', 'AM', 'AZ', 'VM', 'RO', 'AM', 'AZ', 'VM', \
                'RO', 'AM', 'AZ', 'VM', 'RO', 'AM', 'AZ', 'VM', \
                'RO', 'AM', 'AZ', 'VM', 'RO', 'AM', 'AZ', 'VM', \
                'RO', 'AM', 'AZ', 'VM', 'RO', 'AM', 'AZ', 'VM', \
                'RO', 'AM', 'AZ', 'VM', 'RO', 'AM', 'AZ', 'VM']

lista_experimentos_com_reposicao = []
lista_experimentos_sem_reposicao = []
cont = 0
N = 100000

for i in range(N):
    vetor_experimento_com_reposicao = np.array([])
    vetor_experimento_sem_reposicao = np.array([])
    vetor_chapeu_copia = []

    for j in range(40):
        vetor_chapeu_copia.append(vetor_chapeu[j])

    for k in range(10):
        x = random.choice(vetor_chapeu)
        y = random.choice(vetor_chapeu_copia)

        vetor_experimento_com_reposicao = np.append(vetor_experimento_com_reposicao, x)
        vetor_experimento_sem_reposicao = np.append(vetor_experimento_sem_reposicao, y)

        vetor_chapeu_copia.remove(x)

    lista_experimentos_com_reposicao.append(vetor_experimento_com_reposicao)
    lista_experimentos_sem_reposicao.append(vetor_experimento_sem_reposicao)

for experimento in lista_experimentos_com_reposicao:
    if(np.count_nonzero(experimento == 'RO') == 2 and np.count_nonzero(experimento == 'AZ') == 2):
        cont += 1

sucessos_com_reposicao = cont
cont = 0

for experimento in lista_experimentos_sem_reposicao:
    if(np.count_nonzero(experimento == 'RO') == 2 and np.count_nonzero(experimento == 'AZ') == 2):
        cont += 1

sucessos_sem_reposicao = cont

print('A probabilidade de se retirar 2 bolas azuis e 2 bolas roxas do chapéu com reposição é ' + str(sucessos_com_reposicao/N) + '.')
print('A probabilidade de se retirar 2 bolas azuis e 2 bolas roxas do chapéu sem reposição é ' + str(sucessos_sem_reposicao/N) + '.')
