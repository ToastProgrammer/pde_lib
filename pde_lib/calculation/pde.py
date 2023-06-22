"""
Functionality that involves finding solutions to Partial Differential Equations.
"""
import numpy as np


def solve_fw_euler(
        num_dx: int,
        num_dt: int,
        time_total: float,
        diffusivity: float,
        initial_condition: np.ndarray
) -> np.ndarray:
    """
    Approximate solution for PDE using Forward-Euler method
    :param num_dx: number of discrete points over length to use
    :param num_dt: number of discrete points over time period to use
    :param time_total: interval of time to use in modeling PDE solution
    :param diffusivity: diffusion constant
    :param initial_condition: initial values of the system at each x-position

    :return: 2-D array of the system temperature at given [position, time] intervals
    """
    id_matrix = np.eye(num_dx - 1)     # (n-1) x (n-1) Identity matrix
    A = diffusivity * num_dx ** 2 * (
            np.eye(num_dx - 1, k=-1) + (-2) * np.eye(num_dx - 1, k=0) + np.eye(num_dx - 1, k=1)
    )
    # B = delta_t * A + I
    B = (time_total / num_dt) * A + id_matrix

    # Initial step
    u = np.zeros((num_dt - 1, num_dx - 1))
    u[0] = B @ initial_condition[1:-1]
    for time_step in range(1, num_dt-1):
        u[time_step] = B @ u[time_step-1]

    retval = np.zeros((num_dt, num_dx))
    retval[1:, 1:] = u
    return retval
