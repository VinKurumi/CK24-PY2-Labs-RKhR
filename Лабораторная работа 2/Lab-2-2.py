BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    """ Класс книги. """
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    """ Класс библиотеки. """
    def __init__(self, books=None):
        self.books = books if books is not None else []  # если books не передан, инициализируем пустым списком

    def get_next_book_id(self):
        if not self.books:
            return 1  # если список книг пуст, возвращаем 1
        return self.books[-1].id + 1  # иначе возвращаем id последней книги + 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):  # используем enumerate для получения пар (индекс, книга)
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")  # если книга не найдена, вызываем ошибку


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
