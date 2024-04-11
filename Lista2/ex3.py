import random

dado = [1, 2, 3, 4, 5, 6]
somas = []
saldo = 1

jogadas = int(input('Jogadas: '))

for jogada in range(jogadas):
    soma = random.choice(dado) + random.choice(dado) + random.choice(dado) + random.choice(dado)

    if soma < 9:
        saldo += 10
    else:
        saldo -= 1

    if saldo == 0:
        print('Você perdeu na ' + str(jogada + 1) + 'ª jogada.')
        break

print('Fim.\nSaldo: ' + str(saldo) + ' reais.')
