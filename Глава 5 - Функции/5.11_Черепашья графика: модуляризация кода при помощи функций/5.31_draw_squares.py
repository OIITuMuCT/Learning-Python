import turtle

def main():
    turtle.hideturtle()
    square(100, 0, 50, 'red')
    square(-150, -100, 200, 'blue')
    square(-200, 150, 75, 'green')

# Функция square рисует квадрат.
# Параметры х и у - это координаты левого нижнего угла.
# Параметр width - это ширина стороны квадрата.
# Параметр color - это цвет заливки в виде строки.

def square(x, у, width, color):
    turtle.penup()          # Поднять перо.
    turtle.goto(x, у)       # Переместить в указанное место.
    turtle.fillcolor(color) # Задать цвет заливки.
    turtle.pendown()        # Опустить перо.
    turtle.begin_fill()     # Начать заливку.
    for count in range(4):  # Нарисовать квадрат.
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()       # Завершить заливку.
 
# Вызвать главную функцию.
main()