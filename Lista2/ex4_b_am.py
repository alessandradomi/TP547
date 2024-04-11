import numpy as np
import matplotlib.pyplot as plt

N = 100000

y = np.random.uniform(0, 1, N)  # amostras uniformes
yg = np.sqrt(y)  # amostras baseadas em g(x)

# somatório( 2e^(16x^2 - 12x + 2) / x )
integral = np.sum((2 / yg) * np.exp(16 * pow(yg, 2) - 12 * yg + 2)) / N
print(f'Integral = {integral:.4f}')

# Curva
a = np.linspace(-2, 2, N)
curve_y = np.exp(a + pow(a, 2))  # (e^(x + x^2)
plt.plot(a, curve_y, color='black')
plt.fill_between(a, curve_y, color='blue')

# Rótulos
plt.text(0, 300, f'Integral = {integral:.4f}', fontsize=12, color='red')
plt.xlim(-2, 2)
plt.ylim(0, 500)
plt.xlabel('x')
plt.ylabel('y')
plt.title('e^(x + x^2)')

# Exibir gráfico
plt.show()
