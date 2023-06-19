"""
Utilities for graphing PDE solutions.
"""
import matplotlib.pyplot as plt
import numpy as np


def heatmap_3d(
        x_vals: np.ndarray,
        y_vals: np.ndarray,
        z_vals: np.ndarray,
        x_name: str = "Position",
        y_name: str = "Time",
        z_name: str = "Temperature",
) -> None:
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(x_vals, y_vals, z_vals, cmap='viridis')
    ax.set_xlabel(x_name)
    ax.set_ylabel(y_name)
    ax.set_zlabel(z_name)
    plt.show()


def linegraph(
        x_vals: np.ndarray,
        y_vals: np.ndarray,
        x_name: str = "Position",
        y_name: str = "Temperature",

) -> None:
    plt.plot(x_vals, y_vals)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.show()
