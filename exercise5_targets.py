#code5_targets

# 모든값이 0, 모양이 (100,)인 ndarray,
# 모든값이 1, 모양이 (100,)인 ndarray,
# 모든값이 2, 모양이 (100,)인 ndarray,
# 모든값이 3, 모양이 (100,)인 ndarray,
# 연결해서 (400, ) ndarray로 만들기


import numpy as np

#method.1
a = np.zeros(shape=(100, ))
b = np.ones(shape=(100, ))
c = np.full(shape=(100, ), fill_value=2)
d = np.full(shape=(100, ), fill_value=3)

concatenated = np.concatenate((a, b, c, d))

print(f"concatenated: {concatenated.shape}\n{concatenated}")


#method.2

n_classes = 4
n_data = 100

data = []
for class_idx in range(n_classes):
    data_ = class_idx * np.ones(n_data, )
    data.append(data_)
data = np.hstack(data)
# data = np.concatenate(data)

print(data.shape)


#method.3

n_classes = 4
n_data = 100

data = []
for class_idx in range(n_classes):
    data_ = np.full(shape=(n_data, ), fill_value=class_idx)
    data.append(data_)
data = np.hstack(data)
# data = np.concatenate(data)

print(data.shape)
