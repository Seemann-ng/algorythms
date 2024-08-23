class Employee:
    def __init__(self, name: str, age: int, salary: int):
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__bonus = 0

    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    @property
    def salary(self) -> int:
        return self.__salary

    @property
    def bonus(self) -> int:
        return self.__bonus

    @bonus.setter
    def bonus(self, bonus: int):
        self.__bonus = bonus

    @property
    def total_salary(self) -> int:
        return self.__salary + self.__bonus


employee = Employee("John Doe", 25, 4000)

employee.bonus = 1500
print(f"Name: {employee.name}\n"
      f"Age: {employee.age}\n"
      f"Basic wage: ${employee.salary}\n"
      f"Bonus: ${employee.bonus}\n"
      f"Total salary: ${employee.total_salary}")
