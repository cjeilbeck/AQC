
from PAULI_DEF import pauli, X, Y, Z, I
from H_ising import ising_hamiltonian
from h_vector import h_mat
import numpy as np
import scipy as sp
from scipy.linalg import expm
from EVOLUTION import Evolution, Hamiltonian, A, B 
from core import columnvector



import numpy as np
import scipy as sp

Mtest = np.array([[0,1,0],[0,0,1],[0,0,0]])
h = h_mat(Mtest, 0.5)
phi_0 = (1/np.sqrt(8)) * np.ones(8)
phitarget = columnvector(8,5)
print(phitarget)



ising1 = ising_hamiltonian(Mtest,h,3)
startingstate = Hamiltonian(0,100,ising1,3)
endstate = Hamiltonian(100,100,ising1,3)


import matplotlib.pyplot as plt



tmax = 100
q=1000
n=3
k=1000

t_values = np.linspace(0, tmax, q)
_, fidelities = Evolution(tmax, ising1, n, q, k, phi_0, phitarget)

plt.plot(t_values, fidelities)
plt.xlabel("Time")
plt.ylabel("Fidelity with Ground State")
plt.title("Fidelity of Evolving State with Target Ground State")
plt.show()




