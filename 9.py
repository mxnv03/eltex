import matplotlib.pyplot as plt
from math import pi, e, sqrt, exp
import numpy as np
import cmath
tt = 2 * 10 ** (-3)
T = 20e-3
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

def gg(x):
    p1 = -3225.4157
    p2 = -4407.1633
    return p1 * 0.7772523 * exp(p1 * x) + p2 * (-1.703178142216918) * exp(p2 * x)

def g1(x):
    p1 = -3225.4157
    p2 = -4407.1633
    return 25/27+0.7772523*exp(p1*x)-1.703178142216918*exp(p2*x)
U = 3
def f_s(t):
    if t<=tt:
        return U*(gg(t))
    if t<=3*tt:
        return -U * (gg(t)-2*gg(t-tt))
    if t<=4*tt:
        return U * (gg(t)-2*gg(t-tt)+2*gg(t-3*tt))
    if t<=5*tt:
        return U * (gg(t)-2*gg(t-tt)+2*gg(t-3*tt)-2*gg(t-4*tt))
    if t<=6*tt:
        return -U * (gg(t)-2*gg(t-tt)+2*gg(t-3*tt)-2*gg(t-4*tt)+2*gg(t-5*tt))
    return U * (gg(t)-2*gg(t-tt)+2*gg(t-3*tt)-2*gg(t-4*tt)+2*gg(t-5*tt)-gg(t-6*tt))
def f_s1(t):
    if t<=tt:
        return U
    if t<=3*tt:
        return -U
    if t<=4*tt:
        return U
    if t<=5*tt:
        return U
    if t<=6*tt:
        return -U
    return 0

x = np.arange(0, T, 1e-6)
g = np.array(list(map(f_s, x)))
plt.title('График переходной характеристики')
plt.title('График импульсной характеристики')
plt.title('Фрагмент передаваемого сигнала')
plt.xlabel('t, c')
plt.ylabel('u(t), B')
plt.plot(x, g)
plt.show()
# U = 3
# T = 20 * 10 ** (-3)
# def func(k):
#     w = k * 314.1593
#     if (w == 0):
#         return (2*tt)*U
#     rr = (U) * (-e ** complex(0, -6 * tt * w) + 2 * e ** complex(0, -5 * tt * w) \
#                 - 2 * e ** complex(0, -3 * tt * w) + 2 * e ** complex(0, -2 * tt * w) - 1) / complex(0, -w)
#     return abs(((rr)/T) * ww(w))
# # АЧХ
# # plt.axis([0, 10000, 0, 0.6])
# # plt.title('График спектра амплитуд сигнала,образованного переодическим продолжением фрагмента сигнала')
# plt.title('Спектр амплитуд сигнала на выходе системы')
# plt.xlabel('k')
# x = [i for i in range(-50, 50, 1)]
# y = list(map(func, x))