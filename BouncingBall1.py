"""
This script will take a point
The point will be accelerated due to gravity every update
This will update both the velocity and position
"""

import numpy as np
import matplotlib.pyplot as plt

# Global parameters
gravity = np.array([[0.0],
                    [-0.1]])
t_end = 20  # how many iterations in for loop

ball_bounce_coefficient = 1

path = np.zeros((2, t_end))

# Box limits
# [x_lower, x_upper], [y_lower, y_upper]
box_limits = np.array([[0, 10],
                       [0, 10]])


class ball:
    def __init__(self, box_limits, bounce_coefficient):
        # Choose a random starting position within the box limits
        self.position = np.transpose((box_limits[:, 1] - box_limits[:, 0]) * np.random.rand(1, 2) + box_limits[:, 0])

        self.velocity = np.random.rand(2, 1)

        self.bounce_coefficient = bounce_coefficient


    # Methods
    def update_velocity(self):
        self.velocity = self.velocity + gravity

    def update_position(self):
        self.position = self.position + self.velocity

    def bounce(self):
        #x check
        if self.position.item(0) < box_limits.item((0, 0)):
            self.position[0] = 2*box_limits.item((0, 0)) - self.position[0]
            self.velocity[0] = - self.velocity[0]
        elif self.position.item(0) > box_limits.item((0, 1)):
            self.position[0] = 2*box_limits.item((0, 1)) - self.position[0]
            self.velocity[0] = - self.velocity[0]

        #y check
        if self.position.item(1) < box_limits.item((1, 0)):
            self.position[1] = 2*box_limits.item((1, 0)) - self.position[1]
            self.velocity[1] = - self.velocity[1]
        elif self.position.item(1) > box_limits.item((1, 1)):
            self.position[1] = 2*box_limits.item((1, 1)) - self.position[1]
            self.velocity[1] = - self.velocity[1]



    def ball_step_update(self):
        self.update_velocity()
        self.update_position()
        self.bounce()



# create my ball
my_ball = ball(box_limits,
               ball_bounce_coefficient)

# Looping over iterations of ball updates
for t in range(t_end):
    my_ball.ball_step_update()
    path[:, t:t+1] = my_ball.position  # log ball position at each iteration


# Plotting the path of the ball
plt.plot(path[0, :], path[1, :])
#plt.axes(np.ndarray.flatten(box_limits).tolist())
plt.show()






