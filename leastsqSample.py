import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
import math

# 定义最小二乘拟合函数、画图
def leastsqfit(x, y, err, p0):
  ret = leastsq(err, p0, args = (x, y))  
  a, b = ret[0]
  xx = np.linspace(x.min(), x.max(), 201)
  yy = a * np.exp(b * xx)
  ybar = a * np.exp(b * x)
  fig1 = plt.figure(figsize=(8, 8))
  ax1 = plt.subplot(2,1,1)
  ax1.scatter(x, y, color="red", label="Sample Point", linewidth=3)
  ax1.plot(xx, yy, color="orange", label="Fitting Line",linewidth=2)
  ax1.legend()
  ax1.set_title('LeastSQ')
  ax1.grid(True)
  ax2 = plt.subplot(2,1,2)
  index = np.arange(x.size)
  values = ybar - y
  ax2.bar(index, values)
  ax2.set_title('Error Bar')
  ax2.grid(True)
  
  # 求均方误差
  sum = 0
  for error in values:
    sum += error ** 2
  print('The MSE is {}, a is {}, b is {}.'.format(sum / values.size, a, b))

  return fig1

# 定义误差函数
def err(p, x, y):
  return p[0] * np.exp(x * p[1]) - y


if __name__ == "__main__":
  # 读取数据
  data = np.loadtxt('leastsqdata.txt', dtype=np.float32)
  data2 = np.transpose(np.loadtxt('leastsqdata2.txt', dtype=np.float32))
  x = data[:, 0]; x2 = data2[:, 0]
  y = data[:, 1]; y2 = data2[:, 1]
  # 初始系数
  p0 = [1, 1]
  fig1 = leastsqfit(x, y, err, p0)
  fig1.savefig('./figs/leastsq.png', format='png', dpi=250)
  fig2 = leastsqfit(x2, y2, err, p0)
  fig2.savefig('./figs/leastsq2.png', format='png', dpi=250)
  plt.show()