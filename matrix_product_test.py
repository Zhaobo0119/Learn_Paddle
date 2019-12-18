# -*-coding:utf-8-*-
# 矩阵乘积

import numpy as np

arr_1 = np.array([[1, 2], [3, 4]])
arr_2 = np.array([[5, 6, 7], [8, 9, 10]])

arr = np.dot(arr_1, arr_2)

print(arr)


class Network(object):
    def __init__(self, num_of_weights):
        # 随机产生w的初始值
        # 为了保持程序每次运行结果的一致性，此处设置固定的随机数种子
        np.random.seed(0)
        '''
        生成指定长度的一维数据 ，num_of_weights：数组数据行数 ，1：数组数据列数
        randn函数返回一个或一组样本，具有标准正态分布。
        '''
        self.w = np.random.randn(num_of_weights, 1)


# 1.76405235
net = Network(100)
print('------------net.w---------------' + str(net.w))
