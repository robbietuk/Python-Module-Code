import numpy as np
from matplotlib import animation
from matplotlib import pyplot as plt
import HTML

# Constants
bird_count = 10
initial_lower_limit = np.array([200, 800])
initial_upper_limit = np.array([500, 1200])
box_limits = np.array([2000, 2000])[:, np.newaxis]


def new_flock(count, lower_limit, upper_limit):
    width = upper_limit - lower_limit
    return lower_limit[:, np.newaxis] + np.random.rand(2, count) * width[:, np.newaxis]


position = new_flock(bird_count, initial_lower_limit, initial_upper_limit)
velocity = new_flock(bird_count, np.array([0, -20]), np.array([10, 20]))

# Setup the plot
figure = plt.figure()
axes = plt.axes(xlim=(0, box_limits[0, 0]), ylim=(0, box_limits[1, 0]))
scatter = axes.scatter(position[0, :], position[1, :], marker='o', edgecolor='k', lw=0.5)


def update_bird(position, velocity):
    position += velocity

def animate(frame):
    update_bird(position, velocity)
    scatter.set_offsets(position.transpose())

anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)

anim.save('boids_1.mp4')

HTML(anim.to_jshtml())