from codecs import register
import numpy as np
from src.states.statevector import basis_state, normalize, tensor, apply_operator
from src.gates.single_qubit import H

# Define the oracle

def balanced_function(index: np.ndarray) -> int:
    
    if index % 2 == 0:
        return 0
    else:
        return 1

def constant_function(index: np.ndarray) -> int:
    return 0

def bitstring_to_index(bits):
    return int("".join(str(b) for b in bits), 2)

import numpy as np

def deutsch_jozsa_oracle(f, n):
    """
    Build the oracle U_f for Deutsch–Jozsa.

    Parameters
    ----------
    f : callable
        Classical function f(x_bits) -> 0 or 1
    n : int
        Number of input qubits

    Returns
    -------
    U : np.ndarray
        (2^(n+1) x 2^(n+1)) unitary matrix
    """
    dim = 2 ** (n + 1)
    U = np.zeros((dim, dim), dtype=complex)

    for x in range(2**n):
        for y in [0, 1]:
            # input index |x⟩|y⟩
            in_index = (x << 1) | y

            fx = f(x)
            y_out = y ^ fx

            # output index |x⟩|y ⊕ f(x)⟩
            out_index = (x << 1) | y_out

            U[out_index, in_index] = 1.0

    return U


# Prepare initial state
def prepare_register(num_qubits = 1):

# +1 (ancilla)
    register_x = basis_state(0,num_qubits)
    ancilla = basis_state(1,1)

    register = normalize(tensor(register_x, ancilla))

    return register


# Create superposition
def create_superposition(register: np.ndarray) -> np.ndarray:
    num_qubits = int(np.log2(len(register)))
    Hadamard_register = H()
    for _ in range(num_qubits - 1):
        Hadamard_register = np.kron(Hadamard_register, H())
    return apply_operator(register, Hadamard_register)

# Apply oracle gate
def apply_oracle(register: np.ndarray, function) -> np.ndarray:
    n = int(np.log2(len(register))) - 1  # Number of input qubits
    U = deutsch_jozsa_oracle(function, n=n)
    return apply_operator(register, U)

# Apply Hadamard
def last_hadamard(register: np.ndarray) -> np.ndarray:
    num_qubits = int(np.log2(len(register)))
    Hadamard_register = H()
    for _ in range(num_qubits - 2):
        Hadamard_register = np.kron(Hadamard_register, H())
    last_hadamard = np.kron(Hadamard_register, np.eye(2))
    return apply_operator(register, last_hadamard)

# Measurement
def measure_register(register: np.ndarray, num_qubits: int) -> np.ndarray:
    probabilities = np.abs(register)**2
    measurement = np.zeros(2**(num_qubits - 1))
    for i in range(2**(num_qubits - 1)):
        measurement[i] = probabilities[i << 1] + probabilities[(i << 1) | 1]
    return measurement


register1 = prepare_register(2)
register1 = create_superposition(register1)
register1 = apply_oracle(register1, balanced_function)
register1 = last_hadamard(register1)
measurement1 = measure_register(register1, 3)
print("Measurement probabilities for balanced function:", measurement1)
register2 = prepare_register(2)
register2 = create_superposition(register2)
register2 = apply_oracle(register2, constant_function)
register2 = last_hadamard(register2)
measurement2 = measure_register(register2, 3)
print("Measurement probabilities for constant function:", measurement2)