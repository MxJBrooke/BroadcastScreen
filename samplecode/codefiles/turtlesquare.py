import turtle

# Create the turtle
t = turtle.Turtle()

t.color("GREEN")

# Draw a square
for i in range(4):
    t.forward(100)  # Move forward 100 pixels
    t.right(90)     # Turn right 90 degrees

# Keep the window open
turtle.done()