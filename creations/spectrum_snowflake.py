import colorsys

COLORS = [colorsys.hsv_to_rgb(i / 36, 1, 1) for i in range(36)]
EXTENT = 185  # the drawing stays within this distance of the centre
STEP_MS = 25  # pause between steps when the gallery animates it

def draw(t):
    t.getscreen().bgcolor("black")
    t.speed(0)
    t.penup()
    t.goto(-150, 90)
    t.pendown()

    def koch_curve(length, depth, color_idx):
        if depth == 0:
            t.color(COLORS[color_idx % 36])
            t.forward(length)
            return

        length /= 3
        yield from koch_curve(length, depth - 1, color_idx)
        t.left(60)
        yield from koch_curve(length, depth - 1, color_idx + 1)
        t.right(120)
        yield from koch_curve(length, depth - 1, color_idx + 2)
        t.left(60)
        yield from koch_curve(length, depth - 1, color_idx + 3)
        if depth == 1:
            yield  # one step per small group of four segments

    # Draw the three sides of the snowflake
    for side in range(3):
        yield from koch_curve(300, 4, side * 12)
        t.right(120)

if __name__ == "__main__":
    import turtle
    for _ in draw(turtle.Turtle()):
        pass
    turtle.done()