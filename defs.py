import turtle


def replace(source: str, rules: dict) -> str:
    """
    Используется для L-систем!
    Функция проходит по строке посимвольно.
    Если символ является ключом в словаре он заменяется на значение по ключу.
    :param source: изначальная строка
    :param rules: словарь с правилами. ключ- заменяемый символ; значение- подставляемая строка.
    :return: строка, прошедшая одну итерацию l-системы
    """
    result = ""
    for symbol in source:
        if rules.get(symbol) is not None:
            result = result + rules.get(symbol)
        else:
            result = result + symbol
    return result


def processing(axiom: str, rules: dict, iterations: int):
    """
    Цикл с заменой символов в аксиоме.
    :param axiom: аксиома L-системы. с этих нескольких символов все и начнется!(строка)
    :param rules: словарь с правилами. ключ- заменяемый символ; значение- подставляемая строка.
    :param iterations: Количество итераций. То, сколько раз пробежим по строке с заменой.(инт)
    :return: инструкция к действию, которую будем посимвольно интерпретировать. (строка)
    """
    for i in range(iterations):
        axiom = replace(axiom, rules)
    return axiom


def draw(source: str, angle: int = 90, size: int = 10):
    """
    Отрисовка. интерпретируем каждый символ в какое-то действие черепахи.
    :param source: инструкция к действию, которую будем посимвольно интерпретировать. (строка)
    :param angle: угол поворота черепахи.
    :param size: Размер шага черепахи
    :return: ничего. черепаха сама себе вызывает канвас и все рисует.
    """
    for symbol in source:
        if symbol == "F":
            turtle.forward(size)
        elif symbol == "+":
            turtle.left(angle)
        elif symbol == "-":
            turtle.right(angle)
    return None
