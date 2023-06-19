import numpy as np

from pde_lib.calculation.pde import solve_fw_euler
from pde_lib.display.graph import heatmap_3d


def test_fw_euler_3d():
    """
    Test solving PDE using forward Euler method with a diffusivity constant across a 1-dimensional line over fixed time
    """
    # Constants
    diffusivity = 0.01  # Thermal diffusivity
    len_total = 1.0  # Length of the domain
    time_total = 1.0  # Total time
    num_dx = 100  # Number of discrete position steps over 1d line
    num_dt = 200  # Number of time steps

    # Initialize the temperature array and set initial condition
    initial = np.sin(2*np.pi*np.linspace(0, 1, num=num_dx+1))
    u = solve_fw_euler(num_dx, num_dt, time_total, diffusivity, initial)

    pos_arr = np.linspace(0, len_total, num=num_dx)
    time_arr = np.linspace(0, time_total, num=num_dt)

    pos_mesh, time_mesh = np.meshgrid(pos_arr, time_arr)

    heatmap_3d(pos_mesh, time_mesh, u)


if __name__ == "__main__":
    test_fw_euler_3d()
