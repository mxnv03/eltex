import matplotlib.pyplot as plt
import math
import cmath
# ---------- 2 ----------
# plt.axis([0, 400, 0, 0.6*10**(-2)])
# plt.title('Зависимость мощности P от сопротивления R')
# plt.xlabel('R, Ом')
# plt.ylabel('P, Вт')
# x = []
# i = 0.0
# while i <= 400:
#     x.append(i)
#     i += 0.0001
#
# max_r = -10
# max_p = - 10
# for i in range(len(x)):
#     p = abs(((0.646-0.093j)**2 * x[i])/((x[i]+18.278-2.652j)**2))
#     if p > max_p:
#         max_p = p
#         max_r = x[i]
# print(max_p, max_r)
#
# # x = [i for i in range(0, 400, 0.01)]
# y = [abs(((0.646-0.093j)**2 * x[i])/((x[i]+18.278-2.652j)**2)) for i in range(len(x))]
# print(max(y))
# plt.plot(y)
# plt.show()

# ---------- 3 ----------
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
    #y.append(math.atan(ff.imag/ff.real))
# АЧХ
# plt.axis([0, 10000, 0, 0.6])
plt.title('График ФЧХ')
plt.xlabel('w, рад/c')
x = [i for i in range(1, 30000, 1)]
y = list(map(ww, x))


# y = [abs((1/(Z_ob * math.sqrt(2))) * ((complex(0, 85.5) + 250)/(complex(0, 85.5) + 250 + Z_c(x[i]))) * Z_c(x[i])) for i in range(len(x))]
plt.plot(x, y)
plt.show()


# ФЧХ
# plt.axis([0, 10000, 0, 1.6])
# Z_ob = complex(68.86, 106.096)
#
# plt.title('График АЧХ')
# plt.xlabel('w, рад/c')
# x = [i for i in range(1, 10000, 1)]
# y = [complex((abs((1/(Z_ob * math.sqrt(2))) * ((complex(0, 85.5) + 250)/(complex(0, 85.5) + 250 + Z_c(x[i]))) * Z_c(x[i])))) for i in range(len(x))]
# h2 = [math.atan(y[i].imag/y[i].real) for i in range(len(y))]
# print(y[0])
# print(y[13].imag)
# plt.plot(h2)
# plt.show()

# from scipy.integrate import quad
#
# def integrand(x, a, b, w):
#     return cmath.polar(3 * math.e**(-1j*w*x))
#
# plt.axis([0, 10000, 0, 0.2])
#
# plt.title('График модуля спектральной плотности')
# plt.xlabel('w, рад/c')
# x = [i for i in range(1, 10000, 1)]
# y = [quad(integrand, 0, 6*0.002, args=(x[i]))[0] for i in range(len(x))]
# plt.plot(y)
# plt.show()