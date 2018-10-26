"""
This script will take a point
The point will be accelerated due to gravity every update
This will update both the velocity and position
"""

# Global parameters
acceleration = -1
t_end = 20

# Box limits
x_upper = 10
x_lower = 0
y_upper = 10
y_lower = 0

# Initial parameters
position = 5
velocity = -1

def update(x, y):
    x += y
    return x


for _ in range(t_end):
    # for ensuring the ball doesnt escape the box
    if update(position, velocity) < y_lower or update(position, velocity) > y_upper:
        velocity = -velocity
    position = update(position, velocity)






