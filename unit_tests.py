#Unit tests
import unittest
import math

import circle
import rectangle
import square
import triangle

class CircleTestCase(unittest.TestCase):
    # площадь:

    # проверка на 0
    def test_area_zero(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    # проверка с положительными значениями   
    def test_area_plus(self):
        res = circle.area(10)
        self.assertEqual(res, 100*math.pi)

    # проверка с отрицательными значениями
    def test_area_minus(self):
        res = circle.area(-4)
        self.assertEqual(res, None)

    # проверка с большими значениями
    def test_area_longlongint(self):
        res = circle.area(10000000)
        self.assertEqual(res, 100000000000000*math.pi)

    # проверка со строками
    def test_area_char(self):
        res = circle.area("q")
        self.assertEqual(res, None)

    # проверка на дробные числа
    def test_area_double(self):
        res = circle.area(2.5)
        self.assertEqual(res, 6.25*math.pi)


    #периметр:

    # проверка на 0
    def test_perimeter_zero(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    # проверка с положительными значениями   
    def test_perimeter_plus(self):
        res = circle.perimeter(10)
        self.assertEqual(res, 20*math.pi)

    # проверка с отрицательными значениями
    def test_perimeter_minus(self):
        res = circle.perimeter(-4)
        self.assertEqual(res, None)

    # проверка с большими значениями
    def test_perimeter_longlongint(self):
        res = circle.perimeter(10000000,)
        self.assertEqual(res, 20000000*math.pi)

    # проверка со строками
    def test_perimeter_char(self):
        res = circle.perimeter("q")
        self.assertEqual(res, None)

    # проверка на дробные числа
    def test_perimeter_double(self):
        res = circle.perimeter(2.5)
        self.assertEqual(res, 5*math.pi)

class RectangleTestCase(unittest.TestCase):
    # площадь:

    # проверка на 0
    def test_area_zero(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)
    
    # проверка с положительными значениями   
    def test_area_plus(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    # проверка с отрицательными значениями
    def test_area_minus(self):
        res = rectangle.area(-4,-5)
        self.assertEqual(res, None)

    # проверка с большими значениями
    def test_area_longlongint(self):
        res = rectangle.area(10000000,10000000)
        self.assertEqual(res, 100000000000000)

    # проверка со строками
    def test_area_char(self):
        res = rectangle.area("q",10)
        self.assertEqual(res, None)

    # проверка на дробные числа
    def test_area_double(self):
        res = rectangle.area(2.5,1.5)
        self.assertEqual(res, 3.75)


    #периметр:

    # проверка на 0
    def test_perimeter_zero(self):
        res = rectangle.perimeter(10, 0)
        self.assertEqual(res, 0)
    
    # проверка с положительными значениями   
    def test_perimeter_plus(self):
        res = rectangle.perimeter(10, 10)
        self.assertEqual(res, 40)

    # проверка с отрицательными значениями
    def test_perimeter_minus(self):
        res = rectangle.perimeter(-4,-5)
        self.assertEqual(res, None)

    # проверка с большими значениями
    def test_perimeter_longlongint(self):
        res = rectangle.perimeter(10000000,10000000)
        self.assertEqual(res, 40000000)

    # проверка со строками
    def test_perimeter_char(self):
        res = rectangle.perimeter("q",10)
        self.assertEqual(res, None)

    # проверка на дробные числа
    def test_perimeter_double(self):
        res = rectangle.perimeter(2.5,1.5)
        self.assertEqual(res, 8)

class SquareTestCase(unittest.TestCase):
    # площадь:

    # проверка на 0
    def test_area_zero(self):
        res = square.area(0)
        self.assertEqual(res, 0)
    
    # проверка с положительными значениями   
    def test_area_plus(self):
        res = square.area(10)
        self.assertEqual(res, 100)

    # проверка с отрицательными значениями
    def test_area_minus(self):
        res = square.area(-4)
        self.assertEqual(res, None)

    # проверка с большими значениями
    def test_area_longlongint(self):
        res = square.area(10000000)
        self.assertEqual(res, 100000000000000)

    # проверка со строками
    def test_area_char(self):
        res = square.area("q")
        self.assertEqual(res, None)

    # проверка на дробные числа
    def test_area_double(self):
        res = square.area(2.5)
        self.assertEqual(res, 6.25)


    #периметр:

    # проверка на 0
    def test_perimeter_zero(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)
    
    # проверка с положительными значениями   
    def test_perimeter_plus(self):
        res = square.perimeter(10)
        self.assertEqual(res, 40)

    # проверка с отрицательными значениями
    def test_perimeter_minus(self):
        res = square.perimeter(-4)
        self.assertEqual(res, None)

    # проверка с большими значениями
    def test_perimeter_longlongint(self):
        res = square.perimeter(10000000)
        self.assertEqual(res, 40000000)

    # проверка со строками
    def test_perimeter_char(self):
        res = square.perimeter("q")
        self.assertEqual(res, None)

    # проверка на дробные числа
    def test_perimeter_double(self):
        res = square.perimeter(2.5)
        self.assertEqual(res, 10)

class TriangleTestCase(unittest.TestCase):
    # площадь:

    # проверка на 0
    def test_area_zero(self):
        res = triangle.area(0, 0)
        self.assertEqual(res, 0)
    
    # проверка с положительными значениями   
    def test_area_plus(self):
        res = triangle.area(10, 5)
        self.assertEqual(res, 7.5)

    # проверка с отрицательными значениями
    def test_area_minus(self):
        res = triangle.area(-4,-5)
        self.assertEqual(res, None)

    # проверка с большими значениями
    def test_area_longlongint(self):
        res = triangle.area(10000000,4)
        self.assertEqual(res, 100000000000000)

    # проверка со строками
    def test_area_char(self):
        res = triangle.area("q",10)
        self.assertEqual(res, None)

    # проверка на дробные числа
    def test_area_double(self):
        res = triangle.area(2.5,2)
        self.assertEqual(res, 2.5)


    #периметр:

    # проверка на 0
    def test_perimeter_zero(self):
        res = triangle.perimeter(0,0,0)
        self.assertEqual(res, None)
    
    # проверка с положительными значениями   
    def test_perimeter_plus(self):
        res = triangle.perimeter(10, 15, 20)
        self.assertEqual(res, 40)

    # проверка с отрицательными значениями
    def test_perimeter_minus(self):
        res = triangle.perimeter(-4,-5,-6)
        self.assertEqual(res, None)

    # проверка с большими значениями
    def test_perimeter_longlongint(self):
        res = triangle.perimeter(10000000,20000000,30000000)
        self.assertEqual(res, 60000000)

    # проверка со строками
    def test_perimeter_char(self):
        res = triangle.perimeter("q",10,2)
        self.assertEqual(res, None)

    # проверка на дробные числа
    def test_perimeter_double(self):
        res = triangle.perimeter(2.5,1.5,3.8)
        self.assertEqual(res, 7.8)