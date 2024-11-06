import numpy as np
X = np.array([[0, 1], [1, 0]])
Y = np.array([[0, -1j], [1j, 0]])
Z = np.array([[1, 0], [0, -1]])
I = np.eye(2)

#def of tensor operation


def pauli(n, J, dimension):
    new = 1  
    for i in range(1, n+1):
        if i == J:
            new = np.kron(new, dimension)  
        else:
            new = np.kron(new, I) 
    return new

  


