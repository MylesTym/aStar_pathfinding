# Perlin Noise Terrain & Modular A* Pathfinding

This project generates a realistic terrain using Perlin noise and visualizes it in both 2D and 3D. It implements modular A* pathfinding, allowing an agent to navigate through multiple waypoints, with animated path visualization.

## Features
- **Perlin Noise Terrain Generation:** Creates a smooth, realistic terrain using configurable parameters (scale, octaves, persistence).
- **3D and 2D Visualization:** Plots terrain as a 3D surface and 2D contour map with labeled waypoints.
- **Modular A* Pathfinding:** Finds a path from start to end, optionally passing through intermediary waypoints. Pathfinding is extensible to any number of waypoints.
- **Animated Path Visualization:** Uses matplotlib's animation tools to show the agent's path dynamically, with support for saving as GIF or MP4 (requires ffmpeg for MP4).
- **Waypoint Optimization (optional):** Can be extended to find the most optimal order to visit waypoints (Traveling Salesman Problem variant).

## Usage
1. **Install dependencies:**
	- Python 3.x
	- numpy
	- matplotlib
	- scipy
	- noise
	- ffmpeg (system package, for MP4 output)

2. **Run the notebook:**
	- Generates terrain and waypoints
	- Visualizes terrain and waypoints
	- Computes and animates the path

3. **Customize:**
	- Adjust terrain parameters for different landscapes
	- Add or remove waypoints
	- Extend pathfinding to optimize waypoint order

## Example Output
- 3D terrain plot
- 2D contour map with labeled waypoints
- Animated agent path (GIF/MP4)

## Advanced Directions
- Integrate real-world elevation data
- Compare multiple pathfinding algorithms
- Add interactive controls (e.g., with Streamlit)
- Use reinforcement learning for adaptive navigation
- Port to Unity or a game engine for real-time simulation

## Interactive 3D Terrain Visualization (pythreejs)


This feature uses [pythreejs](https://github.com/jupyter-widgets/pythreejs) to render the terrain as an interactive 3D mesh in the notebook. The mesh is colored by elevation and can be rotated, zoomed, and panned.

### Additional Functionality
- **Waypoint Markers:** Start, intermediary, and end points are displayed as colored 3D spheres directly on the mesh for clear visual reference.
- **A* Path Overlay:** The computed A* path is rendered as a red 3D line over the terrain, showing the agent's route in 3D space.
- **Improved Mesh Rendering:** Elevation variance and color mapping are enhanced for better visual contrast and clarity.

These features make the 3D visualization not only interactive, but also informative for understanding both the terrain and the pathfinding solution.

**Requirements:**
- `pythreejs` (install with `pip install pythreejs`)
- Jupyter notebook or JupyterLab

**How to use:**
- Run the relevant notebook cell to generate the mesh after terrain creation.
- Use mouse or touch to interact with the mesh (rotate, zoom, pan).

**Notes:**
- For best performance, the terrain is downsampled before mesh construction.
- Camera and controls are centered on the mesh for optimal viewing.

## Installation
```sh
pip install numpy matplotlib scipy noise
# For MP4 animation output:
brew install ffmpeg  # macOS
sudo apt-get install ffmpeg  # Ubuntu/Linux
```

## License
MIT
# aStar_pathfinding
