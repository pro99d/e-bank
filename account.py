import uuid
import random
import hashlib
import datetime
import shifr


class Person:
    def __init__(self, name: str, last_name: str, born_date: datetime.date, email: str, password: str) -> None:
        self.name: str = name
        self.last_name: str = last_name
        self.born_date: datetime.date = born_date
        self.email: str = email
        self.password: str = password

    def register(self):
        with open('base.txt') as email_list:
            emails = email_list.readlines()
            if self.email not in emails:
                with open('users.txt', 'a', encoding='utf-8') as user_list:
                    user_list.write(shifr.codification(self.name)+','+shifr.codification(self.last_name)+','+str(
                        self.born_date)+','+shifr.codification(self.email)+','+shifr.codification(self.password))

    def login(self):
        with open('users.txt') as user_list:
            users = user_list.readlines()
        for i in users:
            if i == shifr.codification(self.name)+','+shifr.codification(self.last_name)+','+str(self.born_date)+','+shifr.codification(self.email)+','+shifr.codification(self.password):
                return True
        return False


class Account:
    def __init__(self, owner: Person) -> None:
        self.money: float = 0
        self.user: Person = owner

    def deposite(self, amount: float):
        self.money += amount

    def withdraw(self, amount: float) -> None:
        if self.money >= amount:
            self.money -= amount
        else:
            raise ValueError(f"balance is lower then {amount}")
