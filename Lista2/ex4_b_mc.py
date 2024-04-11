import numpy as np
import matplotlib.pyplot as plt

N = 1000000

x = np.random.uniform(0, 1, N)  # amostras uniformes

# somatório( 4e^(16x^2  - 12x + 2) )
integral = 4 * sum(np.exp((16 * pow(x, 2) - 12 * x + 2))) / N
print(integral)

# Curva
a = np.linspace(-2, 2, 100)
f = np.exp(a + pow(a, 2))  # e^(x + x^2)
plt.plot(a, f)
plt.fill_between(a, f, color='lightblue')

# Rótulos
plt.text(0, 300, f'Area = {integral:.3f}', fontsize=12)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('e^(x + x^2)')

# Exibir gráfico
plt.show()
