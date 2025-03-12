print("day 0 homework")
from turtle import *

#drawing square
width(7)
color("red")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#end of square 

#drawing a door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
#end of the door 

#windows 

#first window

color("black")
begin_fill()
penup() 
goto(140, 140)
pendown()

left(90)
forward(40)
left(90)
forward(40)
left(90) 
forward(40)
left(90)
forward(40)
end_fill()
   
#second window 
color("black")
begin_fill()
penup() 
goto(40, 140)
pendown()

left(90)
forward(40)
left(90)
forward(40)
left(90) 
forward(40)
left(90)
forward(40)
end_fill()

#drawing roof

penup()
goto(200,200)
pendown()

color("blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()