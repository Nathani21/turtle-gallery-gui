import colorsys
import math

COLORS = [colorsys.hsv_to_rgb(i / 36, 1, 1) for i in range(36)]
EXTENT = 145  # the drawing stays within this distance of the centre
STEP_MS = 20  # pause between steps when the gallery animates it

def draw(t):
    t.getscreen().bgcolor("black")
    t.speed(0)
    t.pensize(2)

    # Classic spirograph parameters
    R = 120          # fixed circle radius
    r = 50           # moving circle radius
    d = 70           # distance from center of moving circle

    t.penup()
    # Start position
    x = (R - r) * math.cos(0) + d * math.cos((R - r) / r * 0)
    y = (R - r) * math.sin(0) - d * math.sin((R - r) / r * 0)
    t.goto(x, y)
    t.pendown()

    steps = 360 * 5          # the curve closes after 5 turns
    for i in range(steps + 1):
        angle = i * (2 * math.pi / 360)
        x = (R - r) * math.cos(angle) + d * math.cos((R - r) / r * angle)
        y = (R - r) * math.sin(angle) - d * math.sin((R - r) / r * angle)

        t.color(COLORS[i // 50 % 36])
        t.goto(x, y)

        if i % 8 == 0:       # yield every few steps so animation isn’t too slow
            yield

if __name__ == "__main__":
    import turtle
    for _ in draw(turtle.Turtle()):
        pass
    turtle.done()