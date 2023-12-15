from turtle import *
from time import sleep
from math import floor,sqrt

def square_left(x,object,n,rgb,n_ini):
    x=sqrt((x**2)/2)
    object.pu()
    object.left(45)

    object.pd()
    object.begin_fill()
    for i in range(4):
        object.forward(x)
        object.left(90)
    object.end_fill()
    object.pu()
    object.left(90)
    object.forward(x)
    object.right(90)
    object.pd()
    object.hideturtle()
    tree(n-1,x,object,rgb,n_ini)

def square_right(x,object,n,rgb,n_ini):
    object.pu()
    object.forward(x)
    object.right(45)
    x=sqrt((x**2)/2)
    object.backward(x)
    object.pd()
    object.begin_fill()
    for i in range(4):
        object.forward(x)
        object.left(90)
    object.end_fill()
    object.pu()
    object.left(90)
    object.forward(x)
    object.right(90)
    object.pd()
    object.hideturtle()
    tree(n-1,x,object,rgb,n_ini)

def tree(n,x,object,rgb,n_ini):
    if n<=0 :
        return
    rgb=[rgb[0]-floor(125/(n_ini)),rgb[1]+floor(105/(n_ini)),rgb[2]+floor(50/(n_ini))] 
    
    drawer=[Turtle(),Turtle()]
    for i in range(len(drawer)):
            drawer[i].pu()
            drawer[i].speed(0)
            drawer[i].goto(object.position())
            drawer[i].left(object.heading())
            drawer[i].color(rgb[0],rgb[1],rgb[2])
            drawer[i].pd()
    square_left(x,drawer[0],n,rgb,n_ini)
    square_right(x,drawer[1],n,rgb,n_ini)

def start(n,x):
    rgb=[125,50,0]
    object=Turtle()
    object.speed(0)
    object.color(rgb[0],rgb[1],rgb[2])
    object.pu()
    object.goto(-100,-200)
    object.pd()
    object.begin_fill()
    for _ in range(4):
        object.forward(x)
        object.left(90)
    object.end_fill()
    object.pu()
    object.left(90)
    object.forward(x)
    object.right(90)
    object.pd()
    tree(n,x,object,rgb,n+1)

colormode(255)

number_iteration = int(input("Choose the number of iteration : "))
length = 150
reduction = sqrt((length**2)/2)

start(number_iteration,length)

mainloop()

