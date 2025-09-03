# Basic RL environment and agent loop for grid navigation
class GridEnv:
    def __init__(self, terrain, start, end):
        self.terrain = terrain
        self.start = start
        self.end = end
        self.state = start
        self.height, self.width = terrain.shape
        self.actions = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]
    def reset(self):
        self.state = self.start
        return self.state
    def step(self, action):
        x, y = self.state
        dx, dy = self.actions[action]
        nx, ny = x + dx, y + dy
        if 0 <= nx < self.width and 0 <= ny < self.height:
            self.state = (nx, ny)
        # Proximity-based reward: positive reward for getting closer to end, negative for moving away
        prev_dist = ((x - self.end[0]) ** 2 + (y - self.end[1]) ** 2) ** 0.5
        new_dist = ((self.state[0] - self.end[0]) ** 2 + (self.state[1] - self.end[1]) ** 2) ** 0.5
        reward = prev_dist - new_dist  # positive if agent moves closer
        # Optionally, add a small penalty for terrain cost
        reward -= 0.01 * self.terrain[self.state[1], self.state[0]]
        done = self.state == self.end
        return self.state, reward, done

# Q-learning implementation
import numpy as np
alpha = 0.1      # learning rate
gamma = 0.99     # discount factor
epsilon = 0.1    # exploration rate
num_actions = 8
env = GridEnv(terrain, start, end)
Q = np.zeros((env.width, env.height, num_actions))

def plot_agent_path(Q, env, terrain, start, end, episode):
    state = env.reset()
    path = [state]
    done = False
    max_steps = 2000
    steps = 0
    while not done and steps < max_steps:
        x, y = state
        action = np.argmax(Q[x, y])
        next_state, reward, done = env.step(action)
        path.append(next_state)
        state = next_state
        steps += 1
    path_x, path_y = zip(*path)
    plt.figure(figsize=(8, 8))
    contour = plt.contourf(terrain, cmap='terrain', levels=50)
    plt.colorbar(contour, label='Elevation')
    plt.scatter(start[0], start[1], color='yellow', s=100, label='Start', marker='o')
    plt.scatter(end[0], end[1], color='blue', s=100, label='End', marker='o')
    plt.plot(path_x, path_y, color='purple', linewidth=2, label='Agent Path')
    plt.legend()
    plt.title(f'Agent Path at Episode {episode}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

for episode in range(1000):
    state = env.reset()
    done = False
    while not done:
        x, y = state
        # ε-greedy action selection
        if np.random.rand() < epsilon:
            action = np.random.randint(num_actions)
        else:
            action = np.argmax(Q[x, y])
        next_state, reward, done = env.step(action)
        nx, ny = next_state
        # Q-learning update
        Q[x, y, action] = Q[x, y, action] + alpha * (reward + gamma * np.max(Q[nx, ny]) - Q[x, y, action])
        state = next_state
    # Visualize progress every 100 episodes
    if (episode + 1) % 100 == 0:
        plot_agent_path(Q, env, terrain, start, end, episode + 1)

# Final learned policy visualization
plot_agent_path(Q, env, terrain, start, end, 'Final')