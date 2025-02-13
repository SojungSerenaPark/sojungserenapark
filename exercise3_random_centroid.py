#code3 _ random_centroid
#무개중심을 random하게 만들고, dataset의 모양이 (100, 2)이 되도록 만들기. scatter plot로 시각화하기

import numpy as np
import matplotlib.pyplot as plt

center_x = np.random.uniform(-5, 5)
center_y = np.random.uniform(-5, 5)

n_data = 100
x_data = np.random.normal(center_x, 1, (n_data, ))
y_data = np.random.normal(center_y, 1, (n_data, ))

x_data = x_data.reshape(-1, 1)
y_data = y_data.reshape(-1, 1)

data_ = np.hstack([x_data, y_data])

figsize = (10, 10)
fig, ax = plt.subplots(figsize=figsize)

ax.scatter(data_[: , 0], data_[ : , 1])
ax.scatter(center_x, center_y, color='red')

plt.show()