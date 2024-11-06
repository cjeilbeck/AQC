import numpy as np

m_adj = np.array([
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]])





def h_mat(M, kappa):
    width = len(M[0])
    h_init = np.zeros(width)

    for k in range(width):
        sum = 0
        for j in range(width):
            sum += M[k,j] + M[j, k]
        h_init[k] = -sum + kappa
    return h_init



