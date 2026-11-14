import colorsys

# Rainbow colors
COLORS = [colorsys.hsv_to_rgb(i / 36, 1, 1) for i in range(36)]
EXTENT = 215  # the drawing stays within this distance of the centre
STEP_MS = 10  # pause between steps when the gallery animates it

def draw(t):
    t.getscreen().bgcolor("black")
    t.speed(0)
    t.left(90)          # start pointing up
    t.penup()
    t.goto(0, -170)
    t.pendown()

    def branch(length, depth, color_idx):
        if depth == 0 or length < 4:
            return

        t.color(COLORS[color_idx % 36])
        t.pensize(max(1, depth // 2))
        t.forward(length)
        yield

        # right branch
        t.right(30)
        yield from branch(length * 0.7, depth - 1, color_idx + 2)

        # left branch
        t.left(60)
        yield from branch(length * 0.7, depth - 1, color_idx + 4)

        # go back
        t.right(30)
        t.penup()
        t.backward(length)
        t.pendown()

    yield from branch(120, 9, 0)

if __name__ == "__main__":
    import turtle
    for _ in draw(turtle.Turtle()):
        pass
    turtle.done()