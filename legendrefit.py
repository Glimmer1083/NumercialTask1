import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import math
import leastsqSample

# 返回n次勒让德函数函数值
def legendre(x, n):
  if n == 0:
    return 1
  elif n == 1:
    return x
  else: 
    return ((2 * n - 1) * x * legendre(x, n - 1) - (n - 1) * legendre(x, n - 2)) / n
    
def f(x, n):
  return math.exp(x) * legendre(x, n)

# 正交函数本身做内积（可以用正交性简化）
def phiq(x, n):
  return legendre(x, n) ** 2

def legendrefit(x, n):
  yy = np.zeros(x.size)
  for i in range(x.size):
    for nn in range(n):
      yy[i] += integrate.quad(f, -1, 1, args = (nn))[0] / integrate.quad(phiq, -1, 1, args = (nn))[0] * legendre(x[i], nn)  # 求解系数
  return yy

def err(p, x, y):
  return p[0] * np.exp(x * p[1]) - y


if __name__ == "__main__":
  x = np.linspace(-1, 1, 101)
  y = np.exp(x)
  En = np.zeros(11)
  fig = plt.figure(figsize=(12,5))
  ax1 = plt.subplot(1, 2, 1)
  for i in range(11):
    yy = legendrefit(x, i)
    En[i] = abs(yy - y).max()
    ax1.plot(x, abs(yy - y), label="n = " + str(i), linewidth=2)
  ax1.set_title('legendrefit err')
  ax1.legend()
  
  ax2 = plt.subplot(1, 2, 2)
  ax2.scatter(range(11), En, label="En",linewidth=2)
  ax2.set_title('legendrefit err max')
  ax1.grid(True); ax2.grid(True)
  fig.savefig('./figs/legendrefit.png', dpi=250, format='png')

  n = np.array(range(11))

  fig2 = leastsqSample.leastsqfit(n, En, err, [1,1])
  fig2.savefig('./figs/legendrefitleastsq.png', dpi=250, format='png')

  plt.show()
