import numpy as np
import numpy.linalg as lg

np_arrayA = np.array([[1, 2],
                      [0, 3]])

np_arrayB = np.array([[2, 6],
                      [3, 5]])
# 基本运算
# 绝对值
np.abs(-1)
# sin函数
np.sin(np.pi / 2)
# e为底的指数函数
np.exp(3)
# 2的3次方
np.power(2, 3)
# 矩阵点乘
np_arrayC = np.dot(np_arrayA, np_arrayB)
# 开方
np.sqrt(25)
# 求和
np.sum([1, 2, 3, 4])
# 求平均值
np.mean([1, 2, 3, 4])
# 方差
var = np.var(np_arrayA)
# 标准差
std = np.std(np_arrayA)

# 线性代数模块
# 求矩阵的迹
np.trace(np_arrayA)
# 请行列式的值
result_arrayA = lg.det(np_arrayA)
# 矩阵的秩
rank = lg.matrix_rank(np_arrayA)
