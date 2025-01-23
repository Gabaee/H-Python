"""
This program creats a shape of alternating yellow squares and orange circles.
"""

speed(10)
bgcolor("black")
pensize(2)

# Creates the shape
def draw_shape():
    # The variables
    side_length = 10
    radius = 10
    count_variable = 1
    # For loop that creats the alternating effect
    for i in range(5):
        # Uses modulus to determine if the count variable is odd
        if count_variable % 2 != 0:
            color("yellow")
            circle(side_length, 360, 4)
            count_variable = count_variable + 1
            # Adds 10 lenfth to tge side length each pass
            side_length = side_length + 10
        # Uses modulus to determine if the count variable is even
        if count_variable % 2 == 0:
            color("orange")
            circle(-radius)
            # Adds 10 length to the radius each pass
            radius = radius + 10
            count_variable = count_variable - 1

# Draws the shape    
draw_shape()
