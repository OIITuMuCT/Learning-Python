# Функции черепашьей графики.
import turtle

# Функция square рисует -квадрат.
# Параметры х и у - это координаты левого нижнего угла.
# Параметр width - это ширина стороны квадрата.
# Параметр color - это цвет заливки в виде строки.

def square(x,у,width, color):
    turtle.penup()          # Поднять перо.
    turtle.goto(x, у)       # Переместить в указанное место.
    turtle.fillcolor(color) # Задать цвет заливки.
    turtle.pendown()        # Опустить перо.
    turtle.begin_fill()     # Начать заливку.
    for count in range(4):  # Нарисовать квадрат.
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()       #Завершить заливку.

# Функция circle рисует круг.
# Параметры х и у - это координаты центральной точки.
# Параметр radius - это радиус круга.
# Параметр color - это цвет заливки в виде строки.

def circle(x, у, radius, color):
    turtle.penup()                   # Поднять перо.
    turtle.goto(x, у - radius)       # Спозиционировать черепаху.
    turtle.fillcolor(color)          # Задать цвет заливки.
    turtle.pendown()                 # Опустить перо.
    turtle.begin_fill()              # Начать заливку.
    turtle.circle(radius)            # Нарисовать круг.
    turtle.end_fill()                # Завершить заливку.
    
# Функция line рисует линию от (startX, startY) до (endX, endY).
# Параметр color - это цвет линии.

def line(startX, startY, endX, endY, color):
    turtle.penup()                # Поднять перо.
    turtle.goto(startX, startY)     # Переместить в начальную точку.
    turtle.pendown()                # Опустить перо.
    turtle.pencolor(color)          # Задать цвет заливки.
    turtle.goto(endX, endY)         # Нарисовать треугольник.