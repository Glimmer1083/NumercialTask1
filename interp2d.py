import numpy as np, matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from scipy.interpolate import interp2d

# 录入数据
t = np.linspace(100, 400, 4)
domain = np.meshgrid(t, t)
X, Y = domain
Z = np.array([[636, 697, 624, 478], [698, 712, 630, 478], [680, 674, 598, 412], [662, 626, 552, 334]])

# 插值并画出等值线、云图和三维图
fig = plt.figure(figsize=(10,8))

# 未插值前
ax1 = plt.subplot2grid((2,2), (0,0), aspect='equal')
p = ax1.pcolor(X, Y, Z)
fig.colorbar(p)
CP = ax1.contour(X, Y, Z, colors='k')
ax1.clabel(CP)
ax1.set_title('(a)  Contour plot')

ax2 = plt.subplot2grid((2,2), (0,1), projection='3d')
ax2.plot_surface(X, Y, Z, alpha=1)
ax2.scatter(X, Y, Z, s=25)
ax2.set_title('(b)  Surface plot')
fig.tight_layout()

# 获取网格数据
tt = np.linspace(100, 400, 301)
XX, YY = np.meshgrid(tt, tt)
interpolant = interp2d(X, Y, Z, kind='cubic')

# 插值后
ax3 = plt.subplot2grid((2,2), (1,0), aspect='equal')
p = ax3.pcolor(XX, YY, interpolant(tt,tt))
fig.colorbar(p)
CP = ax1.contour(X, Y, Z, colors='k')
ax3.clabel(CP)
ax3.set_title('(c)  Contour plot')

ax4 = plt.subplot2grid((2,2), (1,1), projection='3d')
ax4.plot_surface(XX, YY, interpolant(tt, tt), alpha=1)
ax4.clabel(CP)
ax4.set_title('(d)  Cubic Surface Plot')
ZZ = interpolant(tt, tt)

#查找最大值的索引
m, n = ZZ.shape
index = int(ZZ.argmax())
x = int(index / n)
y = index % n
print('index: {}, {}.'.format(100 + x, 100 + y))
print('max height: {}.'.format(ZZ[x, y]))

# 保存图像
plt.tight_layout()
plt.savefig('./figs/interp2d.png', format='png', dpi=250)
plt.show()
