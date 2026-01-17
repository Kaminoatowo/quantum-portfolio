# Theory of Quantum States

This document provides a theoretical overview of quantum states, covering their mathematical representation and physical interpretation within the framework of quantum mechanics.

## 1. Postulates of Quantum Mechanics (States)

- State postulate
    (Any isolated system is completely described by its quantum state, which mathematically corresponds to a vector in a Hilbert space)
    (In classical mechanics, the state of a system is described by points in phase space, whereas in quantum mechanics, it is represented by vectors in a complex vector space known as Hilbert space.)
    (Dynamics describes how a state evolves over time. In quantum mechanics, this evolution is governed by the Schrödinger equation, which dictates how the state vector changes in response to the system's Hamiltonian.)
    (While in classical mechanics, states are described by real numbers, usually representing positions and momenta, quantum states are represented by complex vectors. Moreover, classical states can be precisely known, whereas quantum states inherently involve probabilities and uncertainties.)
    (The measurement postulate states that the outcome of measuring a quantum system is probabilistic, with probabilities determined by the state's projection onto the measurement basis.)
- Physical meaning of |ψ⟩
    (The ket notation |ψ⟩ represents a quantum state vector in a complex Hilbert space. It encodes all possible information about the system's physical properties.)
    (The description of a system in quantum mechanics begins with identifying a set of variables defining the quantum state of the system. These variables correspond to observables, which are represented by Hermitian operators acting on the Hilbert space.)
    (The state vector |ψ⟩ contains information about the probabilities of different measurement outcomes. The square of the amplitude of each component of the state vector gives the probability of measuring the corresponding eigenvalue.)
    (Measuring a quantum state causes it to collapse to one of the eigenstates of the measurement operator, with probabilities determined by the state's projection onto those eigenstates.)

## 2. Hilbert Space Formalism

- Finite-dimensional Hilbert spaces
    (A finite-dimensional Hilbert space is a complex vector space equipped with an inner product, and its dimension corresponds to the number of basis vectors needed to span the space.)
    (In quantum mechanics, finite-dimensional Hilbert spaces are often used to describe systems with a limited number of states, such as spin systems or qubits.)
    (Vectors in a finite-dimensional Hilbert space can be represented as column vectors, and operations such as addition and scalar multiplication follow the rules of linear algebra.)
    (The inner product in a Hilbert space allows for the definition of orthogonality and normalization of state vectors, which are crucial for understanding quantum states and their measurements.)
- Computational basis
    (The computational basis is a standard orthonormal basis used to represent quantum states, typically consisting of basis vectors corresponding to the classical states of a system.)
    (In the case of a qubit, the computational basis consists of the states |0⟩ and |1⟩, which can be represented as column vectors [1, 0]ᵀ and [0, 1]ᵀ, respectively.)
    (Any quantum state can be expressed as a linear combination (superposition) of the computational basis states, allowing for the representation of complex quantum phenomena.)
    (The choice of computational basis is essential for performing quantum computations and measurements, as it defines how information is encoded and manipulated in quantum systems.)

## 3. Pure States

- Statevectors
    (A statevector is a mathematical representation of a quantum state, typically expressed as a column vector in a complex Hilbert space.)
    (Statevectors can be normalized, meaning their inner product with themselves equals one, which ensures that the total probability of all possible measurement outcomes is one.)
    (Statevectors can be expressed in different bases, and transformations between bases are achieved through unitary operations.)
    (The evolution of statevectors over time is governed by the Schrödinger equation, which describes how the state changes in response to the system's Hamiltonian.)
- Global vs relative phase
    (Global phase refers to a multiplicative factor of the form e^(iθ) applied to a quantum statevector, which does not affect measurement outcomes or physical predictions.)
    (Relative phase, on the other hand, is the phase difference between components of a superposition state, which can influence interference effects and measurement probabilities.)
    (While global phase is unobservable, relative phase plays a crucial role in quantum phenomena such as interference and entanglement.)
    (Understanding the distinction between global and relative phase is essential for interpreting quantum states and their behavior under various operations.)
- Bloch sphere (conceptual)
    (The Bloch sphere is a geometric representation of the state space of a two-level quantum system (qubit), where each point on the sphere corresponds to a unique pure state.)
    (The north and south poles of the Bloch sphere represent the computational basis states |0⟩ and |1⟩, while points on the surface represent superpositions of these states.)
    (The Bloch sphere provides an intuitive way to visualize quantum states, their transformations, and operations such as rotations and measurements.)
    (Understanding the Bloch sphere is helpful for grasping concepts in quantum computing and quantum information theory.)

## 4. Mixed States

- Density matrix formalism
    (A density matrix is a mathematical representation of a quantum state that can describe both pure and mixed states, providing a more general framework than statevectors alone.)
    (The density matrix ρ is defined as ρ = |ψ⟩⟨ψ| for pure states and as a weighted sum of projectors for mixed states, allowing for the representation of statistical ensembles of quantum states.)
    (Density matrices are Hermitian, positive semi-definite, and have a trace equal to one, ensuring they represent valid quantum states.)
    (The density matrix formalism is particularly useful for describing open quantum systems and situations where the system is entangled with its environment.)
    (Operations on density matrices, such as unitary transformations and measurements, can be performed using matrix algebra, making them a powerful tool in quantum mechanics.)
- Statistical mixtures
    (A statistical mixture is a different type of linear combination. It represents a situation where a quantum system is in one of several possible states, each with a certain probability, rather than being in a coherent superposition of those states.)
    (In a statistical mixture, the system is described by a density matrix that is a weighted sum of the density matrices of the individual states, reflecting the probabilities of each state.)
    (Statistical mixtures arise in scenarios where there is uncertainty about the state of the system, such as when dealing with ensembles of particles or when the system interacts with an environment.)
    (The key difference between superpositions and statistical mixtures is that superpositions involve coherent combinations of states, while mixtures represent classical uncertainty about the state.)
- Physical interpretation
    (The density matrix provides a complete description of a quantum system's state, capturing both quantum coherence and classical uncertainty.)
    (The diagonal elements of the density matrix represent the probabilities of finding the system in each basis state, while the off-diagonal elements capture quantum coherence between states.)
    (Measurements on mixed states yield probabilistic outcomes, with probabilities determined by the density matrix, similar to pure states but accounting for statistical mixtures.)
    (The physical interpretation of mixed states is crucial for understanding real-world quantum systems, which often interact with their environment and cannot be described by pure states alone.)

## 5. Reduced States

- Composite systems
    (Composite systems are quantum systems composed of multiple subsystems, where the overall state is described in a larger Hilbert space formed by the tensor product of the individual subsystems' Hilbert spaces.)
    (The state of a composite system can exhibit entanglement, where the states of the subsystems are correlated in such a way that the state of one subsystem cannot be described independently of the other.)
    (The mathematical representation of composite systems involves using tensor products to combine the statevectors or density matrices of the individual subsystems.)
    (Understanding composite systems is essential for studying phenomena such as entanglement, quantum correlations, and quantum information processing.)
    (Operations on composite systems, such as measurements and unitary transformations, can affect the entire system or individual subsystems, leading to complex dynamics and interactions.)
- Partial trace
    (The partial trace is a mathematical operation used to obtain the reduced state of a subsystem from the density matrix of a composite system by tracing out the degrees of freedom of the other subsystems.)
    (The reduced density matrix of a subsystem provides a complete description of that subsystem's state, accounting for its interactions and correlations with the rest of the composite system.)
    (The partial trace operation is essential for studying open quantum systems, where a subsystem interacts with an environment, leading to decoherence and loss of information.)
    (Calculating the partial trace involves summing over the basis states of the subsystem being traced out, resulting in a reduced density matrix for the remaining subsystem.)
- Loss of information and correlations
    (When a subsystem is traced out, information about the correlations between that subsystem and the rest of the composite system is lost, leading to a reduced description of the subsystem's state.)
    (The loss of information due to partial tracing can be quantified using measures such as entropy, which capture how much information is lost in the process.)
    (In open quantum systems, partial tracing is used to model the interaction with an environment, where information flows from the system to its surroundings, causing decoherence and reducing quantum coherence.)
    (Understanding the implications of information loss and correlations is crucial for studying quantum decoherence, entanglement dynamics, and the behavior of quantum systems in realistic settings.)
