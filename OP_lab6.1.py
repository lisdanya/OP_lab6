import math


class Figure:

    def __init__(self, r, h, s_r):
        self.radius = r
        self.height = h
        self.s_radius = s_r

    def getRadius(self):
        return self.radius

    def getHeight(self):
        return self.height

    def getSRadius(self):
        return self.s_radius

    def findAreaCircle(self, r):
        self.areaCircle = math.pi * r * r
        return self.areaCircle

    def findAreaSideCone(self, r, h):
        self.areaSideCone = math.pi * r * math.sqrt(r * r + h * h)
        return self.areaSideCone

    def findAreaSideCylinder(self, r, h):
        self.areaSideCylinder = 2 * math.pi * r * h
        return self.areaSideCylinder

    def findAreaEllipse(self, s_radius, r):
        self.areaEllipse = math.pi * s_radius * r
        return self.areaEllipse

    def findAreaSideEllipticalCylinder(self, r, s_radius, h):
        self.areaSideEllipticalCylinder = h * 2 * math.pi * math.sqrt(
            (r * r + s_radius * s_radius) / 2)
        return self.areaSideEllipticalCylinder


class Cone(Figure):

    def findAreaCone(self, areaCircle, areaSideCone):
        self.areaCone = areaCircle + areaSideCone
        print(self.areaCone)

    def findVolumeCone(self, r, h):
        self.volumeCone = 1 / 3 * math.pi * r * r * h
        print(self.volumeCone)


class Cylinder(Figure):

    def findAreaCylinder(self, areaCircle, areaSideCylinder):
        self.areaCylinder = 2 * areaCircle + areaSideCylinder
        print(self.areaCylinder)

    def findVolumeCylinder(self, areaCircle, h):
        self.volumeCylinder = areaCircle * h
        print(self.volumeCylinder)


class EllipticalCylinder(Figure):

    def findAreaEllipticalCylinder(self, areaEllips, areaSideEllipticalCylinder):
        self.areaEllipticalCylinder = 2 * areaEllips + areaSideEllipticalCylinder
        print(self.areaEllipticalCylinder)

    def findVolumeEllipticalCylinder(self, areaEllips, h):
        self.volumeEllipticalCylinder = areaEllips * h
        print(self.volumeEllipticalCylinder)


s_r = 0
coun=int(input("Для выбора КОНУСА введите 1 \n"
               "Для выбора ЦИЛИНДРА введите 2 \n"
               "Для выбора ЭЛЛИПТИЧЕСКОГО ЦИЛИНДРА введите 3 \n"))


if coun==1:
    r = int(input("Радиус: "))
    h = int(input("Высота: "))
    f1 = Cone(r, h, s_r)
    print("Площадь конуса")
    f1.findAreaCone(f1.findAreaCircle(f1.getRadius()),
                    f1.findAreaSideCone(f1.getRadius(), f1.getHeight()))
    print("Объем конуса ")
    f1.findVolumeCone(f1.getRadius(), f1.getHeight())
elif coun==2:
    r = int(input("Радиус: "))
    h = int(input("Высота: "))
    f2 = Cylinder(r, h, s_r)
    print("Площадь цилиндра ")
    f2.findAreaCylinder(f2.findAreaCircle(f2.getRadius()),
                        f2.findAreaSideCylinder(f2.getRadius(), f2.getHeight()))
    print("Объем цилиндра ")
    f2.findVolumeCylinder(f2.findAreaCircle(f2.getRadius()), f2.getHeight())
elif coun==3:
    r = int(input("Большая полуось: "))
    s_r = int(input("Меньшая полуось: "))
    h = int(input("Высота: "))
    f3 = EllipticalCylinder(r, h, s_r)
    print("Площадь эллиптического цилиндра ")
    f3.findAreaEllipticalCylinder(f3.findAreaEllipse(f3.getRadius(), f3.getSRadius()),
                                  f3.findAreaSideEllipticalCylinder(f3.getRadius(), f3.getSRadius(),
                                                                    f3.getHeight()))
    print("Объем эллиптического цилиндра")
    f3.findVolumeEllipticalCylinder(f3.findAreaEllipse(f3.getRadius(), f3.getSRadius()),
                                    f3.getHeight())
else: print("ERROR")




