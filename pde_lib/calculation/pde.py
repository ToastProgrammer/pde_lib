"""
Functionality that involves finding solutions to Partial Differential Equations.
"""
from dataclasses import dataclass, field
import numpy as np
import matplotlib.pyplot as plt
from typing import Callable, Tuple, Union, Dict, Optional, Iterable


def solve_fw_euler(
        num_dx: int,
        num_dt: int,
        time_total: float,
        diffusivity: float,
        initial_condition: np.ndarray
) -> np.ndarray:
    """
    Simulate the heat equation using the given parameters.
    :param num_dx: the number of discrete points over length to use
    :param num_dt: the number of discrete time points over time_total to evaluate
    :param time_total: total period of time to solve over
    :param diffusivity: the diffusion constant
    :param initial_condition: the initial values of the system

    :return: 2-D array of the system temperature at the given spatial and time intervals
    """
    id_matrix = np.eye(num_dx - 1)     # (n-1) x (n-1) Identity matrix
    A = diffusivity * num_dx ** 2 * (
            np.eye(num_dx - 1, k=-1) + (-2) * np.eye(num_dx - 1, k=0) + np.eye(num_dx - 1, k=1)
    )
    # B = delta_t * A + I
    B = (time_total / num_dt) * A + id_matrix

    # Inital step
    u = np.zeros((num_dt - 1, num_dx - 1))
    u[0] = B @ initial_condition[1:-1]
    for time_step in range(1, num_dt-1):
        u[time_step] = B @ u[time_step-1]

    retval = np.zeros((num_dt, num_dx))
    retval[1:, 1:] = u
    return retval
