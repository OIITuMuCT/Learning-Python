# Эта программа наносит  звезды созвездия Ориона,
# названия звезд и линии созвездия.
import turtle

# Задать размер окна шириной 500 и высотой 600 пикселов.
turtle.setup(500, 600)

# Установить черепаху.
turtle.penup()
turtle.hideturtle()

# Создать именованные константы для звёздных координат.
LEFT_SHOULDER_X = -70  # Левое плечо координаты.
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80  # Правое плечо координаты.
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40  # Левая звезда в поясе координаты.
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0  # Средняя звезда в поясе координаты.
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELSTAR_X = 40  # Крайняя правая звезда в поясе координаты.
RIGHT_BELSTAR_Y = 20

LEFT_KNEE_X = -90  # Левое колено координаты.
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120  # Правое колено координаты.
RIGHT_KNEE_Y = -140

# Нанести звёзды.
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)  # Левое плечо.
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)  # Правое плечо.
turtle.dot()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)  # Левая звезда в поясе.
turtle.dot()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)  # Средняя звезда в поясе
turtle.dot()
turtle.goto(RIGHT_BELSTAR_X, RIGHT_BELSTAR_Y)  # Правая звезда в поясе
turtle.dot()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)  # Левое колено
turtle.dot()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)  # Правое колено
turtle.dot()

# Вывести названия звёзд.
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)  # Левое плечо.
turtle.write('Бетельгейзе')
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)  # Правое плечо.
turtle.write('Хатиса')
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)  # Левая звезда в поясе.
turtle.write('Альнитак')
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)  # Средняя звезда в поясе.
turtle.write('Альнилам')
turtle.goto(RIGHT_BELSTAR_X, RIGHT_BELSTAR_Y)  # Правая звезда в поясе.
turtle.write('Минтака')
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)  # Левое колено.
turtle.write('Саиф')
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)  # Правое колено
turtle.write('Ригель')

# Нанести линию из левого плеча в левую звезду пояса.
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.penup()

# Нанести линию из правого плеча в правую звезду пояса.
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELSTAR_X, RIGHT_BELSTAR_Y)
turtle.penup()

# Нанести линию из левой звезды в среднюю звезду пояса.
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.penup()

# Нанести линию из средней звезды пояса в правую звезду пояса.
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELSTAR_X, RIGHT_BELSTAR_Y)
turtle.penup()

# Нанести линию из левой звезды пояса в левое колено.
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.penup()

# Нанести линию из правой звезды пояса в правое колено.
turtle.goto(RIGHT_BELSTAR_X, RIGHT_BELSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)

# Оставить окно открытым.  (В среде IDLE не требуется.)
turtle.done()
