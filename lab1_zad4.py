import numpy as np
import matplotlib.pyplot as plt
print('Введите функцию от переменной х')
x = np.arange(-10.0, 10.01, 0.01)
y = input()
with plt.xkcd():
    plt.plot(x, eval(y))
    plt.show()
