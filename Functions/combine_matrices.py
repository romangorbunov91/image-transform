import numpy as np

# PyWavelet approah.
def combine_matrices(cA, cH, cV, cD):
    top_row = np.hstack((cA, cH))
    bottom_row = np.hstack((cV, cD))
    return np.vstack((top_row, bottom_row))