import numpy as np

list = [[1, 2, 3], [4, 5, 1]]
# 将普通数组转换为 numpy 数组
list = np.asarray(list)
max = list.max(axis=0)
print('-----max------' + str(max))
min = list.min(axis=0)
print('-----min------' + str(min))
sum = list.sum(axis=0)
print('-----sum------' + str(sum))
for i in range(3):
    print(list[:, i])
