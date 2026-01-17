import numpy as np

def basis_state(index: int, num_qubits: int) -> np.ndarray:
    """
    Returns the computational basis state |index> in a system of num_qubits.
    """

    state = np.zeros(2**num_qubits)
    state[index] = 1

    return state
    
def normalize(state: np.ndarray) -> np.ndarray:
    """Normalize a statevector."""

    normalization = np.vdot(state, state)
    state = state / np.sqrt(normalization)

    return state

def is_normalized(state: np.ndarray, tol=1e-10) -> bool:
    """Check if a statevector is normalized."""

    normalization = np.sum(np.abs(state)**2)

    return np.abs(normalization - 1.) < tol

def tensor(*states: np.ndarray) -> np.ndarray:
    """Tensor product of multiple statevectors."""

    tensor_state = states[0]
    for state in states[1:]:
        print(state)
        #tensor_state = np.hstack([tensor_state[i]*state for i in range(len(tensor_state))])
        tensor_state = np.kron(tensor_state, state)

    return normalize(tensor_state)

def apply_operator(state: np.ndarray, operator: np.ndarray) -> np.ndarray:
    """Apply a unitary operator to a statevector."""

    result = np.matmul(operator,state)

    return normalize(result)

def measurement_probabilities(state: np.ndarray) -> np.ndarray:
    """Return probabilities for computational basis measurement."""

    normalized = normalize(state)
    result = np.abs(normalized*normalized)
    return result

def inner_product(psi: np.ndarray, phi: np.ndarray) -> complex:
    """Compute <psi|phi>."""

    return np.vdot(psi,phi)