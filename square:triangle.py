
# T'Keyah Jefferies
# 10/27/2025
# P4LAB1a_JefferiesTkeyah.py
# Draws a square and a triangle with loops

import turtle

t = turtle.Turtle()
t.speed(2)

# Draw square
for i in range(4):
    t.forward(100)
    t.right(90)

# Draw triangle
for i in range(3):
    t.forward(100)
    t.left(120)

turtle.done()
