# Эта программа выводит простой линейный график. 
import matplotlib.pyplot as plt


def main():

    # Создать списки для координат Х и У каждой точки данных.
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]
 
    # Построить линейный график.
    plt.plot(x_coords, y_coords)

    # Добавить заголовок.
    plt.title('Образец данных')

    # Добавить на оси описательные метки.   
    plt.xlabel('Это ось х')
    plt.ylabel('Это ось у')
    
    # Задать границы осей.
    plt.xlim(xmin=-1, xmax=10)
    plt.ylim(ymin=-1, ymax=6)
    
    
    # Добавить ссетку.
    plt.grid(True)

    # Показать линейный график.
    plt.show()


# Вызвать главную функцию.
if __name__ == '__main__':
    main()