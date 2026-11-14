import colorsys

COLORS = [colorsys.hsv_to_rgb(i / 36, 1, 1) for i in range(36)]
EXTENT = 175  # the drawing stays within this distance of the centre
STEP_MS = 20  # pause between steps when the gallery animates it

def draw(t):
    t.getscreen().bgcolor("black")
    t.speed(0)
    t.penup()
    t.goto(-160, -140)
    t.pendown()

    def sierpinski(length, depth, color_idx):
        if depth == 0:
            # Draw a filled triangle
            t.color(COLORS[color_idx % 36], COLORS[color_idx % 36])
            t.begin_fill()
            for _ in range(3):
                t.forward(length)
                t.left(120)
            t.end_fill()
            yield
            return

        # Three smaller triangles
        yield from sierpinski(length / 2, depth - 1, color_idx)
        t.forward(length / 2)
        yield from sierpinski(length / 2, depth - 1, color_idx + 3)
        t.backward(length / 2)
        t.left(60)
        t.forward(length / 2)
        t.right(60)
        yield from sierpinski(length / 2, depth - 1, color_idx + 6)
        t.left(60)
        t.backward(length / 2)
        t.right(60)

    yield from sierpinski(320, 5, 0)

if __name__ == "__main__":
    import turtle
    for _ in draw(turtle.Turtle()):
        pass
    turtle.done()