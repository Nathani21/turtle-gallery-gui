import colorsys

COLORS = [colorsys.hsv_to_rgb(i / 36, 1, 1) for i in range(36)]
EXTENT = 270  # the drawing stays within this distance of the centre
STEP_MS = 80  # pause between steps when the gallery animates it

def draw(t):
    t.getscreen().bgcolor("black")
    t.speed(0)
    t.pensize(2)

    # Starburst parameters
    rays = 36                 # number of rays
    length = 260              # length of each ray

    for i in range(rays):
        t.color(COLORS[i % 36])
        t.penup()
        t.goto(0, 0)
        t.pendown()

        t.setheading(i * (360 / rays))
        t.forward(length)
        yield

if __name__ == "__main__":
    import turtle
    for _ in draw(turtle.Turtle()):
        pass
    turtle.done()