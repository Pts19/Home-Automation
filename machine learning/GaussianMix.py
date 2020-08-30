import numpy as np
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt
# generate random data
np.random.seed(1)
n = 10
y1 = np.random.uniform(0, 10, size=7)
y2 = np.random.uniform(30, 40, size=7)
x1 = [1,2,3,4,5,6,7]
x2 = [1,2,3,4,5,6,7]
x = np.concatenate([x1, x2])
y = np.concatenate([y1, y2])
data = np.vstack([x, y]).T
model = GaussianMixture (n_components=2).fit(data)
model.predict([[2], [1], [1]])
plt.scatter(x, y, c=model.predict(data))
plt.show()