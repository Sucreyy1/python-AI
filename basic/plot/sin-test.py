import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 0.02)
y = np.sin(x)

# sin图像
plt.figure('sin')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.xlim(-10, 10)
plt.ylim(-1, 1)
# y轴0点
plt.figure('y axis')
line_x = x
line_y = 0 * line_x
# x轴0点
plt.figure('x axis')
line_x1 = 0 * x
line_y1 = np.sin(line_x)
# 作图
plt.plot(line_x, line_y, 'r-', x, y, 'g-', line_x1, line_y1, 'y-')
plt.title('sin图像')
plt.savefig('sin.png')
plt.show()
