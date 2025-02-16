if __name__ == "__main__":
    class ElectronicDevice:
        """Базовый класс для представления электронных устройств.

        Атрибуты:
            manufacturer (str): Производитель устройства
            model (str): Модель устройства
            os (str): Операционная система
        """

        def __init__(self, manufacturer: str, model: str, os: str) -> None:
            """
            Создание экземпляра ElectronicDevice.

            :param manufacturer: Производитель устройства
            :param model: Модель устройства
            :param os: Установленная операционная система

            Примеры:
            >>> electronicdevice = ElectronicDevice("Apple", "Mac", "iOS")

            """
            self.manufacturer = manufacturer
            self.model = model
            self.os = os

        def __str__(self) -> str:
            """
            Возвращает информацию об устройстве в удобочитаемом формате.

            :return: Информация об устройстве.

             Примеры:
            >>> electronicdevice = ElectronicDevice("Apple", "Mac", "iOS")
            >>> print(electronicdevice)
            """
            return f"{self.manufacturer} {self.model} ({self.os})"

        def __repr__(self) -> str:
            """
            Возвращает однозначное строковое представление объекта.

            :return: Однозначное строковое представление объекта.

            Примеры:
            >>> electronicdevice = ElectronicDevice("Apple", "Mac", "iOS")
            >>> print(repr(electronicdevice))
            """
            return f"ElectronicDevice('{self.manufacturer}', '{self.model}', '{self.os}')"

        def get_info(self) -> str:
            """
            Возвращает базовую информацию об устройстве.

            return: Базовая информация об устройстве.

            Примеры:
            >>> electronicdevice = ElectronicDevice("Apple", "Mac", "iOS")
            >>> electronicdevice.get_info()
            """
            return f"Устройство: {self.model} ({self.manufacturer})"


    class Smartphone(ElectronicDevice):
        """Класс для представления смартфонов. Наследуется от ElectronicDevice.

        Дополнительные атрибуты:
            screen_size (float): Диагональ экрана в дюймах
            __battery_level (int): Текущий уровень заряда батареи (приватный)
        """

        def __init__(self, manufacturer: str, model: str, os: str, screen_size: float) -> None:
            """
            Расширяет конструктор базового класса параметром screen_size.

            :param manufacturer: Производитель устройства
            :param model: Модель устройства
            :param os: Установленная операционная система
            :param screen_size: Диагональ экрана в дюймах

            Примеры:
            >>> smartphone = Smartphone("Apple", "iPhone", "iOS", 6)
            """
            super().__init__(manufacturer, model, os)
            self.screen_size = screen_size
            self.__battery_level = 100  # Инкапсуляция: защищаем от прямого изменения

        def __str__(self) -> str:
            """
            Перегрузка строкового представления с добавлением информации об экране.

            :return: Информация об устройстве.

             Примеры:
            >>> smartphone = Smartphone("Apple", "iPhone", "iOS", 6)
            >>> print(smartphone)
            """
            return f"{super().__str__()}, Экран: {self.screen_size}\""

        def __repr__(self) -> str:
            """
            Перегрузка repr с добавлением screen_size.

            :return: Однозначное строковое представление объекта.

            Примеры:
            >>> smartphone = Smartphone("Apple", "iPhone", "iOS", 6)
            >>> print(repr(smartphone))
            """
            return f"Smartphone('{self.manufacturer}', '{self.model}', '{self.os}', {self.screen_size})"

        def get_info(self) -> str:
            """Перегрузка метода для добавления информации об экране.

            Причина перегрузки: необходимость отображения специфичного атрибута класса.

            return: Базовая информация об устройстве.

            Примеры:
            >>> smartphone = Smartphone("Apple", "iPhone", "iOS", 6)
            >>> smartphone.get_info()
            """
            base_info = super().get_info()
            return f"{base_info}, Диагональ экрана: {self.screen_size}\""

        def check_battery(self) -> str:
            """
            Возвращает уровень заряда батареи.

            :return: Уровень заряда.

            Примеры:
            >>> smartphone = Smartphone("Apple", "iPhone", "iOS", 6)
            >>> smartphone.check_battery()
            """
            return f"Уровень заряда: {self.__battery_level}%"

        def charge_battery(self, percent: int) -> None:
            """Заряжает батарею на указанный процент.

            :param percent: Процент для зарядки (0-100)

            :raise ValueError: Если процент для зарядки не положительный.

            Примеры:
            >>> smartphone = Smartphone("Apple", "iPhone", "iOS", 6)
            >>> smartphone.charge_battery(15)
            """
            if percent < 0:
                raise ValueError("Процент заряда не может быть отрицательным")
            self.__battery_level = min(100, self.__battery_level + percent)

    pass
