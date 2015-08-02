import turtle

def draw_shapes():
    window=turtle.Screen()
    window.bgcolor("black")

    draw_circle()
    draw_square()

    window.exitonclick()
    
def draw_circle():
    john=turtle.Turtle()
    john.shape("turtle")
    john.color("green")
    john.speed("slow")
    john.circle(100)


def draw_square():
    raphael=turtle.Turtle()
    raphael.shape("turtle")
    raphael.color("red")
    raphael.speed("slow")
    i=0
    while(i<4):
        raphael.forward(100)
        raphael.right(90)
        i=i+1
    


draw_shapes()
