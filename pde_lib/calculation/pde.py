from dataclasses import dataclass, field
import numpy as np
import matplotlib.pyplot as plt
from typing import Callable, Tuple, Union, Dict, Optional, Iterable

"""
Functionality that involves finding solutions to Partial Differential Equations.
"""


def heat_simulation(
        n: int,
        dt: float,
        time_total: float,
        diffusivity: float,
        initial_condition: np.ndarray
) -> np.ndarray:
    """
    Simulate the heat equation using the given parameters.
    :param n: the number of discrete points over length to use
    :param dt: difference between two adjacent, discrete points in time
    :param time_total: total period of time to solve over
    :param diffusivity: the diffusion constant
    :param initial_condition: the initial condition to use

    :return: the final state of the simulation
    """
    id_matrix = np.eye(n-1)     # (n-1) x (n-1) Identity matrix
    A = diffusivity * n**-2 * (np.eye(n-1, k=-1) + (-2)*np.eye(n-1, k=0) + np.eye(n-1, k=1))
    B = dt*A + id_matrix
    u = initial_condition[1:-1]     # Remove boundaries so they aren't evaluated
    time_interval = np.int64(np.ceil(time_total/dt))
    for _ in range(time_interval):
        u = B @ u
    u = np.concatenate(([0], u, [0]))   # Re-add boundaries
    return u


def heat_simulation_comp(
        n: int,
        m: int,
        length_total: float,
        time_total: float,
        diffusivity: float,
        initial: np.ndarray,
) -> Tuple[np.ndarray, np.ndarray]:
    # Discretization parameters
    dx_stride = length_total / (n - 1)
    dt_stride = time_total / m

    u = initial.copy()

    # Solve the heat equation using finite differences
    for x in range(0, m - 1):
        for i in range(1, n - 1):
            u[i, x + 1] = u[i, x] + diffusivity * dt_stride / dx_stride**2 * (u[i - 1, x] - 2 * u[i, x] + u[i + 1, x])

    # Plot the results
    position_array = np.linspace(0, length_total, n)
    temperature_array = np.linspace(0, time_total, m)
    return np.meshgrid(position_array, temperature_array)
