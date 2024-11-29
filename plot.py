import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6])
y = [1, 1.42, 1.76, 2, 2.24, 2.5])
p, v = np.polyfit(x, y, deg=1)

print(v)
print(p)
print(type(p), type(v))
plt.plot(x, float() * y + float(v), x, y, 'bs')
plt.show()
