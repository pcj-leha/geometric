import unittest
from triangle import area as triangle_area, perimeter as triangle_perimeter
from square import area as square_area, perimeter as square_perimeter


''' 
Класс TestTriangle содержит в себе функции для тестирования функций из файла triangal.py
'''
class TestTriangle(unittest.TestCase):
    '''
    тест для проверки функции triangle_area() при корректно введённых данных
    '''
    def test_area_positive(self):
        self.assertEqual(triangle_area(10, 5), 25, "Triangle area with base 10 and height 5 should be 25")
        self.assertEqual(triangle_area(5, 3), 7.5, "Triangle area with base 5 and height 3 should be 7.5")

    '''
    тест для проверки функции triangle_area() если хотя бы один параметр - ноль
    '''
    def test_area_zero(self):
        with self.assertRaises(ValueError, msg="Zero dimensions should raise a ValueError"):
            triangle_area(0, 5)
        with self.assertRaises(ValueError, msg="Zero dimensions should raise a ValueError"):
            triangle_area(5, 0)

    '''
    тест для проверки функции triangle_area() если хотя бы один параметр - отрицательное число
    '''
    def test_area_negative(self):
        with self.assertRaises(ValueError, msg="Negative dimensions should raise a ValueError"):
            triangle_area(-10, 5)
        with self.assertRaises(ValueError, msg="Negative dimensions should raise a ValueError"):
            triangle_area(10, -5)

    '''
    тест для проверки функции triangle_perimeter() при корректно введённых данных
    '''
    def test_perimeter_positive(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12,
                         "Perimeter of triangle with sides 3, 4, 5 should be 12")
        self.assertEqual(triangle_perimeter(3.25, 4.25, 5.25), 12.75,
                         "Perimeter of triangle with sides 3.25, 4.25, 5.25 should be 12.75")

    '''
    тест для проверки функции triangle_perimeter() если хотя бы один параметр - ноль
    '''
    def test_perimeter_zero(self):
        with self.assertRaises(ValueError, msg="Sides of zero length should raise a ValueError"):
            triangle_perimeter(0, 4, 5)
        with self.assertRaises(ValueError, msg="Sides of zero length should raise a ValueError"):
            triangle_perimeter(4, 0, 5)
        with self.assertRaises(ValueError, msg="Sides of zero length should raise a ValueError"):
            triangle_perimeter(4, 5, 0)

    '''
    тест для проверки функции triangle_perimeter() если хотя бы один параметр - отрицательное число
    '''
    def test_perimeter_negative(self):
        with self.assertRaises(ValueError, msg="Negative sides should raise a ValueError"):
            triangle_perimeter(-3, 4, 5)
        with self.assertRaises(ValueError, msg="Negative sides should raise a ValueError"):
            triangle_perimeter(3, -4, 5)
        with self.assertRaises(ValueError, msg="Negative sides should raise a ValueError"):
            triangle_perimeter(3, 4, -5)

''' 
Класс TestSquare содержит в себе функции для тестирования функций из файла square.py
'''
class TestSquare(unittest.TestCase):
    '''
    тест для проверки функции square_area() при корректно введённых данных
    '''
    def test_area_positive(self):
        self.assertEqual(square_area(4), 16, "Square area with side 4 should be 16")
        self.assertEqual(square_area(2.5), 6.25, "Square area with side 2.5 should be 6.25")

    '''
    тест для проверки функции square_area() если параметр - ноль
    '''
    def test_area_zero(self):
        with self.assertRaises(ValueError, msg="Zero dimensions should raise a ValueError"):
            square_area(0)

    '''
    тест для проверки функции square_area() если параметр - отрицательное число
    '''
    def test_area_negative(self):
        with self.assertRaises(ValueError, msg="Negative side should raise a ValueError"):
            square_area(-4)

    '''
    тест для проверки функции square_perimeter() при корректно введённых данных
    '''
    def test_perimeter_positive(self):
        self.assertEqual(square_perimeter(4), 16, "Square perimeter with side 4 should be 16")
        self.assertEqual(square_perimeter(2.15), 8.6, "Square perimeter with side 2.15 should be 8.16")

    '''
    тест для проверки функции square_perimeter() если параметр - ноль
    '''
    def test_perimeter_zero(self):
        with self.assertRaises(ValueError, msg="Zero dimensions should raise a ValueError"):
            square_perimeter(0)

    '''
        тест для проверки функции square_perimeter() если параметр - отрицательное число
        '''
    def test_perimeter_negative(self):
        with self.assertRaises(ValueError, msg="Negative side should raise a ValueError"):
            square_perimeter(-4)

if __name__ == "__main__":
    unittest.main()
