COLORS = ["red", "yellow", "blue", "green", "purple", "orange"]


def draw(t):
    t.getscreen().bgcolor("black")
    t.speed(0)
    for i in range(200):
        t.color(COLORS[i % len(COLORS)])
        t.circle(i)
        t.left(59)


if __name__ == "__main__":
    import turtle
    draw(turtle.Turtle())
    turtle.done()