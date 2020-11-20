import turtle
import math


def curved_draw(source: str, angle: int = 90, step_size: int = 10):
    """
    Отрисовка. интерпретируем каждый символ в какое-то действие черепахи.
    :param source: инструкция к действию, которую будем посимвольно интерпретировать. (строка)
    :param angle: угол поворота черепахи.
    :param step_size: Размер шага черепахи
    :return: ничего. черепаха сама себе вызывает канвас и все рисует.
    """
    for symbol in source:
        if symbol == "+":
            chamfer("right", int(step_size), 4)
            # turtle.left(angle)
        elif symbol == "-":
            chamfer("left", int(step_size), 4)
            # turtle.right(angle)
    return None


def square_draw(source: str, angle: int = 90, step_size: int = 10):
    """
    Отрисовка. интерпретируем каждый символ в какое-то действие черепахи.
    :param source: инструкция к действию, которую будем посимвольно интерпретировать. (строка)
    :param angle: угол поворота черепахи.
    :param step_size: Размер шага черепахи
    :return: ничего. черепаха сама себе вызывает канвас и все рисует.
    """
    for symbol in source:
        if symbol == "F":
            turtle.forward(step_size)
        elif symbol == "+":
            turtle.left(angle)
        elif symbol == "-":
            turtle.right(angle)
    return None


def chamfer(direction: str, size: int, segments: int, angle: int = 90):
    """
    I gonna write some here when it will works
    well, its work. i will write comment later.
    :param direction:
    :param size:
    :param segments:
    :param angle:
    :return:
    """
    step_size = (size * 2 * math.pi) / segments
    if direction == "right":
        for seg in range(segments):
            turtle.right(angle / segments)
            turtle.fd(step_size)
    elif direction == "left":
        for seg in range(segments):
            turtle.left(angle / segments)
            turtle.fd(step_size)
    return None
