#def J= adjacency matrix and hk = -(jsum of Mkj + Mjk) + kappa

from PAULI_DEF import pauli, X, Y, Z, I
from H_ising import ising_hamiltonian
from h_vector import h_mat
import numpy as np
import scipy as sp
from scipy.linalg import expm
from EVOLUTION import Evolution, Hamiltonian, A, B 
import matplotlib.pyplot as plt


def columnvector(length,position):
    cv = np.zeros(length)
    cv[position]=1         
    return cv


#defining starting variables 

m_adj = np.array([
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]])

htest = h_mat(m_adj,0.5)
H_Ising = ising_hamiltonian(m_adj, htest, 5)
phi_0 = (1/np.sqrt(32)) * np.ones(32)
phitarget = columnvector(32,19)
tmax_values = [1, 2, 5, 10, 100]
q = 500
n = 5
k = 500

# plotting section


plt.figure(figsize=(12, 7))

for tmax in tmax_values:
    
    t_values = np.linspace(0, tmax, q)
    
    
    _, fidelities = Evolution(tmax, H_Ising, n, q, k, phi_0, phitarget)
    
    
    plt.plot(t_values/tmax, fidelities, label=f"tmax = {tmax}")


plt.xlabel("t/t_max")
plt.ylabel("Probability")
plt.title("Probability of Evolving State with Target Ground State")
plt.legend()
plt.show()
