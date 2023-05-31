import numpy as np
import matplotlib.pyplot as plt

from pde_lib.calculation.pde import heat_simulation


if __name__ == "__main__":
    n = 50
    dt = 1/(n**2)
    T = 1
    diffusivity_constant = 0.01
    x = np.linspace(0, 1, num=n+1)
    u0 = np.sin(2*np.pi*x)
    x = -x * (x-1) * np.exp(-x) * np.sin(2*np.pi*x)
    u = heat_simulation(n, dt, T, diffusivity_constant, u0)
    plt.plot(x, u)
    plt.ylabel("Temperature")
