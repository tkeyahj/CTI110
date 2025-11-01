# T'Keyah Jefferies
# 10/27/2025
# P4LAB1b_JefferiesTkeyah.py
# Draws initials T and J using Turtle graphics

import turtle

t = turtle.Turtle()
t.speed(2)
t.pensize(6)
t.color("purple")

# ---- T ----
t.penup()
t.goto(-100, 100)
t.setheading(0)     
t.pendown()
t.forward(120)      
t.backward(60)  
t.right(90)            
t.forward(160)         

# ---- J ----
t.penup()
t.goto(60, 100)        
t.setheading(0)        
t.pendown()
t.forward(90)         
t.backward(45)         
t.right(90)            
t.forward(140)         

t.right(90)            
t.forward(40)          
t.right(90)
t.forward(12)

turtle.done()
