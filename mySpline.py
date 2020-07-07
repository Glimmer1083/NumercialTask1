import numpy as np, matplotlib.pyplot as plt
from scipy.interpolate import *

# 读取数据
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([0, 0.79, 1.53, 2.19, 2.71, 3.03, 3.27, 2.89, 3.06, 3.19, 3.29])

# 样条插值函数
def mySpline(x, y, xx):
  # 定义端点导数值
  m0 = 0.8; mn = 0.2
  d = np.zeros(x.size); mu = np.zeros(x.size); lam = np.zeros(x.size); beta = np.zeros(x.size)
  M = np.zeros(x.size); tmp = np.zeros(x.size)
  
  # 依次计算系数
  lam[0] = 1; mu[x.size - 1] = 1
  d[0] = 6 * ((y[1] - y[0]) / (x[1] - x[0]) - m0) / (x[1] - x[0])
  d[x.size - 1] = 6 * (mn - (y[x.size - 1] - y[x.size - 2]) / (x[x.size - 1] - x[x.size - 2])) / (x[x.size - 1] - x[x.size - 2])
  for i in range(1, x.size - 1):
    mu[i] = (x[i] - x[i - 1]) / (x[i + 1] - x[i - 1])
    lam[i] = (x[i + 1] - x[i]) / (x[i + 1] - x[i - 1])
    d[i] = 6 * (((y[i + 1] - y[i]) / (x[i + 1] - x[i])) - ((y[i] - y[i - 1]) / (x[i] - x[i - 1]))) / (x[i + 1] - x[i - 1])
  
  # 追赶法求解
  beta[0] = lam[0] / 2; tmp[0] = d[0] / 2
  for i in range(1, x.size):
    beta[i] = lam[i] / (2 - mu[i] * beta[i - 1])
    tmp[i] = (d[i] - mu[i] * tmp[i - 1]) / (2 - mu[i] * beta[i - 1])
  
  M[x.size - 1] = tmp[x.size - 1]
  for i in range(x.size - 1):
    M[x.size - i - 2] = tmp[x.size - i - 2] - beta[x.size - i - 2] * M[x.size - i - 1]
  
  # 计算函数值
  for i in range(x.size - 1):
    if xx > x[i] and xx <= x[i + 1] :
      ny =  M[i] * (x[i + 1] - xx)**3 / (6 * (x[i + 1] - x[i])) + \
            M[i + 1] * (xx - x[i])**3 / (6 * (x[i + 1] - x[i])) + \
            (y[i] - M[i] * (x[i + 1] - x[i])**2 / 6) * (x[i + 1] - xx) / (x[i + 1] - x[i]) + \
            (y[i + 1] - M[i + 1] * (x[i + 1] - x[i])**2 / 6) * (xx - x[i]) / (x[i + 1] - x[i])
      break
  return ny

# 画图像
xx = np.linspace(x.min()+0.0001, x.max(), 1000)
yy = np.zeros(xx.size)
for i in range(xx.size):
  yy[i] = mySpline(x, y, xx[i])

ipo3 = splrep(x, y, k=3)
iy3 = splev(xx, ipo3)
f = interp1d(x, y, 'cubic')

fig = plt.figure(figsize=(8,4))
ax1 = plt.subplot(1, 2, 1)
ax1.plot(xx, iy3, label='cubic_scipy')
ax1.plot(xx, yy, label='my')
ax1.scatter(x, y, label='origin')
ax1.legend(loc=4)
ax1.set_title('mySpline')
ax1.grid(True)

ax2 = plt.subplot(1, 2, 2)
ax2.plot(xx, f(xx) - yy)
ax2.set_title('diff with sci-py')
ax2.grid(True)
plt.tight_layout()

fig.savefig('./figs/mySpline.png', dpi=250, format='png')
plt.show()
