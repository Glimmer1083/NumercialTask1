import scipy.interpolate
import numpy as np, matplotlib.pyplot as plt
from scipy.interpolate import *

# 数据初始化
x = np.linspace(-1, 1, 11, endpoint=True) #插值节点
y = 1 / (25 * np.power(x,2) + 1)
xx = np.linspace(x.min(), x.max(), 1000) #绘制图像用到的点

# 画图
fig = plt.figure(figsize=(8,4))
for n in [3, 6, 9, 12]:
  x = np.linspace(-1, 1, n + 1, endpoint=True)
  y = 1 / (25 * np.power(x,2) + 1)
  f = interp1d(x, y, 'cubic')  #样条插值
  ax = plt.subplot(2, 2, n / 3)
  ax.plot(xx, 1 / (25 * np.power(xx, 2) + 1), label='origin')
  ax.plot(xx, f(xx), label='cubic')  
  ax.plot(xx, lagrange(x, y)(xx), label='lagrange')  #拉格朗日插值
  ax.legend(loc=4); ax.set_title('n = ' + str(n)); ax.grid(True)
fig.tight_layout()
fig.savefig('./figs/lagrangeVssp.png', dpi=250, format='png')
plt.show()
