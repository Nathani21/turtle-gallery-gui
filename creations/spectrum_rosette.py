import colorsys

COLORS = [colorsys.hsv_to_rgb(i / 36, 1, 1) for i in range(36)]
EXTENT = 210  # the drawing stays within this distance of the centre
STEP_MS = 60  # pause between steps when the gallery animates it


def draw(t):
    t.getscreen().bgcolor("black")
    t.speed(0)
    for i in range(36):
        t.color(COLORS[i])
        t.circle(100)
        t.left(10)
        yield


if __name__ == "__main__":
    import turtle
    for _ in draw(turtle.Turtle()):
        pass
    turtle.done()