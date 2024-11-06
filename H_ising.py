

from PAULI_DEF import pauli, X, Y, Z, I
import numpy as np
import scipy as sp



def ising_hamiltonian(J, h, n):
    J = np.array(J)
    H = np.zeros((2**n, 2**n), dtype=complex)
    for k in range(1, n+1):
        for j in range(k+1, n+1):
            interaction = J[k-1, j-1]
            if interaction != 0:
                Z_k = pauli(n, k, Z)  # Pauli-Z on qubit k
                Z_j = pauli(n, j, Z)  # Pauli-Z on qubit j
                H += interaction * np.matmul(Z_k,Z_j) 

    for j in range(1,n+1):
        magnetic_field = h[j-1]
        if magnetic_field != 0:
            Z_j = pauli(n, j, Z)  # Pauli-Z on qubit j
            H += magnetic_field * Z_j
    
    
    return H






    