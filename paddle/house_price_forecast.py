# -*-coding:utf-8-*-
# 波士顿房价预测示例

# 导入需要用到的package
import numpy as np
import json


def load_data():
    # 从文件导入数据
    datafile = 'data/housing.data'
    data = np.fromfile(datafile, sep=' ')
    # 每条数据包括14项，其中前面13项是影响因素，第14项是相应的房屋价格中位数
    feature_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
    # 数组长度
    feature_num = len(feature_names)
    '''
    data.shape:
        在一维数组中 data.shape[0] 代表当前数组的 size
        在二位数组中 data.shape[0] 代表一维数组的 size ，data.shape[1] 代表二维数组中的元素个数
    '''
    print(data.shape[0])
    # 将原始数据进行Reshape，变成[N, 14]这样的形状（即由一维数组变成矩阵，参数 1 为行数 ，参数 2 为 列数）; //:相除 求整数
    data = data.reshape([data.shape[0] // feature_num, feature_num])
    # 将原数据集拆分成训练集和测试集
    # 这里使用80%的数据做训练，20%的数据做测试
    # 测试集和训练集必须是没有交集的
    ratio = 0.8
    # 此时 data 为 矩阵 格式
    # data.shape[0] 506 行数据 ，offset=404行 用于计算数据，剩余的用于测试
    offset = int(data.shape[0] * ratio)
    # 取出前 404 条数据 赋值给  training_data
    training_data = data[:offset]

    '''
    计算train数据集的最大值，最小值，平均值
    axis：为列向 axis=0，axis = 1 时为行方向的最值；
    training_data.max(axis=0) 14 列，每一列里最大的数
    training_data.min(axis=0) 14 列，每一列里最小的数\
    training_data.sum(axis=0) 14 列 ，每一列数字总和
    training_data.shape[0] 数据行数 ==》 404
    '''
    maximums, minimums, avgs = training_data.max(axis=0), training_data.min(axis=0), training_data.sum(axis=0) / training_data.shape[0]
    # 对数据进行归一化处理
    for i in range(feature_num):
        '''
        将所有的数据 506 行 14 列 数据 全部归一化 并赋值到原始位置
        print(maximums[i], minimums[i], avgs[i])
        data[:, i] ：第 i列的所有行数据组成的数组
        avgs[i] ：每列所有行数据平均值
        maximums[i] 每列所有行数据中最大值
        minimums[i] 每列所有行数据中最小值
        : ==> 代表所有行；i：第几列
        '''
        data[:, i] = (data[:, i] - avgs[i]) / (maximums[i] - minimums[i])
        print(data[:, i])
    # 训练集和测试集的划分比例
    training_data = data[:offset]
    # 测试数据
    test_data = data[offset:]
    # 返回结果
    return training_data, test_data


if __name__ == '__main__':
    # 获取数据
    training_data, test_data = load_data()
    '''
    获取 404 行训练数据的前 13 位 特征
    '''
    x = training_data[:, :-1]
    '''
    获取 404 行训练数据的 最后一位 预测值
    '''
    y = training_data[:, -1:]
    # 查看数据
    print('---------训练数据集行数------------' + str(len(training_data)))
    print('---------特征值数组------------' + str(x[0]))
    print('---------预测值数组------------' + str(y[0]))
