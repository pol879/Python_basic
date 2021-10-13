import numpy as np
x = [1, 10, 1000]
def slog(n):
    verh = np.e**(1/((np.sin(n)+1)))
    niz = 5/4 + 1/(n**15)
    y = (np.log(verh/niz))/(np.log(1 + n**2))
    return y
for i in x:
    print("y(", i, ")=", slog(i))
