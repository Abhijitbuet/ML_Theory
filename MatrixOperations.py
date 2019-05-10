import numpy as np
from scipy.stats import multivariate_normal


def multiply(a, b):
    c = np.matmul(a, b)
    return c


def transpose(a):
    return a.transpose()


def inverse(a):
    return np.linalg.inv(a)


def determinant(a):
    return np.linalg.det(a)


def eigen_values(a):
    return np.linalg.eig(a)


def norm_with_order(a, order):
    return np.linalg.norm(a, ord=order)


def norm(a):
    return np.linalg.norm(a)


def trace(a):
    return np.trace(a)


def covariance(a):
    return np.cov(a)


def variance(a):
    return np.var(a)


def mean(a):
    return np.mean(a)


a = np.array([[2, 2, 2], [0, 3, 3], [2, 1, 3]])
b = np.array([[4, 1], [2, 2]])
c = mean(a)

covariance = covariance(a)


