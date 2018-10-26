"""
This script will take a point
The point will be accelerated due to gravity every update
This will update both the velocity and position
"""

import numpy as np


# Global parameters
gravity = -0.1
t_end = 20
ball_bounce_constant = 1

# Box limits
# [x_lower, x_upper], [y_lower, y_upper]
box_limits = [[0, 10], [0, 10]]

# Initial parameters
ball_position = 5
ball_velocity = -1


def update(x, y):
    x += y
    return x


def ball_in_box_limits(ball_position, ball_velocity, box_limits):
    if update(ball_position, ball_velocity) < box_limits[1][0] or update(ball_position, ball_velocity) > box_limits[1][1]:
        return False
    else:
        return True





for _ in range(t_end):
    if not ball_in_box_limits(ball_position, ball_velocity, box_limits):
        ball_velocity = -ball_bounce_constant * ball_velocity
    ball_position = update(ball_position, ball_velocity)

    print(ball_position)

    # Gravity influence
    ball_velocity = update(ball_velocity, gravity)








