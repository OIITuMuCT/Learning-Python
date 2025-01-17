# Эта программа рисует узор, используя повторяющиеся линии.
import turtle

# Именованные константы
START_X = -200  # Стартовая координата Х.
START_Y = 0  # Стартовая координата Y.
NUM_LINES = 36  # Кол-во рисуемых линий.
LINE_LENGTH = 400  # Длина каждой линии.
ANGLE = 170  # Угол поворота.
ANIMATION_SPEED = 25  # Скорость анимации.

# Переместить черепаху в начальную позицию.
turtle.hideturtle()
turtle.penup()
turtle.goto(START_X, START_Y)
turtle.pendown()

# Задать скорость анимации.
turtle.speed(ANIMATION_SPEED)

# Нарисовать 36 кругов, наклоняя черепаху на
# 170 градусов после того, как каждая линяя была нарисована.
for x in range(NUM_LINES):
    turtle.forward(LINE_LENGTH)
    turtle.left(ANGLE)

turtle.done()
