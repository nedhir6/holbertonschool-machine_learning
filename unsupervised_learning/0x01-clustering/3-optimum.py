#!/usr/bin/env python3
""" function that tests for the optimum number of clusters by variance"""
import numpy as np
kmeans = __import__('1-kmeans').kmeans
variance = __import__('2-variance').variance


def optimum_k(X, kmin=1, kmax=None, iterations=1000):
    """ X: numpy.ndarray of shape (n, d) containing the data set
        kmin: integer containing the minimum number of clusters to check for
        kmax: integer containing the maximum number of clusters to check for
        iterations: integer containing the number of iterations for K-means"""
    try:
        results, d_vars = [], []
        Svar = variance(X, kmeans(X, kmin)[0])
        for i in range(kmin, kmax + 1):
            C, clss = kmeans(X, i, iterations)
            results.append((C, clss))
            d_vars.append(Svar - variance(X, C))
        return results, d_vars
    except Exception:
        return None, None