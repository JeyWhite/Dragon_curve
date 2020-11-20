

def rewrite(source: str, rules: dict) -> str:
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
    :param axiom: аксиома L-системы. С этих нескольких символов все и начнется!(строка)
    :param rules: словарь с правилами. ключ- заменяемый символ; значение- подставляемая строка.
    :param iterations: Количество итераций. То, сколько раз пробежим по строке с заменой.(инт)
    :return: инструкция к действию, которую будем посимвольно интерпретировать. (строка)
    """
    for i in range(iterations):
        axiom = rewrite(axiom, rules)
    return axiom
