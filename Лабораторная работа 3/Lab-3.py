class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name  # защищённый атрибут
        self._author = author  # защищённый атрибут

    @property
    def name(self) -> str:
        """ Возвращает название книги. """
        return self._name

    @property
    def author(self) -> str:
        """ Возвращает автора книги. """
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Класс бумажной книги. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)  # вызываем конструктор базового класса
        self.pages = pages  # используем свойство для установки значения

    @property
    def pages(self) -> int:
        """ Возвращает количество страниц. """
        return self._pages

    @pages.setter
    def pages(self, value: int):
        """ Устанавливает количество страниц с проверкой. """
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. Страниц: {self.pages}"


class AudioBook(Book):
    """ Класс аудиокниги. """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)  # вызываем конструктор базового класса
        self.duration = duration  # используем свойство для установки значения

    @property
    def duration(self) -> float:
        """ Возвращает продолжительность аудиокниги. """
        return self._duration

    @duration.setter
    def duration(self, value: float):
        """ Устанавливает продолжительность аудиокниги с проверкой. """
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = float(value)

    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}. Продолжительность: {self.duration} часов"
