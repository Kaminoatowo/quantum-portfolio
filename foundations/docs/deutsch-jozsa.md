# Deutsch-Jozsa algorithm

## Introduction

- demonstrating a principle
- concepts: oracles, interference, quantum parallelism

## The problem

- define the function f
- the promise
- determine if f is either constant or balanced
- classical complexity (number of evaluations needed)

## The oracle

- define the quantum oracle

## The idea behind the algorithm

- prepare the suerposition
- the oracle introduces phases independent on f
- global information is coded inside distructive/constructive interference
- f is revealed with one measurement

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
