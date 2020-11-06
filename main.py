import turtle
import defs


Current_Rules = {"X": "X+YF+", "Y": "-FX-Y"}
print("Вбей количество итераций:")
iterations = int(input())
res = defs.processing("FX", Current_Rules, iterations)
print(res) # for debugging
turtle.speed(0)
turtle.bgcolor("black")
turtle.pencolor("blue")
turtle.ht()
turtle.pensize(2)
# defs.
# defs.square_draw(res, 90, int(20 / iterations))
turtle.done()
