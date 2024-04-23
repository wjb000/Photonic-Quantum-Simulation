import streamlit as st
import strawberryfields as sf
from strawberryfields import ops
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

GATES = {
    "Displacement Operator": ops.Dgate,
    "Squeezing Operator": ops.Sgate,
    "Beam Splitter": ops.BSgate,
}

PARAMS = {
    "Displacement Operator": ["abs", "phi"],
    "Squeezing Operator": ["r", "phi"],
    "Beam Splitter": ["theta", "phi"],
}

def simulate_circuit(num_modes, instructions):

    prog = sf.Program(num_modes)

    with prog.context as q:
        for gate, params, modes in instructions:
            GATES[gate](*params) | [q[i] for i in modes]

    eng = sf.Engine('fock', backend_options={"cutoff_dim": 10})
    result = eng.run(prog)

    return result.state

def visualize_state(state):
    num_modes = state.num_modes
    fig, ax = plt.subplots(1, num_modes, figsize=(4*num_modes, 4))

    for i in range(num_modes):
        axis = ax[i] if num_modes > 1 else ax
        data = state.wigner(i, np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))
        cb = axis.contourf(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100), data, cmap='hot')
        fig.colorbar(cb, ax=axis)
        axis.set_title(f"Wigner Function (Mode {i+1})")

    st.pyplot(fig)

    fock_probs = state.all_fock_probs()
    for i in range(num_modes):
        st.bar_chart(fock_probs[:, i])

def main():

    st.title('Quantum Photonic Circuit Simulator')

    num_modes = st.sidebar.slider('Number of modes', 1, 5, 2)
    num_gates = st.sidebar.slider('Number of gates', 1, 5, 2)

    instructions = []
    for i in range(num_gates):
        gate = st.sidebar.selectbox('Select a gate', list(GATES.keys()), key=f'gate{i}')
        modes = st.sidebar.multiselect('Select modes', range(num_modes), key=f'modes{i}')
        params = tuple(st.sidebar.slider(f'Parameter {p}', 0.0, 2.0, 1.0, key=f'param{i}{j}') for j, p in enumerate(PARAMS[gate]))
        instructions.append((gate, params, modes))

    if st.button('Run Simulation'):
        state = simulate_circuit(num_modes, instructions)
        visualize_state(state)

if __name__ == "__main__":
    main()
