# https://habr.com/ru/post/69989/
# https://habr.com/ru/company/piter/blog/496538/

import tree
import rewriting as rw


# import dragon_curve

# Current_Rules = {"X": "X+YF+", "Y": "-FX-Y"}
# colors = {"blue", "red", "green", "gold"}
# print("Вбей количество итераций:")
# iterations = int(input())
# res = dragon_curve.processing("FX", Current_Rules, iterations)
# print(res)  # for debugging
# turtle.speed(0)
# turtle.bgcolor("black")
# turtle.ht()
# turtle.pensize(1)
# for color in colors:
#     turtle.pu()
#     turtle.setpos(0, 0)
#     turtle.right(90)
#     turtle.pencolor(color)
#     turtle.pd()
#     # расскоментируй стиль отрисовки
#     # defs.curved_draw(res, 90, int(20 / iterations))
#     dragon_curve.square_draw(res, 90, int(80 / iterations))
# turtle.done()
# tr.left(90)
# print(tr.heading())
# tr.done()

def main():
    sets = [("F", 22.5), ("F", 25.7), ("F", 20), ("X", 20), ("X", 25.7), ("X", 22.5)]
    rules = [{"F": "FF-[-F+F+F]+[+F-F-F]"},
                     {"F": "F[+F]F[-F]F"},
                     {"F": "F[+F]F[-F][F]"},
                     {"X": "F[+X]F[-X]+X", "F": "FF"},
                     {"X": "F[+X][-X]FX", "F": "FF"},
                     {"X": "F-[[X]+X]+F[+FX]-X", "F": "FF"}]
    stack = []
    print("выбери вариант от 1 до 6:")
    variant = int(input()) - 1
    print("axiom: " + sets[variant][0] + " angle: " + str(sets[variant][1]))
    print(rules[variant])
    print("Вбей количество итераций:")
    iterations = int(input())
    genome = rw.processing(sets[variant][0], rules[variant], iterations)
    print("Геном растения: " + genome)
    tree.draw(genome, sets[variant][1], 10, 1, stack)
    return 0


if __name__ == '__main__':
    main()
