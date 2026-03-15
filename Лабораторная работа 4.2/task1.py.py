class Employee:
    """
    Базовый класс сотрудника
    """
    def __init__(self, name: str, salary: float):
        """
        Создает сотрудника.
        :param name: имя сотрудника
        :param salary: зарплата сотрудника
        """
        self.name = name
        self._salary = salary
    def work(self) -> str:
        """
        Метод, описывающий работу сотрудника.
        """
        return f"{self.name} работает."
    def get_salary(self) -> float:
        """
        Возвращает зарплату сотрудника.
        """
        return self._salary
    def __str__(self) -> str:
        """
        Строковое представление объекта.
        """
        return f"Employee {self.name}, salary = {self._salary}"
    def __repr__(self) -> str:
        """
        Представление объекта для разработчика.
        """
        return f"Employee(name={self.name}, salary={self._salary})"
class Developer(Employee):
    """
    Класс разработчика, наследуется от Employee
    """
    def __init__(self, name: str, salary: float, language: str):
        """
        Создает разработчика.

        :param name: имя сотрудника
        :param salary: зарплата
        :param language: язык программирования
        """
        super().__init__(name, salary)
        self.language = language
    def work(self) -> str:
        """
        Переопределенный метод работы разработчика.
        """
        return f"{self.name} пишет код на {self.language}"
    def write_code(self) -> str:
        """
        Дополнительный метод разработчика.
        """
        return f"{self.name} разрабатывает программу"
    def __str__(self) -> str:
        """
        Строковое представление разработчика.
        """
        return f"Developer {self.name}, language = {self.language}"
    def __repr__(self) -> str:
        """
        Представление разработчика для разработчика.
        """
        return f"Developer(name={self.name}, salary={self._salary}, language={self.language})"
if __name__ == "__main__":
    dev1 = Developer("Ivan", 4000, "Python")
    print(dev1)
    print(dev1.work())
    print(dev1.write_code())
    print(dev1.get_salary())