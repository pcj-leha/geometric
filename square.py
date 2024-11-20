
def area(a):
    '''
    Возвращает площадь квадрата со сторонами a

        Параметры:
            a (float): длина стороны квадрата

        Возвращаемое значение:
            (float): значение площади квадрата
    '''
    if a <= 0:
        raise ValueError("Side must be a positive number")
    return a * a


def perimeter(a):
    '''
    Возвращает периметр квадрата со сторонами a

        Параметры:
            a (float): длина стороны квадрата

        Возвращаемое значение:
            (float): значение периметра квадрата
    '''
    if a <= 0:
        raise ValueError("Side must be a positive number")
    return 4 * a

