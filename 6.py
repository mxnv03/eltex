import matplotlib.pyplot as plt
import numpy as np
from math import pi, e, sqrt

x = np.arange(-10000, 10000, 1, dtype=np.int16)
U = 3
T = 20 * 10 ** (-3)
tt = 2 * 10 ** (-3)
w = 2 * pi / T
Zr2 = 250
Zr3 = 750
Zrn = 100
L = 95 * 10** (-3)
C = 10 * 10 ** (-6)
Ln = 105 * 10 ** (-3)
def Z_c(w):
    return 1/(complex(0, w*(10 * 10**(-6))))
def Z_l(w):
    return complex(0, w*(10 * 10**(-6)))
def ww(w):
    r2 = complex(250, 0)
    r1 = complex(20, 0)
    Zc = Z_c(w)
    Zl = Z_l(w)
    ff = (Zc * (Zl + r2)/((Zl + r2)*Zc + r1*(Zl + r2 + Zc)))
    # return math.atan(ff.imag/ff.real)
    return ff


def func(w):
    if (w == 0):
        return (2*tt)*U
    rr = (U) * (-e ** complex(0, -6 * tt * w) + 2 * e ** complex(0, -5 * tt * w) \
                - 2 * e ** complex(0, -3 * tt * w) + 2 * e ** complex(0, -2 * tt * w) - 1) / complex(0, -w)
    return rr*ww(w)

y = np.array(list(map(func, x)))
y = abs(y)
fig, ax = plt.subplots()
# plt.axis([-10000, 10000, 0, 0.03])
ax.plot(x, y)
ax.legend()
ax.set_xlabel('ω, рад/c')
ax.set_ylabel('S2(ω)')
ax.set_title("График модуля спектральной плотности фрагмента сигнала на выходе схемы.")


plt.show()
