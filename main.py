import turtle
import defs


Current_Rules = {"X": "X+YF+", "Y": "-FX-Y"}
colors = {"blue","red","green","yellow"}
print("Вбей количество итераций:")
iterations = int(input())
res = defs.processing("FX", Current_Rules, iterations)
print(res) # for debugging
turtle.speed(0)
turtle.bgcolor("black")
turtle.ht()
turtle.pensize(2)
for curve in colors:
    turtle.pu()
    turtle.setpos(0,0)
    turtle.right(90)
    turtle.pencolor(curve)
    turtle.pd()
    # расскоментируй стиль отрисовки
    # defs.curved_draw(res, 90, int(20 / iterations))
    defs.square_draw(res, 90, int(80 / iterations))
turtle.done()
