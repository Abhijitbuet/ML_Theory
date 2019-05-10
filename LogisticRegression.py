from sklearn.linear_model import LogisticRegression
'''
multi_class : str, {‘ovr’, ‘multinomial’, ‘auto’}
'''
X = [[0, 0], [0, 1], [2, 5], [3,5]]
y = [0, 0, 1, 1]
clf = LogisticRegression(random_state=0, solver='lbfgs',  multi_class='multinomial').fit(X, y)
print(clf.predict([[0,0.5]]))
print(clf.predict_proba([[0,0.5]]))
print(clf.score(X, y))