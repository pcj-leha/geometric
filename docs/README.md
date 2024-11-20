# Geometric lib

Решение позволяет искать площадь и периметр у таких геометрических фигур, как круг, прямоугольник, квадрад, треугольник.

# Математические формулы
## Площадь
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah / 2

## Периметр
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Функции

## Circle
### circle.area(r)

Возвращает площадь круга радиусом r

    Параметры:
        r (float): радиус круга
        
    Возвращаемое значение:
        (float): значение площади круга

```python
from geometric_lib import circle

circle.area(2) -> 12.566370614359172
```


### circle.perimeter(r)

Возвращает периметр круга радиусом r

    Параметры:
        r (int): радиус круга
    
    Возвращаемое значение:
        (float): значение периметра круга

```python
from geometric_lib import circle

circle.perimeter(2) -> 12.566370614359172
```

## Rectangle
### rectangle.area(a, b)

Возвращает площадь прямоугольника со сторонами a, b

    Параметры:
        a (float): длина прямоугольника
        b (float): ширина прямоугольника

    Возвращаемое значение:
        (float): значение площади прямоугольника

```python
from geometric_lib import rectangle

rectangle.area(2, 3) -> 6
```

### rectangle.perimeter(a, b)

Возвращает периметр прямоугольника со сторонами a, b

    Параметры:
        a (float): длина прямоугольника
        b (float): ширина прямоугольника

    Возвращаемое значение:
        (float): значение периметра прямоугольника

```python
from geometric_lib import rectangle

rectangle.perimeter(2, 3) -> 10
```

## Square
### square.area(a)

Возвращает площадь квадрата со сторонами a

    Параметры:
        a (float): длина стороны квадрата

    Возвращаемое значение:
        (float): значение площади квадрата

```python
from geometric_lib import square

square.area(2) -> 4
```

### square.perimeter(a)

Возвращает периметр квадрата со сторонами a

    Параметры:
        a (float): длина стороны квадрата

    Возвращаемое значение:
        (float): значение периметра квадрата

```python
from geometric_lib import square

print(square.perimeter(2)) -> 8
```

## Triangle
### triangle.area(a, h)

Возвращает площадь треугольника с длиной основания a и высотой проведённой к основанию h

    Параметры:
        a (float): длина основания треугольника
        h (float): длина высоты треугольника проведённой к основанию

    Возвращаемое значение:
        (float): значение площади треугольника

```python
from geometric_lib import triangle

triangle.area(2, 3) -> 3
```

### triangle.perimeter(a, b, c)

Возвращает площадь треугольника с длинами сторой a, b,с

    Параметры:
        a (float): длина первой стороны треугольника
        b (float): длина второй стороны треугольника
        c (float): длина третьей стороны треугольника

    Возвращаемое значение:
        (float): значение периметра треугольника

```python
from geometric_lib import triangle

triangle.perimeter(2, 3, 4) -> 9
```
