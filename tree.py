import turtle as tr
# import random


def draw(source: str, angle: float, segment: int, pensize: int, stack):
    tr.pu()
    tr.left(90)
    tr.sety(tr.ycor()-400)
    tr.color("green")
    tr.ht()
    tr.pensize(pensize)
    tr.speed(0)
    tr.pd
    for symbol in source:
        if symbol == "F":
            tr.fd(segment)
        elif symbol == "+":
            tr.left(angle)
        elif symbol == "-":
            tr.right(angle)
        elif symbol == "[":
            push(stack, tr.pensize())
            tr.pensize(int(tr.pensize()/2))
        elif symbol == "]":
            pop(stack)
    tr.done()
    return None


def pop(stack):
    tr.pu()
    pos, angle, pensize = stack.pop()
    tr.seth(angle)
    tr.setpos(pos)
    tr.pensize(pensize)
    tr.pd()
    return None


def push(stack: list, pensize: int):
    stack.append([tr.pos(), tr.heading(), pensize])
    return None
