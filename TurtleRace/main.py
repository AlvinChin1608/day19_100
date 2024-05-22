from turtle import Turtle, Screen
import random

# Set up the screen dimensions
screen = Screen()
screen.setup(width=500, height=400)

# Get user input for which color turtle they bet on (converted to lowercase for case-insensitive comparison)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

# Define available turtle colors
colors = ["red", "orange", "brown", "green", "blue", "purple"]

# Define starting y positions for each turtle (spaced out evenly)
y_position = [-100, -50, 0, 50, 100, 150]

# Create a list to store all the turtle objects
all_turtle = []

# Create 6 turtles with their shapes, colors, and starting positions
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")  # Create a turtle object with turtle shape
    new_turtle.penup()                    # Lift the pen to avoid drawing while positioning
    new_turtle.color(colors[turtle_index])  # Set the turtle's color
    new_turtle.goto(x=-220, y=y_position[turtle_index])  # Move the turtle to its starting position
    all_turtle.append(new_turtle)         # Add the turtle object to the list

# Flag to control the race loop
is_race_on = False

# Start the race only if the user placed a bet
if user_bet:
    is_race_on = True

# Main race loop that continues until a winner is determined
while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230 and turtle.xcor() < 250:
            is_race_on = False
            winning_color = turtle.pencolor()  # Get the winning turtle's color

            if winning_color == user_bet:
                print(f"You have won! {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

            # This line prints both the pen color and the turtle color
            print(turtle.color())

        # Move the turtle forward by a random distance between 0 and 10
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Listen for clicks to close the screen after the race
screen.listen()
screen.exitonclick()
