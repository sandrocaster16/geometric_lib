def area(a, b):
    '''
    функция для высчитывания площади прямоугольника

    если a и b это числа, то принимает a,b(стороны) и перемножает их
    иначе выводит ничего (None)

    Example:
    int a = 5
    int b = 3

    return: 15
    '''

    if (type(a) != str and type(b) != str) and (a > 0 and b > 0):
        return a * b
    else:
        return None


def perimeter(a, b):
    '''
    функция для высчитывания периметра прямоугольника

    если a и b это числа, то принимает a,b(стороны) и умножает их сумму на 2
    иначе выводит ничего (None)

    Example:
    int a = 5
    int b = 3

    return: 16
    '''

    if (type(a) != str and type(b) != str) and (a > 0 and b > 0):
        return (a + b)*2
    else:
        return None


#Unit tests
import unittest

class RectangleTestCase(unittest.TestCase):
    # площадь:

    # проверка на 0
    def test_area_zero(self):
        res = area(10, 0)
        self.assertEqual(res, None)
    
    # проверка с положительными значениями   
    def test_area_plus(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    # проверка с отрицательными значениями
    def test_area_minus(self):
        res = area(-4,-5)
        self.assertEqual(res, None)

    # проверка с большими значениями
    def test_area_longlongint(self):
        res = area(10000000,10000000)
        self.assertEqual(res, 100000000000000)

    # проверка со строками
    def test_area_char(self):
        res = area("q",10)
        self.assertEqual(res, None)

    # проверка на дробные числа
    def test_area_double(self):
        res = area(2.5,1.5)
        self.assertEqual(res, 3.75)


    #периметр:

    # проверка на 0
    def test_perimeter_zero(self):
        res = perimeter(10, 0)
        self.assertEqual(res, None)
    
    # проверка с положительными значениями   
    def test_perimeter_plus(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    # проверка с отрицательными значениями
    def test_perimeter_minus(self):
        res = perimeter(-4,-5)
        self.assertEqual(res, None)

    # проверка с большими значениями
    def test_perimeter_longlongint(self):
        res = perimeter(10000000,10000000)
        self.assertEqual(res, 40000000)

    # проверка со строками
    def test_perimeter_char(self):
        res = perimeter("q",10)
        self.assertEqual(res, None)

    # проверка на дробные числа
    def test_perimeter_double(self):
        res = perimeter(2.5,1.5)
        self.assertEqual(res, 8)

