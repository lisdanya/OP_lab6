# для решения математических формул
import math
# для наглядности реализации абстрактного класса и метода
from abc import ABC, abstractmethod


# базовый абстрактный класс
class Figure(ABC):

    # Элементы-данные фигур
    def __init__(self, r, h, s_r):
        self.r = r
        self.h = h
        self.s_r = s_r

    # Виртуальный метод
    @abstractmethod
    def findAreaCone(self):
        pass

    # Виртуальный метод
    @abstractmethod
    def findVolumeCone(self):
        pass

    # Виртуальный метод
    @abstractmethod
    def findVolumeEllipticalCylinder(self):
        pass

    # Виртуальный метод
    @abstractmethod
    def findAreaEllipticalCylinder(self):
        pass

    # Виртуальный метод
    @abstractmethod
    def findAreaCylinder(self):
        pass

    # Виртуальный метод
    @abstractmethod
    def findVolumeCylinder(self):
        pass


# Наследник базового класса
class Cone(Figure):

    def findVolumeEllipticalCylinder(self):
        pass

    def findAreaEllipticalCylinder(self):
        pass

    def findAreaCylinder(self):
        pass

    def findVolumeCylinder(self):
        pass

    # формула вычесления площади
    def findAreaCone(self):
        self.areaCone = (math.pi * r * r) + (math.pi * r * math.sqrt(r * r + h * h))
        print(self.areaCone)

    # формула вычесления обьема
    def findVolumeCone(self):
        self.volumeCone = 1 / 3 * math.pi * r * r * h
        print(self.volumeCone)


# Наследник базового класса
class Cylinder(Figure):

    def findAreaCone(self):
        pass

    def findVolumeCone(self):
        pass

    def findVolumeEllipticalCylinder(self):
        pass

    def findAreaEllipticalCylinder(self):
        pass

    # формула вычесления площади
    def findAreaCylinder(self):
        self.areaCylinder = 2 * (math.pi * r * r) + 2 * math.pi * r * h
        print(self.areaCylinder)

    # формула вычесления обьема
    def findVolumeCylinder(self):
        self.volumeCylinder = (math.pi * r * r) * h
        print(self.volumeCylinder)


# Наследник базового класса
class EllipticalCylinder(Figure):

    def findAreaCone(self):
        pass

    def findVolumeCone(self):
        pass

    def findAreaCylinder(self):
        pass

    def findVolumeCylinder(self):
        pass

    # формула вычесления площади
    def findAreaEllipticalCylinder(self):
        self.areaEllipticalCylinder = (2 * math.pi * s_r * r) + (h * 2 * math.pi * math.sqrt(
            (r * r + s_r * s_r) / 2))
        print(self.areaEllipticalCylinder)

    # формула вычесления обьема
    def findVolumeEllipticalCylinder(self):
        self.volumeEllipticalCylinder = (2 * math.pi * s_r * r) * h
        print(self.volumeEllipticalCylinder)

# для фигир у которых нет меньшей полуоси
s_r = 0
# выбор фигуры
coun = int(input("Для выбора КОНУСА введите 1 \n"
                 "Для выбора ЦИЛИНДРА введите 2 \n"
                 "Для выбора ЭЛЛИПТИЧЕСКОГО ЦИЛИНДРА введите 3 \n"))

if coun == 1:
    r = int(input("Радиус: "))
    h = int(input("Высота: "))
    # экземпляр класса конус
    f1 = Cone(r, h, s_r)
    print("Площадь конуса")
    f1.findAreaCone()
    print("Объем конуса ")
    f1.findVolumeCone()
elif coun == 2:
    r = int(input("Радиус: "))
    h = int(input("Высота: "))
    # экземпляр класса цилиндер
    f2 = Cylinder(r, h, s_r)
    print("Площадь цилиндра ")
    f2.findAreaCylinder()
    print("Объем цилиндра ")
    f2.findVolumeCylinder()
elif coun == 3:
    r = int(input("Большая полуось: "))
    s_r = int(input("Меньшая полуось: "))
    h = int(input("Высота: "))
    # экземпляр класса элиптический цилиндр
    f3 = EllipticalCylinder(r, h, s_r)
    print("Площадь эллиптического цилиндра ")
    f3.findAreaEllipticalCylinder()
    print("Объем эллиптического цилиндра")
    f3.findVolumeEllipticalCylinder()
else:
    print("ERROR")
