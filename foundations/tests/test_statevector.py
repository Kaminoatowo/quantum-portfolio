import numpy as np
import pytest

from src.states.statevector import (
    basis_state,
    normalize,
    is_normalized,
    tensor,
    apply_operator,
    measurement_probabilities,
    inner_product,
)

# basis_state

def test_basis_state_dimension():
    state = basis_state(index=0, num_qubits=3)
    assert state.shape == (2**3,)

def test_basis_state_normalization():
    state = basis_state(index=2, num_qubits=3)
    norm = np.vdot(state, state)
    assert np.isclose(norm, 1.0)

def test_basis_state_correct_position():
    state = basis_state(index=1, num_qubits=2)
    expected = np.array([0, 1, 0, 0], dtype=complex)
    assert np.allclose(state, expected)

def test_basis_state_orthogonality():
    psi = basis_state(0, 2)
    phi = basis_state(3, 2)
    overlap = np.vdot(psi, phi)
    assert np.isclose(overlap, 0.0)

# normalize e is_normalized

def test_normalize_state():
    state = np.array([1, 1], dtype=complex)
    normed = normalize(state)
    assert is_normalized(normed)

def test_is_normalized_false():
    state = np.array([1, 1], dtype=complex)
    assert not is_normalized(state)

def test_normalize_preserves_direction():
    state = np.array([1, -1j], dtype=complex)
    normed = normalize(state)
    ratio = normed[0] / state[0]
    assert np.allclose(normed, ratio * state)

# tensor

def test_tensor_single_qubit():
    zero = basis_state(0, 1)
    one = basis_state(1, 1)
    state = tensor(zero, one)
    expected = np.array([0, 1, 0, 0], dtype=complex)
    assert np.allclose(state, expected)

def test_tensor_three_qubits_dimension():
    a = basis_state(0, 1)
    b = basis_state(1, 1)
    c = basis_state(0, 1)
    state = tensor(a, b, c)
    assert state.shape == (2**3,)

def test_tensor_normalization():
    a = normalize(np.array([1, 1], dtype=complex))
    b = normalize(np.array([1, -1], dtype=complex))
    state = tensor(a, b)
    assert is_normalized(state)

# apply_operator

def test_apply_identity_operator():
    state = basis_state(0, 1)
    identity = np.eye(2)
    result = apply_operator(state, identity)
    assert np.allclose(result, state)

def test_apply_operator_dimension_mismatch():
    state = basis_state(0, 1)
    operator = np.eye(4)
    with pytest.raises(ValueError):
        apply_operator(state, operator)

def test_apply_operator_unitary_preserves_norm():
    state = normalize(np.array([1, 1j], dtype=complex))
    unitary = np.array([[0, 1], [1, 0]], dtype=complex)  # Pauli-X
    result = apply_operator(state, unitary)
    assert is_normalized(result)

# measurement_probabilities

def test_measurement_probabilities_sum_to_one():
    state = normalize(np.array([1, 1], dtype=complex))
    probs = measurement_probabilities(state)
    assert np.isclose(np.sum(probs), 1.0)

def test_measurement_probabilities_basis_state():
    state = basis_state(2, 2)
    probs = measurement_probabilities(state)
    expected = np.array([0, 0, 1, 0])
    assert np.allclose(probs, expected)

def test_measurement_probabilities_non_negative():
    state = normalize(np.array([1, -1j], dtype=complex))
    probs = measurement_probabilities(state)
    assert np.all(probs >= 0)

# inner_product

def test_inner_product_self():
    psi = basis_state(1, 2)
    overlap = inner_product(psi, psi)
    assert np.isclose(overlap, 1.0)

def test_inner_product_orthogonal():
    psi = basis_state(0, 2)
    phi = basis_state(3, 2)
    overlap = inner_product(psi, phi)
    assert np.isclose(overlap, 0.0)

def test_inner_product_linearity():
    psi = basis_state(0, 1)
    phi = basis_state(1, 1)
    superposition = normalize(psi + phi)
    overlap = inner_product(psi, superposition)
    assert np.isclose(abs(overlap)**2, 0.5)

