import math

def area(r):
    '''
    функция для высчитывания площади круга

    если r (радиус) это число, то возводит в квадрат и умножает на число пи
    иначе выводит ничего (None)

    Example:
    int r = 5

    return: 25pi
    '''
    return math.pi * r * r

def perimeter(r):
    '''
    функция для высчитывания периметра круга

    если r (радиус) это число, то умножает его на число пи и на 2
    иначе выводит ничего (None)

    Example:
    int r = 5

    return: 10pi
    '''
    return 2 * math.pi * r

