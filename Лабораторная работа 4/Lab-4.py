class Car:
    """
    Базовый класс, представляющий автомобиль.

    Атрибуты:
        brand (str): Марка автомобиля.
        max_speed (int): Максимальная скорость автомобиля (км/ч).
        fuel_consumption (float): Расход топлива автомобиля (л/100 км).
    """

    def __init__(self, brand: str, max_speed: int, fuel_consumption: float):
        """
        Инициализация объекта "Автомобиль".

        :param brand: Марка автомобиля.
        :param max_speed: Максимальная скорость автомобиля (км/ч).
        :param fuel_consumption: Расход топлива автомобиля (л/100 км).
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

    def __str__(self) -> str:
        """
        Возвращает строковое представление автомобиля.

        :return: Строковое представление автомобиля.
        """
        return f"Автомобиль {self.brand} с максимальной скоростью {self.max_speed} км/ч и расходом топлива {self.fuel_consumption} л/100 км."

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление автомобиля.

        :return: Формальное строковое представление автомобиля.
        """
        return f"Car(brand={self.brand}, max_speed={self.max_speed}, fuel_consumption={self.fuel_consumption})"

    def drive(self, distance: float) -> float:
        """
        Расчет времени поездки на заданное расстояние.

        :param distance: Расстояние поездки (км).
        :return: Время поездки (часы).
        """
        if not isinstance(distance, (int, float)):
            raise TypeError("Расстояние должно быть типа int или float")
        if distance <= 0:
            raise ValueError("Расстояние должно быть положительным числом")
        return distance / self.max_speed


class PassengerCar(Car):
    """
    Дочерний класс, представляющий легковой автомобиль.

    Атрибуты:
        brand (str): Марка автомобиля.
        max_speed (int): Максимальная скорость автомобиля (км/ч).
        fuel_consumption (float): Расход топлива автомобиля (л/100 км).
        passenger_capacity (int): Вместимость пассажиров.
    """

    def __init__(self, brand: str, max_speed: int, fuel_consumption: float, passenger_capacity: int):
        """
        Инициализация объекта "Легковой автомобиль".

        :param brand: Марка автомобиля.
        :param max_speed: Максимальная скорость автомобиля (км/ч).
        :param fuel_consumption: Расход топлива автомобиля (л/100 км).
        :param passenger_capacity: Вместимость пассажиров.
        """
        super().__init__(brand, max_speed, fuel_consumption)
        if not isinstance(passenger_capacity, int):
            raise TypeError("Вместимость пассажиров должна быть типа int")
        if passenger_capacity <= 0:
            raise ValueError("Вместимость пассажиров должна быть положительным числом")

        self.passenger_capacity = passenger_capacity

    def __str__(self) -> str:
        """
        Возвращает строковое представление легкового автомобиля.

        :return: Строковое представление легкового автомобиля.
        """
        return f"Легковой автомобиль {self.brand} с максимальной скоростью {self.max_speed} км/ч, расходом топлива {self.fuel_consumption} л/100 км и вместимостью {self.passenger_capacity} пассажиров."

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление легкового автомобиля.

        :return: Формальное строковое представление легкового автомобиля.
        """
        return f"PassengerCar(brand={self.brand}, max_speed={self.max_speed}, fuel_consumption={self.fuel_consumption}, passenger_capacity={self.passenger_capacity})"

    def drive(self, distance: float) -> float:
        """
        Перегрузка метода drive для учета дополнительного времени на остановки для пассажиров.

        :param distance: Расстояние поездки (км).
        :return: Время поездки с учетом остановок (часы).
        """
        base_time = super().drive(distance)
        # Предположим, что на каждые 100 км делается одна остановка на 0.5 часа
        stops = distance // 100
        return base_time + stops * 0.5


class Truck(Car):
    """
    Дочерний класс, представляющий грузовой автомобиль.

    Атрибуты:
        brand (str): Марка автомобиля.
        max_speed (int): Максимальная скорость автомобиля (км/ч).
        fuel_consumption (float): Расход топлива автомобиля (л/100 км).
        cargo_capacity (float): Грузоподъемность автомобиля (тонны).
    """

    def __init__(self, brand: str, max_speed: int, fuel_consumption: float, cargo_capacity: float):
        """
        Инициализация объекта "Грузовой автомобиль".

        :param brand: Марка автомобиля.
        :param max_speed: Максимальная скорость автомобиля (км/ч).
        :param fuel_consumption: Расход топлива автомобиля (л/100 км).
        :param cargo_capacity: Грузоподъемность автомобиля (тонны).
        """
        super().__init__(brand, max_speed, fuel_consumption)
        if not isinstance(cargo_capacity, (int, float)):
            raise TypeError("Грузоподъемность должна быть типа int или float")
        if cargo_capacity <= 0:
            raise ValueError("Грузоподъемность должна быть положительным числом")

        self.cargo_capacity = cargo_capacity

    def __str__(self) -> str:
        """
        Возвращает строковое представление грузового автомобиля.

        :return: Строковое представление грузового автомобиля.
        """
        return f"Грузовой автомобиль {self.brand} с максимальной скоростью {self.max_speed} км/ч, расходом топлива {self.fuel_consumption} л/100 км и грузоподъемностью {self.cargo_capacity} тонн."

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление грузового автомобиля.

        :return: Формальное строковое представление грузового автомобиля.
        """
        return f"Truck(brand={self.brand}, max_speed={self.max_speed}, fuel_consumption={self.fuel_consumption}, cargo_capacity={self.cargo_capacity})"

    def load_cargo(self, weight: float) -> None:
        """
        Загрузка груза в автомобиль.

        :param weight: Вес груза (тонны).
        :raise ValueError: Если вес груза превышает грузоподъемность.
        """
        if not isinstance(weight, (int, float)):
            raise TypeError("Вес груза должен быть типа int или float")
        if weight <= 0:
            raise ValueError("Вес груза должен быть положительным числом")
        if weight > self.cargo_capacity:
            raise ValueError("Вес груза превышает грузоподъемность автомобиля")
        print(f"Груз весом {weight} тонн успешно загружен.")
