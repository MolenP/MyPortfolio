from turtle import *

def teleport(x,y):
    penup()
    goto(x,y)
    pendown()

teleport(-300, 0)
begin_fill()
for i in range(3):
    forward(100)
    right(120)
end_fill()
#2---------------------------------------------
teleport(-100, 0)
for i in range(5):
    forward(100)
    right(72)
#3 - Circle ---------------------------------------------
teleport(200, 0)
color("red")

begin_fill()
right(180)
circle(100)
end_fill()
#M letter------------------------------------------------
teleport(150, -150)
pensize(20)
color("white")

right(90)
forward(100)
right(135)
forward(70)
left(90)
forward(70)
right(135)
forward(100)

#Marmok------------------------------------------------
teleport(200, -250)
color("red")
write("Marmok", align="Center", font=("Arial", 20, "bold"))

teleport(200, -300)

exitonclick()