# Photonic Quantum Computer Simulation

## Description
This program is a photonic quantum computer simulator that leverages the Strawberry Fields quantum computing library to model and manipulate quantum states of light. It begins by preparing a quantum state in a two-mode Fock basis, followed by a sequence of quantum operations: a displacement operation, a squeezing operation, and a beamsplitter operation. These transformations result in a new quantum state. Lastly, the program computes and visualizes the Wigner function, a representation of the quantum state in phase space, for each mode.

Users can specify the parameters for the displacement amplitude, displacement phase, squeezing parameter (r), and squeezing angle (phi), enabling them to explore how these different parameters influence the resulting quantum state.

## Requirements
* Python 3.6 or higher
* Strawberry Fields library

To install the Strawberry Fields library, use the pip package manager:
```
pip install strawberryfields
```

## Usage
To execute the program, run the following command:

```
python3 qpc.py
```

You will be asked to input the following parameters:

* Displacement amplitude
* Displacement phase
* Squeezing parameter (r)
* Squeezing angle (phi)

For instance:

```
Enter the displacement amplitude: 1.0
Enter the displacement phase: 0.5
Enter the squeezing parameter r: 0.6
Enter the squeezing angle phi: 1.57
```

Upon entering the parameters, the program will execute the simulation and display the Wigner function for each mode in a phase-space diagram (position vs momentum). This visualization represents the quantum state of each mode in the optical system post-transformation.

