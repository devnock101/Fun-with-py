import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor('red')

    rick = turtle.Turtle()
    rick.speed(100)
    rick.color("yellow")
    j = 360
    while j > 0:    
        rick.right(360 - j)
        i = 4
        while i > 0:
            rick.forward(100)
            rick.right(90)
            i -= 1
        j -= 2
    window.exitonclick()


draw_square()