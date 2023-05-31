from dataclasses import dataclass, field
import numpy as np
import matplotlib.pyplot as plt
from typing import Callable, Tuple, Union, Dict, Optional

"""
Functionality that involves finding solutions to Partial Differential Equations.
"""

def heat_simulation(n: int, dt: float, T: int, initial_condition, dfs_c: float = 1) -> float:
    """
    Simulate the heat equation using the given parameters.
    :param n: the number of points to simulate
    :param dt: the time step to use
    :param dfs_c: the diffusion constant
    :param initial_condition: the initial condition to use

    :return: the final state of the simulation
    """
    I = np.eye(n-1) # (n-1) x (n-1) Identity matrix
    A = (dfs_c * n**2) * (np.eye(n-1,k=-1) + -2*np.eye(n-1) + np.eye(n-1,k=1))
    B = dt*A + I
    u = initial_condition.copy()[1:-1]
    num_steps = np.int64(np.ceil(T/dt))
    for _ in range(num_steps):
        u = B @ u
    u = np.concatenate(([0], u, [0]))
    return u

def backward_euler(n: int, dt: float, T: int, difc: float = 1, initial_condition=None) -> float:
    """
    Simulate the heat equation using the given parameters using the backwards euler method.
    :param n: the number of points to simulate
    :param dt: the time step to use
    :param difc: the diffusion constant
    :param initial_condition: the initial condition to use

    :return: the final state of the simulation
    """
    pass
    # TODO: implement this
    # temporary code:
    ## for _ in range(num_steps):
    ##    u = np.linalg.solve(B, u)
    ## u = np.concatenate(([0], u, [0]))
    ## return u
    