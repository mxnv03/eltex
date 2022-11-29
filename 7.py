import matplotlib.pyplot as plt
from math import pi, e, sqrt
import cmath
tt = 2 * 10 ** (-3)
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

U = 3
T = 20 * 10 ** (-3)
def func(k):
    w = k * 314.1593
    if (w == 0):
        return (2*tt)*U
    rr = (U) * (-e ** complex(0, -6 * tt * w) + 2 * e ** complex(0, -5 * tt * w) \
                - 2 * e ** complex(0, -3 * tt * w) + 2 * e ** complex(0, -2 * tt * w) - 1) / complex(0, -w)
    return abs(((rr)/T) * ww(w))
# АЧХ
# plt.axis([0, 10000, 0, 0.6])
# plt.title('График спектра амплитуд сигнала,образованного переодическим продолжением фрагмента сигнала')
plt.title('Спектр амплитуд сигнала на выходе системы')
plt.xlabel('k')
x = [i for i in range(-50, 50, 1)]
y = list(map(func, x))


# y = [abs((1/(Z_ob * math.sqrt(2))) * ((complex(0, 85.5) + 250)/(complex(0, 85.5) + 250 + Z_c(x[i]))) * Z_c(x[i])) for i in range(len(x))]
plt.stem(x, y)
plt.show()