import numpy as np
from numpy import *

def unbiasedSampleVariance(arr):
    xbar = np.mean(arr)
    return np.sum([(x - xbar)**2 for x in arr])/(len(arr)-1)