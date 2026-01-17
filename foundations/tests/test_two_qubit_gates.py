import numpy as np
import pytest

from src.gates.two_qubit import CNOT, CZ, SWAP, controlled
from src.gates.single_qubit import X, Z
from src.states.statevector import (
    basis_state,
    tensor,
    apply_operator,
    is_normalized,
)

# Test strutturali

@pytest.mark.parametrize("gate_fn", [CNOT, CZ, SWAP])
def test_two_qubit_gate_shape(gate_fn):
    gate = gate_fn()
    assert gate.shape == (4, 4)

def test_gate_complex_dtype():
    gate = CNOT()
    assert np.iscomplexobj(gate)

def test_controlled_gate_shape():
    CU = controlled(X())
    assert CU.shape == (4, 4)

def test_controlled_gate_complex_dtype():
    CU = controlled(Z())
    assert np.iscomplexobj(CU)


# Unitarietà

@pytest.mark.parametrize("gate_fn", [CNOT, CZ, SWAP])
def test_two_qubit_gate_unitary(gate_fn):
    U = gate_fn()
    identity = np.eye(4)
    assert np.allclose(U.conj().T @ U, identity)

def test_controlled_gate_unitary():
    CU = controlled(X())
    identity = np.eye(4)
    assert np.allclose(CU.conj().T @ CU, identity)


# Azione sugli stati base

def computational_basis():
    zero = basis_state(0, 1)
    one = basis_state(1, 1)

    return {
        "00": tensor(zero, zero),
        "01": tensor(zero, one),
        "10": tensor(one, zero),
        "11": tensor(one, one),
    }

def test_CNOT_action():
    states = computational_basis()
    U = CNOT()

    assert np.allclose(apply_operator(states["00"], U), states["00"])
    assert np.allclose(apply_operator(states["01"], U), states["01"])
    assert np.allclose(apply_operator(states["10"], U), states["11"])
    assert np.allclose(apply_operator(states["11"], U), states["10"])

def test_CZ_action():
    states = computational_basis()
    U = CZ()

    assert np.allclose(apply_operator(states["00"], U), states["00"])
    assert np.allclose(apply_operator(states["01"], U), states["01"])
    assert np.allclose(apply_operator(states["10"], U), states["10"])
    assert np.allclose(apply_operator(states["11"], U), -states["11"])

def test_SWAP_action():
    states = computational_basis()
    U = SWAP()

    assert np.allclose(apply_operator(states["01"], U), states["10"])
    assert np.allclose(apply_operator(states["10"], U), states["01"])
    assert np.allclose(apply_operator(states["00"], U), states["00"])
    assert np.allclose(apply_operator(states["11"], U), states["11"])

def test_controlled_X_is_CNOT():
    states = computational_basis()
    CU = controlled(X())

    assert np.allclose(apply_operator(states["00"], CU), states["00"])
    assert np.allclose(apply_operator(states["01"], CU), states["01"])
    assert np.allclose(apply_operator(states["10"], CU), states["11"])
    assert np.allclose(apply_operator(states["11"], CU), states["10"])

def test_controlled_Z_is_CZ():
    states = computational_basis()
    CU = controlled(Z())

    assert np.allclose(apply_operator(states["00"], CU), states["00"])
    assert np.allclose(apply_operator(states["01"], CU), states["01"])
    assert np.allclose(apply_operator(states["10"], CU), states["10"])
    assert np.allclose(apply_operator(states["11"], CU), -states["11"])

# Proprietà note

def test_SWAP_squared_identity():
    U = SWAP()
    assert np.allclose(U @ U, np.eye(4))

def test_CNOT_squared_identity():
    U = CNOT()
    assert np.allclose(U @ U, np.eye(4))

def test_controlled_gate_superposition():
    zero = basis_state(0, 1)
    one = basis_state(1, 1)

    # (|0⟩ + |1⟩)/√2 ⊗ |0⟩
    control_superposed = (tensor(zero, zero) + tensor(one, zero)) / np.sqrt(2)

    CU = controlled(X())
    result = apply_operator(control_superposed, CU)

    assert is_normalized(result)
    assert np.isclose(abs(result[0])**2, 0.5)  # |00⟩
    assert np.isclose(abs(result[3])**2, 0.5)  # |11⟩

# Creazione di entanglement

from src.gates.single_qubit import H

def test_CNOT_creates_bell_state():
    zero = basis_state(0, 1)
    state_00 = tensor(zero, zero)

    H1 = np.kron(H(), np.eye(2))
    state_plus = apply_operator(state_00, H1)

    bell = apply_operator(state_plus, CNOT())

    assert is_normalized(bell)
    assert np.isclose(abs(bell[0])**2, 0.5)
    assert np.isclose(abs(bell[3])**2, 0.5)
    assert np.isclose(abs(bell[1])**2, 0.0)
    assert np.isclose(abs(bell[2])**2, 0.0)

# Conservazione della norma

@pytest.mark.parametrize("gate_fn", [CNOT, CZ, SWAP])
def test_two_qubit_gate_preserves_norm(gate_fn):
    zero = basis_state(0, 1)
    one = basis_state(1, 1)
    state = tensor(zero, one)

    new_state = apply_operator(state, gate_fn())
    assert is_normalized(new_state)

# Errori

def test_controlled_rejects_invalid_gate():
    bad_gate = np.eye(3)
    with pytest.raises(ValueError):
        controlled(bad_gate)
