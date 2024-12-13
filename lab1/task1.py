import doctest


class Student:
    def __init__(self, name: str, age: int, grades: list):
        """
        Создание объекта "Студент"

        :param name: Имя студента
        :param age: Возраст студента
        :param grades: Список оценок студента

        Примеры:
        >>> student = Student("Иван", 20, [5, 4, 5, 3])
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        self.name = name

        if not isinstance(age, int) or age <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        self.age = age

        if not isinstance(grades, list) or not all(isinstance(grade, (int, float)) for grade in grades):
            raise TypeError("Оценки должны быть списком чисел")
        self.grades = grades


    def get_average_grade(self) -> float:
        """
        Получение средней оценки студента.

        :return: Средняя оценка

        Примеры:
        >>> student = Student("Иван", 20, [5, 4, 5, 3])
        >>> student.get_average_grade()
        """
        ...

    def is_passed(self) -> bool:
        """
        Проверка, сдал ли студент все экзамены (средняя оценка > 3).

        :return: True, если студент сдал все экзамены, иначе False

        Примеры:
        >>> student = Student("Иван", 20, [5, 4, 5, 3])
        >>> student.is_passed()
        """
        ...



class Car:
    def __init__(self, make: str, model: str, fuel_capacity: float, fuel_level: float = 0.0):
        """
        Создание объекта "Автомобиль"

        :param make: Марка автомобиля
        :param model: Модель автомобиля
        :param fuel_capacity: Ёмкость топливного бака
        :param fuel_level: Уровень топлива в баке (по умолчанию 0)

        Примеры:
        >>> car = Car("Renault", "Logan", 50, 20)
        """
        if not isinstance(make, str) or not isinstance(model, str):
            raise TypeError("Марка и модель автомобиля должны быть строками")
        self.make = make
        self.model = model

        if not isinstance(fuel_capacity, (int, float)) or fuel_capacity <= 0:
            raise ValueError("Ёмкость топливного бака должна быть положительным числом")
        self.fuel_capacity = fuel_capacity

        if not isinstance(fuel_level, (int, float)) or not (0 <= fuel_level <= fuel_capacity):
            raise ValueError("Уровень топлива должен быть в пределах от 0 до ёмкости бака")
        self.fuel_level = fuel_level


    def refuel(self, amount: float) -> None:
        """
        Заправка автомобиля.

        :param amount: Количество топлива для заправки

        :raise ValueError: Если количество топлива превышает ёмкость бака.

        Примеры:
        >>> car = Car("Toyota", "Corolla", 50, 20)
        >>> car.refuel(10)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Количество топлива для заправки должно быть типа int или float")
        if amount < 0:
            raise ValueError("Количество топлива не может быть отрицательным")
        if self.fuel_level + amount > self.fuel_capacity:
            raise ValueError("Превышен объём топлива, который можно залить в бак")
        ...


    def drive(self, fuel_needed: float) -> None:
        """
        Поездка на автомобиле.

        :param fuel_needed: Топливо, необходимое для поездки

        :raise ValueError: Если топлива недостаточно для поездки.

        Примеры:
        >>> car = Car("Toyota", "Corolla", 50, 20)
        >>> car.drive(10)
        """

        if not isinstance(fuel_needed, (int, float)):
            raise TypeError("Количество топлива для поездки должно быть типа int или float")
        if fuel_needed > self.fuel_level:
            raise ValueError("Недостаточно топлива для поездки")
        ...



class Cat:
    def __init__(self, name: str, age: int, health_status: str = "здоров"):
        """
        Создание объекта "Кошка"

        :param name: Имя кошки
        :param age: Возраст кошки
        :param health_status: Статус здоровья кошки (по умолчанию "здоров")

        Примеры:
        >>> cat = Cat("Барсик", 3)
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        self.name = name

        if not isinstance(age, int) or age <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        self.age = age

        if not isinstance(health_status, str) or health_status not in ["здоров", "болен", "восстанавливается"]:
            raise ValueError("Статус здоровья должен быть одним из: 'здоров', 'болен', 'восстанавливается'")
        self.health_status = health_status

    def feed(self, food_amount: float) -> None:
        """
        Кормление кошки.

        :param food_amount: Количество пищи в граммах

        :raise ValueError: Если количество пищи не положительное.

        Примеры:
        >>> cat = Cat("Барсик", 3)
        >>> cat.feed(100)
        """
        if not isinstance(food_amount, (int, float)):
            raise TypeError("Количество пищи должно быть типа int или float")
        if food_amount <= 0:
            raise ValueError("Количество пищи должно быть положительным числом")
        ...


    def play(self) -> None:
        """
        Игра с кошкой.

        При игре кошка становится более активной, но не меняет состояние здоровья, если оно не "болен".

        :raise ValueError: Если кошка больна.

        Примеры:
        >>> cat = Cat("Барсик", 3, "восстанавливается")
        >>> cat.play()
        """
        if self.health_status == "болен":
            raise ValueError("Кошка не может играть, пока она больна")
        ...


    def check_health(self) -> str:
        """
        Проверка состояния здоровья кошки.

        :return: Статус здоровья кошки

        Примеры:
        >>> cat = Cat("Барсик", 3, "болен")
        >>> cat.check_health()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
