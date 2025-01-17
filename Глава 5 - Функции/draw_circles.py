import turtle

def main():
    turtle.hideturtle()
    circle(0, 0, 100, 'red')
    circle(-150, -75, 50, 'blue')
    circle(-200, 150, 75, 'green')

# Функция circle рисует круг.
# Параметры х и у - это координаты центральной точки.
# Параметр radius - это радиус круга.
# Параметр color - это цвет заливки в виде строки.

def circle(x, у, radius, color):
    turtle.penup()              # Поднять перо.
    turtle.goto(x, у - radius)  # Спозиционировать черепаху.
    turtle.fillcolor(color)     # Задать цвет заливки.
    turtle.pendown()            # Опустить перо.
    turtle.begin_fill()         # Начать заливку.
    turtle.circle(radius)       # Нарисовать круг.
    turtle.end_fill()           # Завершить заливку.

# Вызвать главную функцию.
main()