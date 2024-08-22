class Employee:
    def __init__(self, name: str, age: int, salary: int):
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__bonus = 0

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age

    def get_salary(self) -> int:
        return self.__salary

    def set_bonus(self, bonus: int):
        self.__bonus = bonus

    def get_bonus(self) -> int:
        return self.__bonus

    def get_total_salary(self) -> int:
        return self.__salary + self.__bonus


employee = Employee("John Doe", 25, 4000)

employee.set_bonus(1500)
print(f"Name: {employee.get_name()}\n"
      f"Age: {employee.get_age()}\n"
      f"Basic wage: ${employee.get_salary()}\n"
      f"Bonus: ${employee.get_bonus()}\n"
      f"Total salary: ${employee.get_total_salary()}")