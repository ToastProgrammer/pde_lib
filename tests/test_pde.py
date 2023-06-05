import numpy as np

from pde_lib.calculation.pde import heat_simulation, heat_simulation_comp
from pde_lib.display.graph import heatmap_3d, linegraph


def test_comp():
    """
    Alternate method, that generates a 3D mesh, to compare results against.
    """
    # Constants
    diffusivity = 0.1  # Thermal diffusivity
    L = 1.0  # Length of the domain
    T = 1.0  # Total time
    n = 100  # Number of grid points
    m = 100  # Number of time steps
    # Initialize the temperature array and set initial condition
    initial = np.zeros((n, m))
    initial[:, 0] = np.sin(np.pi * np.linspace(0, 1, n))

    space_mesh, temperature_mesh = heat_simulation_comp(n, m, L, T, diffusivity, initial)
    heatmap_3d(space_mesh, temperature_mesh, initial)


def test_orig():
    n = 100
    dt = 1/(n**2)
    T = 1.0
    diffusivity_constant = 0.01
    x = np.linspace(0, 1, num=n+1)
    u0 = np.sin(2*np.pi*x)
    u = heat_simulation(n, dt, T, diffusivity_constant, u0)
    linegraph(x, u)
