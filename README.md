# Quantum Photonic Circuit (QPC) Simulator

The `qpc.py` is a Python script that simulates a quantum photonic circuit. It provides a user interface to interactively build and simulate a quantum circuit using a selected set of quantum gates. The script is built on the [Strawberry Fields](https://strawberryfields.ai/) library developed by [Xanadu](https://www.xanadu.ai/) and utilizes [Streamlit](https://streamlit.io/) for the web-based interactive user interface.

## Features

1. **Circuit Configuration:** The user can select the number of quantum modes and quantum gates to use in the circuit.

2. **Gate Configuration:** For each gate, the user can select the gate type, the modes to apply the gate to, and the gate's parameters.

3. **Simulation:** After defining the circuit and the gates, the user can simulate the quantum circuit, and the script will display the resulting quantum state.

4. **Visualization:** The script visualizes the resulting state by showing the Wigner function and Fock distribution for each mode.

## Prerequisites

The script requires the following Python libraries:

- numpy
- matplotlib
- seaborn
- streamlit
- strawberryfields

You can install these libraries using pip:

```bash
pip install numpy matplotlib seaborn streamlit strawberryfields
```

## Usage

To start the simulator, run the `qpc.py` script with Streamlit:

```bash
streamlit run qpc.py
```

This will open a web page in your default browser with the user interface of the quantum photonic circuit simulator. Use the sidebar on the left to define the circuit and the gates, then press the "Run Simulation" button to simulate the circuit and visualize the resulting quantum state.
