from turtle import *

speed(30)
width(7)

color("blue")
# build a littel house
forward(120)
left(90)
forward(120)
left(90)
forward(120)
left(90)
forward(120)
left(90)
forward(40)
left(90)
# build red door
color("red")
begin_fill()
forward(60)
right(90)
forward(40)
right(90)
forward(60)
end_fill()

# make yellow roof

penup()
goto(120, 120)
pendown()

color("yellow")
begin_fill()
right(150)
forward(120)
left(120)
forward(120)
end_fill()

# draw a brown window

penup()
goto(35, 65)
pendown()

width("2")

color("brown")
right(150)
forward(40)
left(90)
forward(35)
left(90)
forward(40)
left(90)
forward(35)
left(90)
forward(19)
left(90)
forward(35)
right(90)
forward(21)
right(90)
forward(17)
right(90)
forward(40)

# draw second window

penup()
goto(115, 65)
pendown()

width("2")

color("brown")
right(180)
forward(40)
left(90)
forward(36)
left(90)
forward(40)
left(90)
forward(36)
left(90)
forward(19)
left(90)
forward(36)
right(90)
forward(21)
right(90)
forward(19)
right(90)
forward(40)



exitonclick()