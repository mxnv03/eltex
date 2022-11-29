import matplotlib.pyplot as plt
import math
import cmath
# ---------- 2 ----------
plt.axis([0, 400, 0, 0.6*10**(-2)])
plt.title('Зависимость мощности P от сопротивления R')
plt.xlabel('R, Ом')
plt.ylabel('P, Вт')
# x = []
# i = 0.0
# while i <= 400:
#     x.append(i)
#     i += 0.0001

# max_r = -10
# max_p = - 10
# for i in range(len(x)):
#     p = abs(((complex(0.646, 0.093))**2 * x[i])/((x[i]+complex(18.278, 2.652))**2))
#     if p > max_p:
#         max_p = p
#         max_r = x[i]
# print(max_p, max_r)

x = [i for i in range(0, 400, 1)]
y = [abs(((complex(0.646, 0.093))**2 * x[i])/((x[i]+complex(18.278, 2.652))**2)) for i in range(len(x))]
plt.plot(y)
plt.show()