#code4_knn_x_dataset
#4class, class마다 100개의 점을 가지는 dataset 만들기
#-> (400, 2)
#-> class들의 centroid 는 랜덤하게

import matplotlib.pyplot as plt
import numpy as np

n_classes = 4
n_data = 100
data = []
centroids = []
for _ in range(n_classes):
    centroid = np.random.uniform(-10, 10, (2, ))
    data_ = np.random.normal(centroid, 1, (n_data, 2))

    centroids.append(centroid)
    data.append(data_)

centroids = np.vstack(centroids)
data = np.vstack(data)

fig, ax = plt.subplots(figsize=(5, 5))
for class_idx in range(n_classes):
    data_ = data[class_idx * n_data : (class_idx + 1) * n_data]

    ax.scatter(data_[:, 0], data_[:, 1], alpha=0.5)

for centroid in centroids:
    ax.scatter(centroid[0], centroid[1], c='purple', marker='x', s=100)

plt.show()