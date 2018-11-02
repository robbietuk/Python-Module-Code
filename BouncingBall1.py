"""
This script will take a point
The point will be accelerated due to gravity every update
This will update both the velocity and position
"""

import numpy as np
import matplotlib.pyplot as plt
import random

# Global parameters
no_balls = 10
timescale = 0.01
t_end = int(10.0 / timescale)  # how many iterations in for loop

gravity = np.array([[0.0 * timescale],
                    [-0.1 * timescale]])

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

        self.path = np.zeros((2, t_end))

        self.velocity = timescale * (random.choice((-1, 1)) * (5 * np.random.rand(2, 1)))

        self.bounce_coefficient = my_ball_bounce_coefficient

    # Methods
    def box_size(self):
        return box_limits[:, 1] - box_limits[:, 0]

    def update_velocity(self):
        self.velocity = self.velocity + gravity

    def update_position(self, t):
        self.position = self.position + self.velocity
        self.path[:, t:t+1] = self.position

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

    def ball_step_update(self, t):
        self.update_velocity()
        self.update_position(t)
        self.bounce()


# create ball_list

ball_list = np.empty(no_balls).tolist()
for i in range(no_balls):
    ball_list[i] = ball(box_limits, my_ball_bounce_coefficient)

# Looping over iterations of ball updates
for ball in ball_list:
    for t in range(t_end):
        ball.ball_step_update(t)

    plt.plot(ball.path[0, :], ball.path[1, :])

# Plotting the path of the ball

plt.xlim(box_limits[0, :])
plt.ylim(box_limits[1, :])
plt.show()