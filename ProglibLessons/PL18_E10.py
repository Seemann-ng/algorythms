ranks = ["PVT", "CPR", "SGT", "MSG", "FLT", "SLT", "CPT", "MJR", "COL"]


def print_info(cls):
    class NewClass(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            print(f"New playable character of type {cls.__name__} with attributes: {self.__dict__}.")

        def get_rank(self):
            print(f"Character {self.name} has the following rank: {self._Soldier__rank}.")

        def promote(self):
            super().promote()
            print(f"{self.name} has been promoted, they are {self._Soldier__rank} now.")

        def demote(self):
            super().demote()
            print(f"{self.name} has been demoted, they are {self._Soldier__rank} now.")

    return NewClass


@print_info
class Soldier:
    def __init__(self, name: str, rank: str, service_number: str):
        self.name = name
        self.__rank = rank
        self.__service_number = service_number

    def verifyServiceNumber(self, service_number):
        return self.__service_number == service_number

    def promote(self):
        if self.__rank in ranks[:-1]:
            self.__rank = ranks[ranks.index(self.__rank) + 1]

    def demote(self):
        if self.__rank in ranks[1:]:
            self.__rank = ranks[ranks.index(self.__rank) - 1]


soldier1 = Soldier("John Doe", "MJR", "12345")
soldier2 = Soldier("John Snow", "PVT", "98475")

soldier1.get_rank()
soldier1.promote()
soldier1.promote()
soldier1.demote()
print(str(soldier1.verifyServiceNumber("12345")))

soldier2.get_rank()
soldier2.promote()
soldier2.demote()
soldier2.demote()
print(str(soldier2.verifyServiceNumber("12345")))
