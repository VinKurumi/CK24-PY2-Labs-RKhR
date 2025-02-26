import doctest


class Car:
    def __init__(self, brand: str, max_speed: int, fuel_consumption: float):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param brand: Марка автомобиля
        :param max_speed: Максимальная скорость автомобиля (км/ч)
        :param fuel_consumption: Расход топлива автомобиля (л/100 км)

        Примеры:
        >>> car = Car("Toyota", 200, 8.5)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть типа str")
        if not isinstance(max_speed, int):
            raise TypeError("Максимальная скорость должна быть типа int")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом")
        if not isinstance(fuel_consumption, (int, float)):
            raise TypeError("Расход топлива должен быть типа int или float")
        if fuel_consumption <= 0:
            raise ValueError("Расход топлива должен быть положительным числом")

        self.brand = brand
        self.max_speed = max_speed
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: float) -> float:
        """
        Расчет времени поездки на заданное расстояние.

        :param distance: Расстояние поездки (км)
        :return: Время поездки (часы)

        Примеры:
        >>> car = Car("Toyota", 200, 8.5)
        >>> car.drive(100)
        """
        if not isinstance(distance, (int, float)):
            raise TypeError("Расстояние должно быть типа int или float")
        if distance <= 0:
            raise ValueError("Расстояние должно быть положительным числом")
        ...

    def refuel(self, fuel_amount: float) -> None:
        """
        Заправка автомобиля.

        :param fuel_amount: Количество топлива для заправки (л)
        :raise ValueError: Если количество топлива меньше или равно нулю

        Примеры:
        >>> car = Car("Toyota", 200, 8.5)
        >>> car.refuel(30)
        """
        if not isinstance(fuel_amount, (int, float)):
            raise TypeError("Количество топлива должно быть типа int или float")
        if fuel_amount <= 0:
            raise ValueError("Количество топлива должно быть положительным числом")
        ...


class Airplane:
    def __init__(self, model: str, max_altitude: int, passenger_capacity: int):
        """
        Создание и подготовка к работе объекта "Самолет"

        :param model: Модель самолета
        :param max_altitude: Максимальная высота полета (м)
        :param passenger_capacity: Вместимость пассажиров

        Примеры:
        >>> airplane = Airplane("Boeing 747", 13000, 416)  # инициализация экземпляра класса
        """
        if not isinstance(model, str):
            raise TypeError("Модель самолета должна быть типа str")
        if not isinstance(max_altitude, int):
            raise TypeError("Максимальная высота должна быть типа int")
        if max_altitude <= 0:
            raise ValueError("Максимальная высота должна быть положительным числом")
        if not isinstance(passenger_capacity, int):
            raise TypeError("Вместимость пассажиров должна быть типа int")
        if passenger_capacity <= 0:
            raise ValueError("Вместимость пассажиров должна быть положительным числом")

        self.model = model
        self.max_altitude = max_altitude
        self.passenger_capacity = passenger_capacity

    def take_off(self) -> None:
        """
        Взлет самолета.

        Примеры:
        >>> airplane = Airplane("Boeing 747", 13000, 416)
        >>> airplane.take_off()
        """
        ...

    def land(self) -> None:
        """
        Посадка самолета.

        Примеры:
        >>> airplane = Airplane("Boeing 747", 13000, 416)
        >>> airplane.land()
        """
        ...


class Ship:
    def __init__(self, name: str, displacement: float, max_speed: int):
        """
        Создание и подготовка к работе объекта "Корабль"

        :param name: Название корабля
        :param displacement: Водоизмещение корабля (тонны)
        :param max_speed: Максимальная скорость корабля (узлы)

        Примеры:
        >>> ship = Ship("Titanic", 52310, 24)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название корабля должно быть типа str")
        if not isinstance(displacement, (int, float)):
            raise TypeError("Водоизмещение должно быть типа int или float")
        if displacement <= 0:
            raise ValueError("Водоизмещение должно быть положительным числом")
        if not isinstance(max_speed, int):
            raise TypeError("Максимальная скорость должна быть типа int")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом")

        self.name = name
        self.displacement = displacement
        self.max_speed = max_speed

    def sail(self, distance: float) -> float:
        """
        Расчет времени плавания на заданное расстояние.

        :param distance: Расстояние плавания (морские мили)
        :return: Время плавания (часы)

        Примеры:
        >>> ship = Ship("Titanic", 52310, 24)
        >>> ship.sail(100)
        """
        if not isinstance(distance, (int, float)):
            raise TypeError("Расстояние должно быть типа int или float")
        if distance <= 0:
            raise ValueError("Расстояние должно быть положительным числом")
        ...

    def dock(self) -> None:
        """
        Швартовка корабля.

        Примеры:
        >>> ship = Ship("Titanic", 52310, 24)
        >>> ship.dock()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
