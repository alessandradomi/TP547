import numpy as np
import matplotlib.pyplot as plt

N = 100000

x = np.random.uniform(0, 1, N)  # amostras uniformes

# somatório( (1 - x^2)^(3/2) )
integral = sum(pow((1 - pow(x, 2)), (3 / 2))) / N
print(integral)

# Curva
a = np.linspace(0, 1, 1000)
f = pow((1 - a ** 2), (3 / 2))  # (1 - x^2)^(3/2)
plt.plot(a, f)
plt.fill_between(a, f, color='lightblue')

# Rótulos
plt.text(0.5, 0.8, f'Area = {integral:.3f}', fontsize=12)  # area value
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('(1 - x^2)^(3/2)')

# Exibir gráfico
plt.show()
