import numpy as np
X = np.array([[0, 1], [1, 0]])
Y = np.array([[0, -1j], [1j, 0]])
Z = np.array([[1, 0], [0, -1]])
I = np.eye(2)

#def of tensor operation


def pauli(n, J, dimension):
    new = 1  # Start with scalar 1 so that np.kron works correctly.
    for i in range(1, n+1):
        if i == J:
            new = np.kron(new, dimension)  # Insert the Pauli matrix at the J-th position.
        else:
            new = np.kron(new, I)  # Insert identity matrix at other positions.
    return new

abc = pauli(5,4,Z)
print(abc)
print(np.sqrt(abc.size))


cba = pauli(5,5,Z)

print(cba)
print(np.sqrt(cba.size))