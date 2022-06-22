# Plot the error surface
import numpy as np

def visualize_steps(fig, axis, log_a, log_b, x, y):
    
    # Define a grid of a,b parameters
    min_ab = min(min(log_a), min(log_b))
    max_ab = max(max(log_a), max(log_b))

    d = max_ab - min_ab
    min_ab -= d * 0.1
    max_ab += d * 0.1

    a = np.linspace(min_ab, max_ab, num=40)
    b = np.linspace(min_ab, max_ab, num=40)
    a_grid, b_grid = np.meshgrid(a, b)

    # Compute the RMSE score for each a,b pair on that grid
    rmse_grid = np.zeros_like(a_grid)

    for i in range(40):
        for j in range(40):
            a, b = a_grid[i, j], b_grid[i, j]
            rmse_grid[i, j] = rmse(a * x + b, y)

    # RMSE surface
    axis.set_aspect("equal", adjustable="box")
    mpl_contourset = axis.contourf(a_grid, b_grid, rmse_grid, 20, cmap=plt.cm.coolwarm)
    fig.colorbar(mpl_contourset, ax=axis, label="RMSE")

    # Plot the GD steps
    axis.plot(log_a, log_b, c="#00abe9")
    axis.scatter(log_a, log_b, c="#00abe9")

    # Set titles and labels
    axis.set_xlabel("parameter a")
    axis.set_ylabel("parameter b")

    axis.set_xlim(min_ab, max_ab)
    axis.set_ylim(min_ab, max_ab)