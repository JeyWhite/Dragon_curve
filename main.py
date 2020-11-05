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
defs.draw(res, 90, int(80 / iterations))
turtle.done()
