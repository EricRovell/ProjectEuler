import matplotlib.pyplot as plt
from math import log10
import seaborn as sns
import numpy as np

x = np.zeros(shape = (100, 100))

for i in range(1, 100):
  for j in range(1, 100):
    x[i, j] = int(log10(i ** j)) + 1

plt.title('Number of digits for a^b')

ax = sns.heatmap(x, cbar=True)
ax.invert_yaxis()
plt.show()
