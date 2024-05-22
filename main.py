from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# Flag to control continuous movement
is_moving = False

def move_forward():
    if is_moving:
        tim.forward(10)
        screen.ontimer(move_forward, 100)  # Call move_forward every 100 ms

def start_moving():
    global is_moving
    is_moving = True
    move_forward()

def stop_moving():
    global is_moving
    is_moving = False

def move_backward():
    tim.backward(10)

def move_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()

"""
Here is the reason why without parenthesis 👇

screen.onkey(key = "space", fun = move_forward()) 
screen.onkey(key = "space", fun = move_forward) 

When you pass a function to another function (such as setting up an event listener), you generally pass the function's 
name without parentheses to provide a reference to the function itself. This allows the function to be called later in 
response to an event, rather than being called immediately when the program runs.

This concept is a crucial part of event-driven programming, which is commonly used in graphical user interfaces (GUIs) 
and game development.
"""
# Another explanation
"""
Functions as Input 

def function_a(something):
    #Do this with something
    #Then do this 
    #Finally do this 
    
def function_b():
    #Do this
    
function_a(function_b)

So notice that when we pass a function as an input,
we only pass the name without the parenthesis in the end

"""
# Event listeners
screen.onkeypress(start_moving, "w")
screen.onkeyrelease(stop_moving, "w")
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "a", fun = move_left)
screen.onkey(key = "d", fun = move_right)

screen.onkey(clear, "c")
screen.exitonclick()