# Photonic Quantum Computer Simulation

This program is a simple simulator of a photonic quantum computer. It uses the Strawberry Fields quantum computing library to create and manipulate quantum states of light. 

## Description

The program begins by creating a quantum state in a two-mode Fock basis. It then applies a sequence of quantum operations (a displacement operation followed by a squeezing operation and a beamsplitter operation) to transform the state. Finally, it calculates and prints the expectation values and variances of the position and momentum of the state.

The parameters of the displacement and squeezing operations can be specified by the user when running the program. This allows the user to explore how different parameters affect the resulting quantum state.

## Requirements

- Python 3.6 or higher
- Strawberry Fields library (can be installed with `pip install strawberryfields`)

## Usage

To run the program, use the following command:

```
python3 qpc.py
```

When prompted, enter the real and imaginary parts of the displacement parameter alpha, the squeezing parameter r, and the squeezing angle phi. These should all be real numbers.

For example:

```
Enter the real part of alpha: 1.0
Enter the imaginary part of alpha: 0.5
Enter the squeezing parameter r: 0.6
Enter the squeezing angle phi: 1.57
```

After entering the parameters, the program will calculate and print the expectation values and variances of the position and momentum of the resulting quantum state. It will also display a Wigner function of the state, which is a graphical representation of the quantum state in phase space.

## Learning

By using this program, you can learn more about the effects of different quantum operations on quantum states of light. This can help you build intuition about how these operations transform quantum states, and how they can be used in quantum computing and quantum information processing.

In addition, the program can be easily modified to include additional operations or to change the initial state, allowing you to explore a wider range of quantum phenomena.
