# Документация проекта Geometric Lib

## Описание
Geometric Lib - библиотека на языке Python, предназначенная для выполнения геометрических вычислений.
Библиотека позволяет вычислять площадь и периметр геометрических фигур. 
В проекте реализованы функции для работы с кругом, квадратом, прямоугольником 
и треугольником.

## Math formulas
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: ah/2

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: a + b + c

## Примеры вызова
circle area(4)
circle perimeter(4)
rectangle area(4, 9)
rectangle perimeter(4, 9)
square area(8)
square perimeter(8)
triangle area(5, 2)
triangle perimeter(3, 3, 5)

## Изменения коммитами
2c51a71 - Добавлен файл 'rectangle.py'

b90def6 - Добавлен файл 'triangle.py' и исправлено вычисление периметра в 'rectangle.py'

```python
import math


def area(r):
    '''Вычисляет площадь круга по заданному радиусу
       Параметр:
         r (float): длина радиуса
       Возвращаемое значение:
         float: площадь круга
       Пример вызова:
         circle area(4)
    '''
    return math.pi * r * r


def perimeter(r):
    '''Вычисляет длину окружности по заданному радиусу
       Параметр:
         r (float): длина радиуса
       Возвращаемое значение:
         float: длина окружности
       Пример вызова:
         circle perimeter(4)
    '''
    return 2 * math.pi * r
```
