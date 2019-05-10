from sklearn.neighbors import KNeighborsClassifier
X = [[0, 0], [0, 1], [2, 5], [3,5]]
y = [0, 0, 1, 1]
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X, y)
print(classifier)
print(classifier.predict(X))
print(classifier.predict([[0, 2]]))