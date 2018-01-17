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


if __name__ == '__main__':
    population_function()
