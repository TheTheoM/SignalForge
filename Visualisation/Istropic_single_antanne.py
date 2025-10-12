import numpy as np
import matplotlib.pyplot as plt

grid_size = 500  # Size of the grid for the heatmap
center = (grid_size // 2, grid_size // 2)  # Center of the antenna
max_distance = 100  # Max distance from the center for visualization

x = np.linspace(-max_distance, max_distance, grid_size)
y = np.linspace(-max_distance, max_distance, grid_size)
X, Y = np.meshgrid(x, y)

R = np.sqrt(X**2 + Y**2)

R[R == 0] = np.nan

signal_strength = 1 / R**2

normalized_strength = np.log10(signal_strength + 1e-10)  # Log 0 avoidance.

# Plot the heatmap
plt.figure(figsize=(8, 6))
plt.imshow(
    normalized_strength, 
    extent=(-max_distance, max_distance, -max_distance, max_distance), 
    origin='lower', 
    cmap='hot'
)
plt.colorbar(label='Log(Signal Strength)')
plt.title('Isotropic Antenna Signal Strength (Inverse Square Law)')
plt.xlabel('X Distance')
plt.ylabel('Y Distance')
plt.grid(False)
plt.show()
