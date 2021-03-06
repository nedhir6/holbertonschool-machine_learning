#!/usr/bin/env python3
"""Function that calculates a correlation matrix"""
import numpy as np


def correlation(C):
    """ C: numpy.ndarray of shape (d, d)
    d: number of dimensions"""
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")
    corr = np.outer(np.sqrt(np.diag(C)), np.sqrt(np.diag(C)))
    return C / corr
