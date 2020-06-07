from collections import defaultdict


# класс отвечающий за манипуляции с продуктами
class Food():

    def __init__(self):
        self.products = defaultdict()

    @property
    def get_products(self):
        return self.products

    # Приготовление блюда , при этом уменьшается количество продуктов на складе ,
    # в случае отсутствия продуктов выводит невозможность приготовить блюдо
    def dish(self, product1, product2):
        # если есть продукты
        if self.get_products[product1][0] >= 1 and self.products[product2][0] >= 1:
            self.get_products[product1][0] -= 1
            self.get_products[product2][0] -= 1
            return True  # блюдо приготовится
        else:
            print("Закончились продукты")
            return False  # блюдо не приготовится

    # Задаёт изначальное количество продуктов на складе
    def warehouse(self, product, count):
        self.get_products[product] = [count]

    # Заказ определенного количества выбраного продукта
    def purchase(self, product, count):
        self.get_products[product][0] += count
        # print(self.get_products)


# класс отвечающий за действия на кухне
class Kitchen(Food):

    def __init__(self):
        super().__init__()
        self.recipe = defaultdict()

    # Добавление в меню блюд ,продуктов из которых они сделаны и их стоимости
    def menu(self, dish, product1, product2, price):
        # если достаточно продуктов, блюдо будет добавлено в меню
        if self.products[product1][0] >= 1 and self.products[product2][0] >= 1:
            self.recipe[dish] = [product1, product2, price, 0]
            # self.recipe[dish][1] = product2
            # self.recipe[dish][2] = price
            # print(self.recipe)
        else:
            print("Закажите еще продуктов")


# класс отвечающий за действия в ресторане
class Restaurant(Kitchen):

    def __init__(self):
        super().__init__()
        self.proceed = 0  # в начале дня выручка нулевая
        self.proceed_dish = []  # выручка определенного блюда
        self.reserve = defaultdict()  # зарезервированыеместа
        self.counter = 0

    # Функция зарезервирования столика определенным человеком
    def reserved(self, customer):
        self.counter += 1
        self.reserve[customer] = [self.counter]
        # print(self.reserve)

    # функция заказа блюда
    def order(self, dish):
        try:
            if self.dish(self.recipe[dish][0], self.recipe[dish][1]):  # есди есть продукты
                self.recipe[dish][3] += 1
                # print(self.recipe)
        except Exception:  # если введено название блюда , которого нет в меню
            print("Такого блюда нет в нашем меню")

    # Подсчет прибыли
    def proceeds(self):
        for dish in self.recipe:
            proceed_dishs = self.recipe[dish][2] * self.recipe[dish][3]  # прибыль каждого блюда
            self.proceed_dish.append(["Блюдо: " + str(dish) + ",",
                                      "Количество заказов: " + str(self.recipe[dish][3]) + ",",
                                      "Прибыль " + str(proceed_dishs)])
            self.proceed += proceed_dishs  # общая прибыль всех блюд меню
        for dish in self.proceed_dish:
            print(*dish)
        # print(self.proceed_dish)
        print("Выручка за день:", self.proceed)


# экземпляр класса Ресторан
restik = Restaurant()
# Сколько продуктов уже было на складе
restik.warehouse("Гречка", 10)
restik.warehouse("Мясо", 10)
restik.warehouse("Картофель", 5)
restik.warehouse("Масло", 5)
# Скоько продуктов еще нужно заказать
restik.purchase("Гречка", 10)
restik.purchase("Мясо", 10)
restik.purchase("Картофель", 10)
restik.purchase("Масло", 10)
# добавление в меню блюд исходя из имеющихся продуктов
restik.menu("Гарнир", "Гречка", "Мясо", 1000)
restik.menu("Пюре", "Картофель", "Масло", 500)
# заказ блюд
restik.order("Пюре")
restik.order("Пюре")
restik.order("Пюре")
restik.order("Пюре")
restik.order("Пюре")
restik.order("Пюре")
restik.order("Гарнир")
restik.order("Гарнир")
restik.order("Гарнир")
restik.order("Гарнир")
restik.order("Гарнир")
restik.order("Гарнир")
restik.purchase("Мясо", 1)
# резервирование мест
restik.reserved("Вася")
restik.reserved("Петя")
restik.reserved("Ваня")
# вывод выручки
restik.proceeds()
