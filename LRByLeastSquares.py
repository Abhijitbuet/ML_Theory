'''
Given x = [1, 2, 3]
 and y = [2, 3, 5]
 find w where y = w0 + w1*x
 sensitivity = tp / (tp + fn)
 specificity = tn / (tn + fp)
'''

import numpy as np
import MatrixOperations as math
X = np.array([[1, 1], [1, 2],[1, 3]])

Y = np.array([2, 3, 5])

firstPart = math.inverse(math.multiply(math.transpose(X), X))
secondPart = math.multiply(math.transpose(X), Y)
w = math.multiply(firstPart, secondPart)
print(w)