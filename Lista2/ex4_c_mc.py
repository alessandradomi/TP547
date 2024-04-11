import numpy as np
import matplotlib.pyplot as plt

N = 100000

x = np.random.uniform(0, 1, N)  #amostras uniformes

#somatório( (x - x^2) / (4x^4 - 8x^3 + 8x^2 - 4y + 1) )
integral = np.sum((x - pow(x, 2)) / (4*pow(x, 4) - 8*pow(x, 3) + 8*pow(x, 2) - 4*x + 1)) / N
print(integral)

# Curva
a = np.linspace(0, 10, 1000)
f = a / pow((1 + a ** 2), 2)    #x / (1 + x^2)^2
plt.plot(a, f)  # plotar função
plt.fill_between(a, f, color='lightblue')   #preencher área

# Rótulos
plt.text(5, 0.3, f'Area = {integral:.3f}', fontsize=12)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('x / (1 + x^2)^(2)')

# Exibir gráfico
plt.show()
