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
