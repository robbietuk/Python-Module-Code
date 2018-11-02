"""
This script will take a point
The point will be accelerated due to gravity every update
This will update both the velocity and position
"""

import numpy as np
import matplotlib.pyplot as plt
import random

# Global parameters
time_scale = 0.01
t_end = int(10.0 / time_scale)  # how many iterations in for loop

gravity = np.array([[0.0 * time_scale],
                    [-0.1 * time_scale]])

my_ball_bounce_coefficient = 0.75

# Box limits
# [x_lower, x_upper], [y_lower, y_upper]
box_limits = np.array([[0, 10],
                       [0, 10]])


class ball:
    def __init__(self, box_limits, my_ball_bounce_coefficient):
        # Choose a random starting position within the box limits
        self.position = np.transpose(.5 * self.box_size() * np.random.rand(1, 2))\
                                     + np.reshape(box_limits[:, 0], [2, 1])\
                                     + 0.5 * (np.reshape(np.array([0, box_limits[1, 1] - box_limits[1, 0]]), [2, 1]))

        self.velocity = time_scale * (random.choice((-1, 1)) * (2 * np.random.rand(2, 1)))

        self.bounce_coefficient = my_ball_bounce_coefficient

    # Methods
    def box_size(self):
        return box_limits[:, 1] - box_limits[:, 0]

    def update_velocity(self):
        self.velocity = self.velocity + gravity

    def update_position(self):
        self.position = self.position + self.velocity

    def bounce(self):
        # x check
        if self.position.item(0) < box_limits.item((0, 0)):
            self.position[0] = 2 * box_limits.item((0, 0)) - self.position[0]
            self.velocity[0] = - self.bounce_coefficient * self.velocity[0]
        elif self.position.item(0) > box_limits.item((0, 1)):
            self.position[0] = 2 * box_limits.item((0, 1)) - self.position[0]
            self.velocity[0] = - self.bounce_coefficient * self.velocity[0]

        # y check
        if self.position.item(1) < box_limits.item((1, 0)):
            self.position[1] = 2 * box_limits.item((1, 0)) - self.position[1]
            self.velocity[1] = - self.bounce_coefficient * self.velocity[1]
        elif self.position.item(1) > box_limits.item((1, 1)):
            self.position[1] = 2 * box_limits.item((1, 1)) - self.position[1]
            self.velocity[1] = - self.bounce_coefficient * self.velocity[1]

    def ball_step_update(self):
        self.update_velocity()
        self.update_position()
        self.bounce()


# create my ball
my_ball = ball(box_limits, my_ball_bounce_coefficient)

path = np.zeros((2, t_end))
# Looping over iterations of ball updates
for t in range(t_end):
    my_ball.ball_step_update()
    path[:, t:t + 1] = my_ball.position  # log ball position at each iteration

# Plotting the path of the ball
plt.plot(path[0, :], path[1, :])
plt.xlim(box_limits[0, :])
plt.ylim(box_limits[1, :])
plt.show()
