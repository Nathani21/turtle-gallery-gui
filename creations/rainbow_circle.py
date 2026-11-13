import colorsys

COLORS = [colorsys.hsv_to_rgb(i / 36, 1, 1) for i in range(36)]


def draw(t):
    t.getscreen().bgcolor("black")
    t.speed(0)
    for i in range(36):
        t.color(COLORS[i])
        t.circle(100)
        t.left(10)


if __name__ == "__main__":
    import turtle
    draw(turtle.Turtle())
    turtle.done()