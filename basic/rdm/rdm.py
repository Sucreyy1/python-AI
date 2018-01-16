import numpy as np
import numpy.random as random

# 产生一个[0,1)之间的浮点型随机数
num = random.random()
# 按照指定的大小产生[0,1)之间的浮点型随机数array 3x3
random_array = random.random((3, 3))
# 产生10个[1,6)之间的浮点型随机数
num = random.uniform(1, 6, 10)
# 产生10个[1,6)之间的整型随机数
ran = random.randint(1, 6, 10)
# 产生2x5的标准正太分布样本
num = random.normal(size=(5, 2))
# 从ran中有回放的随机采样7个
result = random.choice(ran, 7)
# 从ran中无回放的随机采样7个
result = random.choice(ran, 7, replace=False)

# 数组的计算
arr = random.randn(4, 4)
arr = np.where(arr > 0, 2, arr)
num = random.randint(0, 2, 1000)
draws = np.where(num > 0, 1, -1)
walk = np.cumsum(draws)
