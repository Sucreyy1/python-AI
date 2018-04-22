from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# Series
arr = np.arange(0, 3)
s1 = Series(arr, index=('a', 'b', 'c'))
s1.name = 'test'
s1.index.name = 'index-test'
s2 = s1.reindex(['a', 'c', 'd'], fill_value=0)
obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj3 = obj3.reindex(range(6), method='ffill')

# DataFrame
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data, columns=['year', 'state', 'pop'])
# 列索引
# print(frame.year)
print(frame['year'])
# 行索引
line = frame.ix[0, 'year']

# for index, value in ['1', '2', '3']:
#     print(index, value)

i = 1
print(i + 1)

if __name__ == '__main__':
    x = [[1, 2, 3],
         [4, 5, 6]]
    y = [1,
         -1]
    for a, b in zip(x, y):
        print(a, b)
        print('-----')
