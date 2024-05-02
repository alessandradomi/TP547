import numpy as np
import matplotlib.pyplot as plt

N = 1000000  # numero de amostras

lambda_ij = 256
lambda_pi = 1
lambda_pj = 1

k1 = k2 = 2
eta = 1
R = 2

code_gain_cegnc = 3
code_gain_cedf = 0.5
div_order_cegnc = 4
div_order_cedf = 2

OP_cedt = []
OP_cegnc = []
OP_cedf = []

for a in np.arange(0.001, 0.999, 0.01):  # Diferentes valores de alpha

    h_ij = np.random.exponential(lambda_ij, N)  # |hij|^2
    h_pi = np.random.exponential(lambda_pi, N)  # |hpi|^2
    h_pj = np.random.exponential(lambda_pj, N)  # |hpj|^2

    I_ij = np.log2(1 + 2 * eta * a * h_ij * h_pi / (h_pj * (1 - a)))  # informação mútua

    Prob_cedt = np.sum(I_ij < R / (1 - a)) / N
    Prob_cegnc = code_gain_cegnc * (Prob_cedt ** div_order_cegnc)
    Prob_cedf = code_gain_cedf * (Prob_cedt ** div_order_cedf)

    OP_cedt = np.append(OP_cedt, Prob_cedt)
    OP_cegnc = np.append(OP_cegnc, Prob_cegnc)
    OP_cedf = np.append(OP_cedf, Prob_cedf)

eixo_alpha = np.arange(0.001, 0.999, 0.01)

plt.semilogy(eixo_alpha, OP_cedt, 'r--')
plt.semilogy(eixo_alpha, OP_cegnc, 'b--')
plt.semilogy(eixo_alpha, OP_cedf, 'g--')

plt.grid()
plt.axis([0, 1, 1e-4, 1])
plt.xlabel('alpha')
plt.ylabel('Outage probability')
plt.figlegend(['CEDT', 'CEGNC', 'CEDF'])

plt.show()
