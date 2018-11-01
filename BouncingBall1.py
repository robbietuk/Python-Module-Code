"""
This script will take a point
The point will be accelerated due to gravity every update
This will update both the velocity and position
"""

import numpy as np


# Global parameters
gravity = np.array([0, -0.1])
t_end = 20
ball_bounce_constant = 1

# Box limits
# [x_lower, x_upper], [y_lower, y_upper]
box_limits = np.array([[0, 10], [0, 10]])

# Initial parameters
# in x, y

class ball:
    def __init__(self, position, velocity, bounce_coefficient):
        self.position = position
        self.velocity = velocity
        self.bounce_coefficient = bounce_coefficient
        self.velocity_update = velocity + gravity

my_ball = ball(np.array([5, 5]), np.array([0,1]), 1.0)




def update_ball(x, y):
    return x + y







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




