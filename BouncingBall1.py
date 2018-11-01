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


# Initial parameters
# in x, y

class ball:
    def __init__(self, name, box_limits, bounce_coefficient):
        self.name = name

        # Set position as a random point within the box limits
        self.position = np.transpose((box_limits[:, 1] - box_limits[:, 0]) * np.random.rand(1, 2) + box_limits[:, 0])
        self.velocity = np.random.rand(2, 1)
        self.bounce_coefficient = bounce_coefficient

        # self.ball_path = np.zeros((2, t_end))

    def say_hi(self):
        print("Hi, my name is ", self.name)

    def update_velocity(self):
        self.velocity = self.velocity + gravity

    def update_position(self):
        self.position = self.position + self.velocity

    def ball_update(self):
        self.update_position()
        self.update_velocity()


# create my ball
my_ball = ball("my_ball",
               box_limits,
               ball_bounce_coefficient)




for t in range(t_end):
    my_ball.ball_update()
    path[:, t:t+1] = my_ball.position
    print("Pos. = ", my_ball.position)


plt.plot(path[0, :], path[1, :], 'ro')
plt.axes([0, 10, 0 , 10])
plt.show()

"""




print(ball_velocity)
print(update_ball(ball_velocity, gravity))


def ball_in_box_limits(ball_position, ball_velocity, box_limits):

    #x axis position check
    if update_ball(ball_position, ball_velocity)[0] < box_limits[0, 0] or update_ball(ball_position, ball_velocity)[0] > box_limits[0, 1]:



    if update_ball(ball_position, ball_velocity) < box_limits[1, :] \
            or update_ball(ball_position, ball_velocity) > box_limits[1, 1]:
        return False
    else:
        return True





for _ in range(t_end):
    if not ball_in_box_limits(ball_position, ball_velocity, box_limits):
        ball_velocity = -ball_bounce_constant * ball_velocity  # the ball bounces if would be out of range
    ball_position = update_ball(ball_position, ball_velocity)

    print(ball_position)

    # Gravity influence
    ball_velocity = update_ball(ball_velocity, gravity)



"""
