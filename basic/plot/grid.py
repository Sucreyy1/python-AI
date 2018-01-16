import matplotlib.pyplot as plt
import numpy as np

points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
# print(ys)
z = np.sqrt(xs ** 2 + ys ** 2)
plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Image plot of $\sqrt{x^2+y^2}$ for a grid of values')
plt.savefig('grid.png')
plt.show()
