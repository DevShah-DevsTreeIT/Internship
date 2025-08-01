import turtle
import math

def draw_circle(t, color,x, y,radius ):
    t.penup()
    t.goto(x,y - radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draaw_solor_system():
    screen = turtle.Screen()
    screen.bgcolor("black") 
    screen.title("Solar System")

    t = turtle.Turtle()
    t.speed(0)

    # Draw sun
    draw_circle(t,"yellow", 0, 0, 50)

    # Planets(approxmate orbits and sizes)
    planets = [
        ("gray",80, 8), #Mercury
        ("orange",120,12), #Venus
        ("blue",170, 14), #Earth
        ("red",220, 10), #Mars
        ("brown",300, 30), #Jupiter
        ("lightblue",400, 25), #Saturn
        ("cyan",500, 20), #Uranus
        ("blue",600, 18) #Neptune
    ]

    for color,distance, radius in planets:
        draw_circle(t, color, distance, 0 , radius)

    t.hideturtle()
    screen.mainloop()

# run the function
draaw_solor_system()

