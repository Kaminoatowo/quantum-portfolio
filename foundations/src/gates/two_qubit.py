import numpy as np

def CNOT() -> np.ndarray:
    
    return np.array([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 0., 1.], [0., 0., 1., 0.]], complex)

def CZ() -> np.ndarray:

    return np.array([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., -1.]], complex)

def SWAP() -> np.ndarray:

    return np.array([[1., 0., 0., 0.], [0., 0., 1., 0.], [0., 1., 0., 0.], [0., 0., 0., 1.]], complex)
    
def controlled(U: np.ndarray) -> np.ndarray:
    """Build controlled-U gate."""

    if len(U) != 2 and len(U[0]) != 2:
        raise ValueError("Argument gate must be 2x2 matrix")
    return np.array([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., U[0][0], U[0][1]], [0., 0., U[1][0], U[1][1]]], complex)
