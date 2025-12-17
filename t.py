
class Person:
    def __init__(self, name: str, last_name: str, age: int) -> None:
        self.name: int = name
        self.last_name: int = last_name
        self.age: int = age

class Account:
    def __init__(self, owner: Person) -> None:
        self.money: float = 0
        self.owner: Person = owner
        
