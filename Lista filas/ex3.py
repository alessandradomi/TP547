import numpy as np

lambda1 = 200  # taxa media de chegada
mu1 = 250  # taxa media de serviço
#N = 1 + 1
#N = 5 + 1
#N = 10 + 1
N = 15 + 1

lq = 0  # numero de elementos na fila
ls = 1  # numero de elementos no servidor
PB = 0

k = 0  # variável auxiliar para atendimentos
k1 = 0  # variavel auxiliar para chegadas
k2 = 0  # variavel auxiliar para partidas

chegadas = np.random.exponential(1 / lambda1, 100000)  # vetor de chegadas
partidas = np.random.exponential(1 / mu1, 100000)  # vetor de partidas

tc = [0]  # tempo de chegadas
tp = []  # tempo de partidas
ts = []  # tempo no sistema
n_chegadas = 0

ta = chegadas[k1]  # tempo para proxima chegada
td = partidas[k2]  # tempo para proxima partida
t = np.minimum(ta, td)  # proximo tempo de execucao

while (t < 300):  # tempo limite de simulacao

    if ta < td:  # evento de chegada

        if (ls + lq) < N:

            tc = np.append(tc, t)  # armazena tempo atual de chegada

            if ls == 1:  # servidor ocupado
                lq = lq + 1  # aumenta a fila

            else:  # servidor desocupado
                ls = 1  # ocupa o servidor

                k2 += 1
                td = t + partidas[k2]  # tempo para próxima partida

        else: PB += 1

        n_chegadas += 1
        k1 += 1
        ta = t + chegadas[k1]  # tempo para próxima chegada

    elif ta == td:  # chegada e partida simultanea
        tc = np.append(tc, t)  # armazena o tempo atual de chegada
        tp = np.append(tp, t)  # armazena o tempo atual de partida

        ts = np.append(ts, (tp[k] - tc[k]))  # calcula o tempo no sistema (tempo de partida - tempo de chegada)
        k += 1  # incrementa indice de atendimentos

        k1 += 1
        ta = t + chegadas[k1]  # tempo para próxima chegada

        k2 += 1
        td = t + partidas[k2]  # tempo para próxima partida

    else:  # evento de partida
        tp = np.append(tp, t)  # armazena o tempo atual de partida

        if lq > 0:  # existem pacotes na fila
            lq = lq - 1  # diminuo a fila em 1

            k2 += 1
            td = t + partidas[k2]  # calculo a proxima partida

        else:  # nao ha pacotes na fila
            ls = 0  # esvazia o servidor
            td = np.infty  # tempo da proxima partida muito grande

        ts = np.append(ts, (tp[k] - tc[k]))  # calcula o tempo no sistema (tempo de partida - tempo de chegada)
        k += 1  # incrementa indice de atendimentos

    t = np.minimum(ta, td)  # tempo do próximo evento do processo

tw = np.mean(ts) - 1 / mu1
eq = lambda1 * np.mean(ts)
ew = lambda1 * tw
rho = lambda1 / mu1

print("Comprimento do buffer: " + str(N - 1) + '.')
print("Probabilidade de bloqueio: " + str(PB/n_chegadas) + '.')
print("Número médio de pacotes no sistema: " + str(eq) + '.')
print("Tempo médio no sistema: " + str(np.mean(ts)) + '.')
