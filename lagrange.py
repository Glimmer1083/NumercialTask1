#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
import math

# 选择函数
func = input("""Please select the function: 
1. fx = 1/(1 + 25 * x^2)
2. fx = x/(1 + x^4)
3. fx = arctan(x)
""")

# 定义拉格朗日函数：计算在xx、yy为插值节点条件下的拉格朗日多项式函数值
def lagrange(x, xx, yy):
  ny = 0
  for i in range(xx.size):
    l = 1
    for j in range(xx.size):
      if xx[i] != xx[j]:
        l = ((x - xx[j]) / (xx[i] - xx[j])) * l
    ny = yy[i] * l + ny
  return ny

# 定义函数1
def f1(x):
  return 1 / (25 * np.power(x, 2) + 1)

# 定义函数2
def f2(x):
  return x / (np.power(x, 4) + 1)

# 定义函数3
def f3(x):
  return np.arctan(x)

# 画出图像
def lagrangeplot(xx, f, n, type):
  if type == 'equal':
    x = np.linspace(xx.min(), xx.max(), n + 1)
  else:
    k = np.linspace(1, n + 1, n + 1, endpoint=True); 
    x = (xx.max() + xx.min()) / 2 + \
        (xx.max() - xx.min()) / 2 * np.cos((2 * k - 1) * math.pi / (2 * (n + 1)))
  y = f(x); yy = f(xx); ny = np.zeros(xx.size)
  for i in range(xx.size):
    ny[i] = lagrange(xx[i], x, y)
  ax = plt.subplot(2, 2, n / 3)
  ax.plot(xx, ny, label=type)
  ax.plot(xx, yy, label="origin")
  ax.set_title('n = ' + str(n) )
  plt.grid(True, linestyle='--')
  plt.legend(loc=4)
  return ny

# 主函数
if __name__ == "__main__":
  if func == '1':
    for t in ['equal', 'chebyshev']:
      fig = plt.figure(figsize=(8,6))
      for n in [3, 6, 9, 12]:
        xx = np.linspace(-1, 1, 1000, endpoint=True)
        lagrangeplot(xx, f1, n, type=t)
      fig.tight_layout()
      fig.savefig('./figs/lagrange_' + func + t + '.png', dpi=250, format='png')
  elif func == '2':
    for t in ['equal', 'chebyshev']:
      fig = plt.figure(figsize=(8,6))
      for n in [3, 6, 9, 12]:
        xx = np.linspace(-5, 5, 1000, endpoint=True)
        lagrangeplot(xx, f2, n, type=t)
      fig.tight_layout()
      fig.savefig('./figs/lagrange_' + func + t + '.png', dpi=250, format='png')
  else:
    for t in ['equal', 'chebyshev']:
      fig = plt.figure(figsize=(8,6))
      for n in [3, 6, 9, 12]:
        xx = np.linspace(-5, 5, 1000, endpoint=True)
        lagrangeplot(xx, f3, n, type=t)
      fig.tight_layout()
      fig.savefig('./figs/lagrange_' + func + t + '.png', dpi=250, format='png')
  
  plt.show()