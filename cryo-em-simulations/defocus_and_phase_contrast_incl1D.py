import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

def generate_thon_rings(defocus):
    """Generate a simulated Thon ring pattern with defocus."""
    # Define image size and frequency space
    size = 500  # Image size in pixels
    center = size // 2  # Center of the image
    max_rings = 8  # Maximum number of Thon rings

    # Create a grid in frequency space
    x = np.linspace(-1, 1, size)
    y = np.linspace(-1, 1, size)
    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2)  # Radial distance

    # Simulate Thon rings: sin waves modulated by defocus
    thon_rings = np.sin(2 * np.pi * max_rings * R + defocus) * np.exp(-10 * R)

    # Compute 1D radial average
    r_vals = np.linspace(0, 1, 100)
    radial_avg = [np.mean(thon_rings[(R >= r - 0.01) & (R < r + 0.01)]) for r in r_vals]

    # Create figure with two plots: 2D Thon rings and 1D radial average
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Show Thon rings
    axes[0].imshow(thon_rings, cmap='gray', extent=[-1, 1, -1, 1])
    axes[0].set_title(f"Simulated Thon Rings (Defocus={defocus:.2f})")
    axes[0].set_xticks([])
    axes[0].set_yticks([])

    # Plot radial average
    axes[1].plot(r_vals, radial_avg, color='black')
    axes[1].set_title("1D Radial Average of Thon Rings")
    axes[1].set_xlabel("Spatial Frequency")
    axes[1].set_ylabel("Intensity")

    plt.show()

# Interactive widget to control defocus level
defocus_slider = widgets.FloatSlider(min=0, max=3, step=0.1, value=0, description="Defocus")
interactive_plot = widgets.interactive(generate_thon_rings, defocus=defocus_slider)

# Display interactive plot
display(interactive_plot)
