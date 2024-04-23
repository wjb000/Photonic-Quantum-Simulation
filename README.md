# Quantum Photonic Circuit (QPC) Simulator

The `qpc.py` is a Python script that simulates quantum photonic circuits. It provides a user-friendly, interactive interface to build and simulate quantum circuits using a curated set of quantum gates. This script leverages the Strawberry Fields library by Xanadu and uses Streamlit to facilitate a web-based, interactive user interface.

## Features

1. **Dynamic Circuit Configuration:** Users can dynamically configure the number of quantum modes and gates directly through the user interface.

2. **Flexible Gate Configuration:** Each gate can be configured interactively, allowing users to select the gate type, apply it to specific modes, and set individual parameters.

3. **Interactive Simulation:** The simulator offers a "Run Simulation" button that processes the user-defined circuit configurations and computes the resulting quantum state.

4. **Advanced Visualization:** Post-simulation, the script provides detailed visualizations, including:
   - **Wigner Function:** Displays the Wigner function for each mode in the circuit.
   - **Fock State Probabilities:** Shows the probability distribution across different Fock states for each mode.

5. **Responsive Design:** The Streamlit interface is designed to be responsive and intuitive, providing real-time feedback and updates as users configure and simulate circuits.

## Prerequisites

Before running the simulator, ensure you have the following Python libraries installed:

- **numpy**
- **matplotlib**
- **seaborn**
- **streamlit**
- **strawberryfields**

These dependencies can be installed via pip using the following command:

```bash
pip install numpy matplotlib seaborn streamlit strawberryfields
```

## Installation

To get started with the Quantum Photonic Circuit Simulator, clone the repository or download the `qpc.py` file directly. Ensure all dependencies are installed as listed above.

## Usage

To launch the simulator, use the following command:

```bash
streamlit run qpc.py
```

This command starts a local web server and opens the interactive simulator in your default web browser. Follow the on-screen instructions to configure and simulate your quantum photonic circuits.
