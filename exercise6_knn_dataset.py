#code6_knn_dataset
#4개의 class(0, 1, 2, 3) 을 가지는 dataset 만들기
# x: (400,2)
# y: (400, )

import numpy as np

n_classes = 4
n_data = 100

x, y = [], []

for class_idx in range(n_classes):
    centroid = np.random.uniform(-10, 10, (2, ))
    x_ = np.random.normal(centroid, 2, size=(n_data, 2))
    y_ = class_idx * np.ones(n_data, )

    x.append(x_); y.append(y_)

print(y_.shape)

x = np.vstack(x)
y = np.hstack(y)

print(x.shape, y.shape)