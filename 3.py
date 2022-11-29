import matplotlib.pyplot as plt
import numpy as np
from math import pi, e

x = np.arange(-10000, 10000, 1)
U = 3
T = 20 * 10 ** (-3)
tt = 2 * 10 ** (-3)
w = 2 * pi / T


def func(w):
    if (w == 0):
        return 2*tt*U
    rr = (U) * (-e ** complex(0, -6 * tt * w) + 2 * e ** complex(0, -5 * tt * w) \
                - 2 * e ** complex(0, -3 * tt * w) + 2 * e ** complex(0, -2 * tt * w) - 1) / complex(0, -w)
    return abs(rr)


y = np.array(list(map(func, x)))
fig, ax = plt.subplots()
plt.axis([-10000, 10000, 0, 0.025])
ax.plot(x, y, linewidth=0.5)
ax.legend()
ax.set_xlabel('ω, рад/c')
ax.set_ylabel('S1(ω)')
ax.set_title("График модуля спектральной плотности фрагмента сигнала.")

plt.show()