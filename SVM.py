import numpy as np
from sklearn.svm import SVC, LinearSVC

X = np.array([[2, 1], [2, -1], [2, 3], [2, 5], [4, 0], [4, 1], [4, -1], [4, 5]])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

clf = SVC()
clf.fit(X, y)

print(clf.predict([[3, 3]]))
print(clf.intercept_)
print(clf._get_coef())
