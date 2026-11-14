import colorsys

COLORS = [colorsys.hsv_to_rgb(i / 36, 1, 1) for i in range(36)]
EXTENT = 130  # the drawing stays within this distance of the centre
STEP_MS = 150  # pause between steps when the gallery animates it

def draw(t):
    t.getscreen().bgcolor("black")
    t.speed(0)
    t.penup()
    t.goto(0, 0)
    t.pendown()

    # Draw petals
    for i in range(12):                      # 12 petals
        t.color(COLORS[i * 3 % 36])
        t.begin_fill()
        t.circle(120, 60)                    # one side of the petal
        t.left(120)
        t.circle(120, 60)                    # other side
        t.left(120)
        t.end_fill()
        t.left(30)                           # rotate for next petal
        yield

    # Center of the flower
    t.penup()
    t.goto(0, -28)  # bottom of the centre circle, so it sits on the petals' hub
    t.pendown()
    t.color("gold")
    t.begin_fill()
    t.circle(28)
    t.end_fill()
    yield

if __name__ == "__main__":
    import turtle
    for _ in draw(turtle.Turtle()):
        pass
    turtle.done()