import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, (10, 10))

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

print(len(x))
plt.show()