import numpy as np
import matplotlib.pyplot as plt

from numpy.core.multiarray import ndarray

count = 0

for i in range(1000000):
	
	x: ndarray = np.random.random()
	y: ndarray = np.random.random()

	if x ** 2 + y ** 2 < 1:
		count += 1

print(count * 4 / 1000000)

c1 = plt.Circle((0, 0), radius=1, fc="None", ec="r", linewidth=3)
ax = plt.gca()
ax.add_patch(c1)

plt.axis("scaled")
plt.xlim(0, 1)
plt.ylim(0, 1)

x = np.random.rand(1000)
y = np.random.rand(1000)
plt.scatter(x, y, marker="x")
plt.show()
