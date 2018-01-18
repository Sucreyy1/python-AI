import pandas as pd
import numpy as np
from pandas import Series, DataFrame

"""
简单统计2015年全国人口分布情况
"""


def population_function():
    path1 = 'D:/data-csv/population.csv'
    population = pd.read_csv(path1, sep=',', encoding='ANSI')
    # 得到数据集的统计信息,包括count,mean,std,min,max等等
    info = population.describe()
    # 得到数据集的行数,列数
    rows = population.shape[0]
    col = population.shape[1]
    # 得到列名
    col_name = population.columns
    # 通过ix这个函数可以选取指定的行和列
    # 得到各省市农村人口
    r_pop = population.ix[:, 2]
    # 得到各省市城市人口
    c_pop = population.ix[:, 1]
    # 人口最多的省份
    new_pop = population.groupby('地区').sum()
    total_pop = new_pop.sum(axis=1)
    # 地区总数
    total_area = population.地区.value_counts().count()
    # 排序(降序)
    population.sort_values(['2015年城市人口', '2015年农村人口'], ascending=False)
    # 列顺序
    population.reindex(columns=['2015年农村人口', '2015年城市人口', '地区'])
    # 强行求个平均
    average_pop = new_pop.mean(axis=1)
    # 选取城市人口超过2000的省份
    city_gt2000 = population[population['2015年城市人口'] > 2000]
    # 查看四川人口情况
    sc_pop = population.ix[population.地区.isin(['四川省']), ['地区', '2015年城市人口', '2015年农村人口']]
    # 将某列设置为日期类型
    # population['2015年农村人口'] = pd.to_datetime(population['2015年农村人口'], format='%Y')
    # 将某列设置为索引
    population.set_index('2015年城市人口', drop=True)
    # 删除xx列
    del population['2015年农村人口']
    # 求出农村人口和城市人口最大值对应的索引
    # 1
    population.ix[:, ['2015年农村人口', '2015年城市人口']].idxmax(0)
    # 2
    new = population.set_index('地区', drop=True)
    new.idxmax(0)


def data_concat():
    raw_data_1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

    raw_data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

    raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
    data1 = pd.DataFrame(raw_data_1, columns=['subject_id', 'first_name', 'last_name'])
    data2 = pd.DataFrame(raw_data_2, columns=['subject_id', 'first_name', 'last_name'])
    data3 = pd.DataFrame(raw_data_3, columns=['subject_id', 'test_id'])
    # 将data1和data2两个数据框按照行的维度就行合并,命名为all_data
    all_data = pd.concat([data1, data2])  # 其实相当于传了一个axis=0
    # 将data1和data2两个数据框按照列的维度进行合并,命名为add_data_col
    all_data_col = pd.concat([data1, data2], axis=1)
    # 按照subject_id的值对all_data和data3进行合并
    pd.merge(all_data, data3, on='subject_id')
    # data1和data2按照subject_id连接(取交集)
    pd.merge(data1, data2, on='subject_id', how='inner')
    # data1和data2按照subject_id连接(取并集,不重叠部分为NaN)
    data4 = pd.merge(data1, data2, on='subject_id', how='outer')
    # 每一列数据缺失总数
    data4.isnull().sum()
    # 每一列完整数据总数
    data4[1] - data4.isnull().sum()
    # 查询指定条件的数据
    data1.query('first_name == "Alex" or last_name == "Aoni"')


if __name__ == '__main__':
    data_concat()
