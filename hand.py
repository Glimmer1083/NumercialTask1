import numpy as np, matplotlib.pyplot as plt
from scipy.interpolate import *

# 读取手的数据
data = np.loadtxt('hand.txt',dtype=np.float32)

x = data[:, 0]
y = data[:, 1]

# 二次独立插值并画出图像
fig, ax1 = plt.subplots()
fx = interp1d(range(1, x.size + 1), x, 'cubic')
fy = interp1d(range(1, x.size + 1), y, 'cubic')
pp = np.linspace(1, x.size, 1000, endpoint=False)
ax1.plot(fx(pp), fy(pp), label='cubic')
ax1.scatter(x, y, label='origin')
ax1.legend()
ax1.set_title('hand')
fig.savefig('./figs/hand.png', dpi=250, format='png')
plt.show()
