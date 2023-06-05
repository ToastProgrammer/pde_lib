import matplotlib.pyplot as plt
import numpy as np


def heatmap_3d(
        position: np.ndarray,
        temperature: np.ndarray,
        time: np.ndarray,
) -> None:
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(position, temperature, time, cmap='viridis')
    ax.set_xlabel('Position')
    ax.set_ylabel('Temperature')
    ax.set_zlabel('Time')
    plt.show()


def linegraph(
        position: np.ndarray,
        temperature: np.ndarray,
) -> None:

    plt.plot(position, temperature)
    plt.xlabel('Position')
    plt.ylabel('Temperature')
    plt.show()
