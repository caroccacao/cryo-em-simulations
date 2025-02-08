import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

# Function to generate wave pattern with phase shift
def generate_wave(defocus):
    x = np.linspace(-10, 10, 500)
    y = np.linspace(-10, 10, 500)
    X, Y = np.meshgrid(x, y)

    # Simulate an electron wave with a sample-induced phase shift
    phase_shift = np.sin(2 * np.pi * (X**2 + Y**2) / 20)
    
    # Apply defocus effect by shifting the wave further
    defocused_wave = np.sin(2 * np.pi * (X**2 + Y**2) / 20 + defocus)

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    # In-focus wave (phase shifts are present but invisible)
    axes[0].imshow(phase_shift, cmap='gray', extent=[-10, 10, -10, 10])
    axes[0].set_title("In-focus: Phase shifts invisible")

    # Defocused wave (phase shifts converted to intensity contrast)
    axes[1].imshow(defocused_wave, cmap='gray', extent=[-10, 10, -10, 10])
    axes[1].set_title(f"Defocused: Phase shifts revealed (Defocus={defocus:.2f})")

    plt.show()

# Interactive widget to control defocus level
defocus_slider = widgets.FloatSlider(min=0, max=3, step=0.1, value=0, description="Defocus")
interactive_plot = widgets.interactive(generate_wave, defocus=defocus_slider)

# Display interactive plot
display(interactive_plot)
