import numpy as np
import matplotlib.pyplot as plt

N = 100000

y = np.random.uniform(0, 1, N)  # amostras uniformes
yg = np.sqrt(y)  # amostras baseadas em g(x)

# somatório( (1 - x) / (8x^4 - 16x^3 + 16x^2 - 8y + 2) )
integral = np.sum((1 - yg) / (8 * pow(yg, 4) - 16 * pow(yg, 3) + 16 * pow(yg, 2) - 8 * yg + 2)) / N
print(f'Integral = {integral:.4f}')

# Curva
a = np.linspace(0, 10, N)
curve_y = a / pow((1 + a ** 2), 2)
plt.plot(a, curve_y, color='black')
plt.fill_between(a, curve_y, color='blue')

# Rótulos
plt.text(5, 0.4, f'Integral = {integral:.4f}', fontsize=12, color='red')
plt.xlim(0, 10)
plt.ylim(0, 0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('x / (1 + x^2)^(2)')

# Exibir gráfico
plt.show()
