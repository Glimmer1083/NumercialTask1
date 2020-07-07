import matplotlib.pyplot as plt
import numpy as np

n_dot = 51

x = np.linspace(-1, 1, n_dot)
y = 1 / (25 * np.power(x, 2) + 1)
t = np.linspace(-1, 1, 400)

for n in [6, 12, 18, 24]:
  ax = plt.subplot(2, 2, n / 6)
  p = np.poly1d(np.polyfit(x, y, n))
  ax.plot(t, 1 / (25 * np.power(t, 2) + 1), t, p(t))
  ax.set_title('n = ' + str(n))
  ax.grid(True)

t = np.linspace(-1,1,200)

plt.tight_layout()
plt.savefig('./figs/polyfit.png', dpi=250, format='png')
plt.show()
