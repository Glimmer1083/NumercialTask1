import matplotlib.pyplot as plt
import numpy as np

n_dot = 31


def f(x):
  return 1 + x + np.power(x, 2) + np.power(x, 3) + np.power(x, 4) + np.power(x, 5)
x = np.linspace(0, 1, n_dot)
y = f(x)
t = np.linspace(0, 1, 201)

for n in [5, 10, 15, 20]:
  ax = plt.subplot(2, 2, n / 5)
  p = np.poly1d(np.polyfit(x, y, n))
  ax.plot(t, f(t) - p(t))
  ax.set_title('n = ' + str(n))
  ax.grid(True)

plt.tight_layout()
plt.savefig('./figs/polyfit2.png', dpi=250, format='png')
plt.show()
