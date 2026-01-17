import numpy as np
import pytest

from src.gates.single_qubit import X, Y, Z, H, RX, RY, RZ
from src.states.statevector import basis_state, apply_operator, is_normalized

# Test strutturali

def test_gate_shape():
    gate = X()
    assert gate.shape == (2, 2)

def test_gate_complex_dtype():
    gate = Y()
    assert np.iscomplexobj(gate)

# Unitarietà

@pytest.mark.parametrize("gate_fn", [X, Y, Z, H])
def test_gate_unitary(gate_fn):
    U = gate_fn()
    identity = np.eye(2)
    assert np.allclose(U.conj().T @ U, identity)

@pytest.mark.parametrize("theta", [0.1, 0.5, 1.0])
def test_rotation_gate_unitary(theta):
    for gate in [RX(theta), RY(theta), RZ(theta)]:
        identity = np.eye(2)
        assert np.allclose(gate.conj().T @ gate, identity)

# Azione sugli stati base

def test_X_gate_action():
    zero = basis_state(0, 1)
    one = basis_state(1, 1)

    assert np.allclose(apply_operator(zero, X()), one)
    assert np.allclose(apply_operator(one, X()), zero)

def test_Z_gate_action():
    zero = basis_state(0, 1)
    one = basis_state(1, 1)

    assert np.allclose(apply_operator(zero, Z()), zero)
    assert np.allclose(apply_operator(one, Z()), -one)

def test_H_gate_action():
    zero = basis_state(0, 1)
    one = basis_state(1, 1)

    plus = apply_operator(zero, H())
    minus = apply_operator(one, H())

    assert is_normalized(plus)
    assert is_normalized(minus)

    assert np.allclose(abs(plus[0])**2, 0.5)
    assert np.allclose(abs(plus[1])**2, 0.5)

# Proprietà note

def test_H_squared_identity():
    U = H()
    assert np.allclose(U @ U, np.eye(2))

@pytest.mark.parametrize("gate_fn", [X, Z])
def test_pauli_squared_identity(gate_fn):
    U = gate_fn()
    assert np.allclose(U @ U, np.eye(2))

# Rotazioni (limiti e casi noti)

def test_RX_zero_identity():
    assert np.allclose(RX(0.0), np.eye(2))

def test_RZ_pi_phase():
    one = basis_state(1, 1)
    rotated = apply_operator(one, RZ(np.pi))

    # global phase allowed, but magnitude must be preserved
    assert np.isclose(abs(rotated[1]), 1.0)

# Conservazione della norma

@pytest.mark.parametrize("gate_fn", [X, Y, Z, H])
def test_gate_preserves_norm(gate_fn):
    state = basis_state(0, 1)
    new_state = apply_operator(state, gate_fn())
    assert is_normalized(new_state)

@pytest.mark.parametrize("theta", [0.2, 0.7])
def test_rotation_preserves_norm(theta):
    state = basis_state(1, 1)
    for gate in [RX(theta), RY(theta), RZ(theta)]:
        new_state = apply_operator(state, gate)
        assert is_normalized(new_state)
