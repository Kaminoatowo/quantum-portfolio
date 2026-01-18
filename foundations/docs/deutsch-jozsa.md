# Deutsch-Jozsa algorithm

## Introduction

- demonstrating a principle
    (Deutsch-Jozsa algorithm was developped to be an easy problem to solve for a quantum algorithm, but very difficult for a classical one. In essence, it shows that a black box problem can be deterministically solved by a quantum computer - without errors -, while a deterministic classical computer would take a large number of queries to the oracle.)
- concepts: oracles, interference, quantum parallelism
    (The idea is to make use of interference between states in a quantum computer to encode the answer to the DJ problem to the measurement of a specific quantum state.)
    (The action of the oracle function on the basis states is mapped to the relative phases of the computational basis and letting the states interfere makes so the information about the constant-ness or balanced-ness nature of the oracle function is tied to the probability of measuring one specific state.)

## The problem

- define the function f
    (The oracle function is defined over the n-dimensional tensor product of the computational basis of bits {0,1} and has values in {0,1}. It is either defined constant - it outputs only 0 or only 1 - or balanced - it outputs 0 for half of the n-bits binary strings and 1 for the others.)
- the promise
    (The only fact that is known about the oracle function is that it is either constant or balanced. This is called "the promise". It guarantees that no other choices are possible.)
- determine if f is either constant or balanced
    (Imagine querying the oracle twice and obtaining 0 as the first answer and 1 as the second. We immediately know that the function is balanced, since this is the only possible case for obtaining two different results - remember the promise.)
    (If we rather obtain 0 for both queries - or 1 - we don't know if the function is constant or is it balanced. We know it's balanced in the moment we obtain the other possible value - 1 for our base case. If the function is constant, we will always obtain the same value as output; but if the function is balanced, we could be so unlucky to keep measuring the same value all the times it is possible. Say we have two bits, then the number of basis states is four and a balanced function would return 0 for two of these and 1 for the other two. In this case the maximum number of times we can measure the same number and don't yet know the nature of the function is two, since the third time we query the oracle we could obtain another 0 and know the function is constant or get a 1 and know the function is balanced.)
- classical complexity (number of evaluations needed)
    (In the classical case, for a deterministic algorithm, we need 2^{n-1}-1 queries to know the nature of the function. We could use a randomized algorithm, then k queries are enough to know whether the function is constant or balanced with an error probability of 1/2^k. For an exact answer we need k=2^{n-1}-1 also in this case.)
    (A quantum algorithm needs only one query to know for sure the nature of the oracle function.)

## The oracle

- define the quantum oracle
    (The oracle is implemented as a black box that takes in a quantum registry of n qubits and an ancillary qubit. The implementation of the oracle is such that it doesn't copy the input x and it outputs the action on x through the ancilla qubit. The oracle should not make the input collapse.)

## The idea behind the algorithm

- prepare the suerposition
    (We would like to havve all the states of the computational basis at disposal. We can do that using superposition: apply a n+1-fold Hadamard gate on the n qubits + ancilla initial state - prepared in the all zero state and ancilla in 1 -, we can find out that the "all +" state is the uniform superposition of all of the states of the computational basis, while the ancilla state is mapped to the "-" state.)
- the oracle introduces phases dependent on f
    (The action of the oracle is to map the input state to the tensor state generated from the input n-qubits state and the modulo 2 addition of the ancilla state with the action of the function on the n-qubits state. Since the ancilla is in the "-" state, both possibilities are available in the superposition. This has the same result as adding a relative phase to each n-registry-ancilla tensor state, depending on the action of the oracle function. To be more specific, this relative phase is just a sign depending on the value of function.)
- global information is coded inside distructive/constructive interference
    (One final Hadamard gate on the n-qubits registry combines all the relative phases into the coefficients of each of the basis states. This act of interference introduces a new phase which depends on how the previous states are mapped to the new superposition. However, by measuring the "all zero" state, this phase is unitary, so it doesn't add more information to the coefficient.)
- f is revealed with one measurement
    (Finally, by measuring the "all zero" state we can obtain the hidden information relative to the oracle function. By inspecting the probability of measuring the "all zero" state, we find that this is equal to 1 if the function is constant (constructive interference), while it is equal to 0 if the function is balanced(destructive interference).)

## The algorithm step-by-step

1. initial state
   1. why the ancilla is in state 1?
2. hadamard on all qubits
   1. uniform superposition
   2. ancilla in state -
3. apply the oracle
   1. phase kickback
4. hadamard on the n qubits
   1. constant f -> amplitude in focused on the "all zero" state
   2. balanced f -> null amplitude for the "all zero" state
5. measurement
   1. measure the "all zero" state -> f is constant
   2. measure any other state -> f is balanced

## What needs to be coded

1. primitives from the framework
   1. statevector
   2. tensor product
   3. gates: H, X, controlled(U)
   4. application of operators
2. new components
   1. oracle function and gate
   2. initial state preparation
   3. build the circuit
   4. simulation and interpretation

## Relevance

- query complexity
- reference problem (Simon, Bernstein-Vazirani, Grover)
- global information emerging without knowing local details
