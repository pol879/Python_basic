import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-3.0, 3.5, 0.01)
t = np.arange(-3.0, 4, 1)
sp = plt.subplot(111)
plt.figure(figsize=(10, 5))
plt.plot(x, x**2 - x - 6, t, t**2 - t - 6, 'ro')
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$f(x)$', fontsize=14)
plt.grid(True)
plt.show()
