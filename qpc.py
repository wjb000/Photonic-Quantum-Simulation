import strawberryfields as sf
from strawberryfields import ops
from math import pi
import numpy as np
import matplotlib.pyplot as plt


def get_input():
    displacement_amplitude = float(input("Enter the displacement amplitude: "))
    displacement_phase = float(input("Enter the displacement phase: "))
    r = float(input("Enter the squeezing parameter r: "))
    phi = float(input("Enter the squeezing angle phi: "))
    return displacement_amplitude, displacement_phase, r, phi


def main():
    displacement_amplitude, displacement_phase, r, phi = get_input()

    # initialize a 2-mode quantum register
    prog = sf.Program(2)

    with prog.context as q:
        # Prepare displaced squeezed state in the first mode
        ops.Dgate(displacement_amplitude, displacement_phase) | q[0]
        ops.Sgate(r, phi) | q[0]

        # Apply 50-50 beam splitter
        ops.BSgate(pi/4, 0) | (q[0], q[1])

    # initialize a quantum simulator
    eng = sf.Engine('fock', backend_options={"cutoff_dim": 5})

    result = eng.run(prog)

    # get the state of the quantum register
    state = result.state

    # print the Wigner function of the first mode
    x = p = np.linspace(-5, 5, 100)
    W = state.wigner(0, x, p)
    plt.contourf(x, p, W)
    plt.title("Wigner function of the first mode")
    plt.xlabel("Position")
    plt.ylabel("Momentum")
    plt.show()

    # print the Wigner function of the second mode
    W = state.wigner(1, x, p)
    plt.contourf(x, p, W)
    plt.title("Wigner function of the second mode")
    plt.xlabel("Position")
    plt.ylabel("Momentum")
    plt.show()


if __name__ == "__main__":
    main()
