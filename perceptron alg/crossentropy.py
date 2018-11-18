import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    centropy = 0
    for value_y, value_p in zip(Y,P):
        centropy += -(value_y * np.log(value_p)) - ((1-value_y)* np.log(1-value_p))
    return centropy

    
OR 

import numpy as np

def cross_entropy(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))