import flet as ft
import account
import datetime

DEFAULT_TEXT_SIZE = 20
DEFAULT_BIG_TEXT_SIZE = 60

def main(page: ft.Page):
    page.title = "Е-Банк"
    balance = account.Account(account.Person("Noname", "Какой-та", datetime.date(2025, 12, 16)))
    text = ft.Text("Спасибо, за использование Е-банка!", size= DEFAULT_BIG_TEXT_SIZE)
    balance = ft.Text(f"баланc: {str(balance.money)}", size=DEFAULT_TEXT_SIZE)
    page.add(text, balance)
    page.update()


ft.app(target= main)
