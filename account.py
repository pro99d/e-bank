import uuid
import random
import hashlib
import datetime


class Person:
    def __init__(self, name: str, last_name: str, age: datetime.date) -> None:
        self.name: str = name
        self.last_name: str = last_name
        self.age: datetime.date = age
        self.uuid = uuid.uuid4()

class Account:
    def __init__(self, owner: Person) -> None:
        self.money: float = 0
        self.user: Person = owner
        self._generate_uuid()

    def deposite(self, amount: float):
        self.money += amount

    def withdraw(self, amount: float) -> None:
        if self.money >= amount:
            self.money -= amount
        else:
            raise ValueError(f"balance is lower then {amount}")

    def _generate_uuid(self) -> None:
        self._uuid = uuid.uuid4()



def main():
    user = Person("oleg", "spitsyn", datetime.date(2010, 3, 31))

if __name__ == "__main__":
    main()
