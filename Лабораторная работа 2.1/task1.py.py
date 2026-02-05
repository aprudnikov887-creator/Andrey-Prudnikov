# TODO Написать 3 класса с документацией и аннотацией типов
class Tree:
    """
    Класс, представляющий дерево.
    """

    def __init__(self, height: float, age: int, species: str):
        """
        Инициализация объекта дерева.

        :param height: Высота дерева в метрах.
        :param age: Возраст дерева в годах.
        :param species: Вид дерева.

        >>> t = Tree(15.5, 50, "Дуб")
        """
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом.")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        if not species.strip():
            raise ValueError("Вид дерева не может быть пустым.")

        self.height = height
        self.age = age
        self.species = species

    def grow(self, years: int) -> None:
        """
        Увеличивает возраст дерева на указанное количество лет и корректирует высоту.

        :param years: Количество лет, на которое дерево растёт.
        :return: None

        >>> t = Tree(10, 20, "Сосна")
        >>> t.grow(5)
        """
        if not isinstance(years, int):
            raise TypeError("Прибавляемый возраст должна быть типа int")
        if years < 0:
            raise ValueError("Прибавляемый возраст должен быть положительным числом")
        pass

    def get_info(self) -> str:
        """
        Возвращает строку с информацией о дереве.

        :return: Строка с описанием дерева.

        >>> t = Tree(25, 100, "Баобаб")
        >>> t.get_info()
        """
        # Реализация не требуется
        pass

    def lose_leaves(self, season: str) -> bool:
        """
        Определяет, теряет ли дерево листья в зависимости от сезона.

        :param season: Сезон года (зима, весна, лето, осень).
        :return: True, если листья опадают, иначе False.

        >>> t = Tree(12, 30, "Берёза")
        >>> t.lose_leaves("осень")
        """
        # Реализация не требуется
        pass


class Profile:
    """
    Класс, представляющий кошелек.
    """

    def __init__(self, username: str, age: int, residence: str):
        """
        Инициализация профиля пользователя.

        :param username: Имя и Фамилия пользователя.
        :param age: Возраст пользователя.
        :param residence: Место проживания пользователя.

        >>> p = Profile("Иван Иванов", 49, "Удомля")
        """
        if age <= 0:
            raise ValueError("Возраст должен быть положительным числом.")
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть типа str")

        if not isinstance(residence, str):
            raise TypeError("Место проживания должно быть типа str")
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")

        self.age = age
        self.residence = residence
        self.username = username

    def friends(self) -> None:
        """
        Выводит количество друзей.

        :return: Количество друзей

        >>> p = Profile("Иван Иванов", 49, "Удомля")
        >>> p.friends()
        """
        pass

    def get_older(self, years: int) -> None:
        """
        Прибавляет возраст пользователю.
        :param years: Прибавляемый возраст.


        >>> p = Profile("Иван Иванов", 49, "Удомля")
        >>> p.get_older(1)
        """
        if years <= 0:
            raise ValueError("Прибавляемый возраст должен быть положительным числом.")
        if not isinstance(years, int):
            raise TypeError("Прибавляемый возраст должен быть типа int")
        pass

    def status(self) -> str:
        """
        Выводит статус пользоваетеля.

        :return: Статус пользователя.

        >>> p = Profile("Иван Иванов", 49, "Удомля")
        >>> p.status()
        """
        # Реализация не требуется
        pass
class Product:
    """
    Класс, представляющий продукт в магазине.
    """

    def __init__(self, product_name: str, quantity: int, description: str):
        """
        Инициализация продукта.

        :param product_name: Название продукта
        :param quantity: Количество продукта в наличии
        :param description: Описание продукта

        >>> pr = Product("Шоколад горький", 120, "Низкокалорийный")
        """
        if quantity < 0:
            raise ValueError("Количество продуктов должно быть положительным числом.")
        if not isinstance(product_name, str):
            raise TypeError("Название продукта должно быть типа str")

        if not isinstance(description, str):
            raise TypeError("Описание продукта должно быть типа str")
        if not isinstance(quantity, int):
            raise TypeError("Количество продукта должен быть типа int")

        self.quantity = quantity
        self.product_name = product_name
        self.description = description

    def quantity_from_the_supplier(self) -> None:
        """
        Выводит количество продукта у поставщика

        :return: Количество продукта у поставщика

        >>> pr = Product("Шоколад горький", 120, "Низкокалорийный")
        >>> pr.quantity_from_the_supplier()
        """
        pass

    def change_quantity(self, number) -> None:
        """

        Прибавляет или убавляет количество товара.
        :param number: изменяемое количество товара


        >>> pr = Product("Шоколад горький", 120, "Низкокалорийный")
        >>> pr.change_quantity(100)
        """
        if not isinstance(number, int):
            raise TypeError("Изменяемое количество продукта должно быть типа int")
        pass

    def required_quanity(self) -> None:
        """
        Выводит необходимое количество продукта

        :return: необходимое количество продукта

        >>> pr = Product("Шоколад горький", 120, "Низкокалорийный")
        >>> pr.required_quanity()
        """
        pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
