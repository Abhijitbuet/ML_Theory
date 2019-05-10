import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

randomMatrix = np.array([[.4173, .4893], [.0497, .3377], [.9027, 0.9001], [.9448, .3692], [.6, .2]])
linked = linkage(randomMatrix, 'complete')

labelList = ['1','2','3','4','5']

plt.figure(figsize=(8, 8))
dendrogram(
            linked,
            orientation='top',
            labels=labelList,
            distance_sort='descending',
            show_leaf_counts=False
          )
plt.show()