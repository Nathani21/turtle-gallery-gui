COLORS = ["red", "yellow", "blue", "green", "purple", "orange"]
EXTENT = 400  # the drawing stays within this distance of the centre
STEP_MS = 20  # pause between steps when the gallery animates it


def draw(t):
    t.getscreen().bgcolor("black")
    t.speed(0)
    for i in range(200):
        t.color(COLORS[i % len(COLORS)])
        t.circle(i)
        t.left(59)
        yield


if __name__ == "__main__":
    import turtle
    for _ in draw(turtle.Turtle()):
        pass
    turtle.done()