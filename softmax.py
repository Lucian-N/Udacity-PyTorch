import numpy as np
import math


# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    denominator = [math.exp(value) for value in L]
    denominator = sum(denominator)
    p_values = [math.exp(value) / denominator for value in L]
    return p_values