import numpy as np
import matplotlib.pyplot as plt

N = 100000

y = np.random.uniform(0, 1, N)  # amostras uniformes
yg = np.sqrt(y)  # amostras baseadas em g(x)

#somatório( (1 - x^2)^(3/2) / 2x )
integral = np.sum((1 / (2 * yg)) * pow(1 - pow(yg, 2), (3/2))) / N
print(f'Integral = {integral:.4f}')

# Curva
a = np.linspace(0, 1, N)
curve_y = pow((1 - pow(a, 2)), (3 / 2)) # (1 - x^2)^(3/2)
plt.plot(a, curve_y, color='black')
plt.fill_between(a, curve_y, color='blue')

# Rótulos
plt.text(0.5, 0.8, f'Integral = {integral:.4f}', fontsize=12, color='red')
plt.xlim(0, 1)
plt.ylim(0, 1.1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('(1 - x^2)^(3/2)')

# Exibir gráfico
plt.show()
