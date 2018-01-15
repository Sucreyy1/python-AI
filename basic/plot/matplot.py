import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
"""
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
"""
# 通过rcParams设置全局横纵轴字体大小
mpl.rcParams['xtick.labelsize'] = 24
mpl.rcParams['ytick.labelsize'] = 24

# x轴的采样点
x = np.linspace(0, 5, 100)
# 通过下面曲线加上噪声生成数据，所以拟合模型就用y了……
y = 2 * np.sin(x) + 0.3 * x ** 2
y_data = y + np.random.normal(scale=0.3, size=100)

# figure()指定图表名称
plt.figure('data')

# '.'表明画散点图,每个散点的形状是个圆
plt.plot(x, y_data, '.')

# 画模型的图,plot函数默认画连线图
plt.figure('model')
plt.plot(x, y)

# 两个图画一起
plt.figure('data & model')

# 通过'k'指定线的颜色，lw指定线的宽度
# 第三个参数除了颜色也可以指定线形，比如'r--'表示红色虚线
# 更多属性可以参考官网：http://matplotlib.org/api/pyplot_api.html
plt.plot(x, y, c='k', lw=3)

# scatter可以更容易生成散点图
plt.scatter(x, y_data)
plt.savefig('./result.png')
plt.show()
