#defining starting state of phi
from PAULI_DEF import pauli, X, Y, Z, I
from H_ising import ising_hamiltonian
from h_vector import h_mat
import numpy as np
import scipy as sp
from scipy.linalg import expm



# defining A,B time variables 

def A(tmax, t):
    return 1-(t/tmax)
def B(tmax, t):
    return t/tmax

# defining Time Dependent Hamiltonian

def Hamiltonian(t, tmax, Ising, n):
    H = np.zeros((2**n, 2**n), dtype=complex)
    for i in range(1, n+1):
        H += pauli(n,i,X)
    return -(A(tmax,t)* H) + (B(tmax,t)*Ising)

#defining evolution

def Evolution(tmax, Ising, n, q, k, phi0, phi_target):
    tau = tmax / q
    product = np.eye(2**n, dtype=complex)
    fidelities = []

    for i in range(1, k + 1):
        # Calculate time-dependent Hamiltonian at time t = i * tau
        H_t = Hamiltonian(i * tau, tmax, Ising, n)
        exp_term = expm(-1j * tau * H_t)

        # Apply in time-ordered manner (new term on the left)
        product = np.matmul(exp_term, product)

        # Calculate evolved state and fidelity
        evolved_state = np.matmul(product, phi0)
        fidelity = np.abs(np.inner(evolved_state, phi_target))**2
        fidelities.append(fidelity)

    return evolved_state, fidelities