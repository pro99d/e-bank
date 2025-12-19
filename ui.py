import flet as ft
import account
import datetime

TEXT = "#2E3440"
COLOR = "3B4252"
BACKGROUND = "#D8DEE9"

DEFAULT_TEXT_SIZE = 20
DEFAULT_BIG_TEXT_SIZE = 60

def main(page: ft.Page):
    page.title = "Е-Банк"
    page.bgcolor = BACKGROUND
    
    def main_page():
        text = ft.Text("Спасибо, за использование Е-банка!", size= DEFAULT_BIG_TEXT_SIZE, bgcolor= BACKGROUND, color= TEXT)
        login_button = ft.Row([text, ft.Button(text= "Войти", color=COLOR, bgcolor= BACKGROUND, on_click= lambda _: page.go("/login"))], alignment= ft.MainAxisAlignment.SPACE_BETWEEN)
        balance_t = ft.Text(f"баланc: 0", size=DEFAULT_TEXT_SIZE, bgcolor= BACKGROUND, color= TEXT)
        page.views.append(
            ft.View(
                "/",
                [
                    login_button,
                    balance_t,
                ],
                bgcolor= BACKGROUND
            )
        )
        page.update()
    def login_page():
        page.views.append(
            ft.View(
                "/login",
                [
                    ft.Button("Home", color= COLOR, bgcolor= BACKGROUND, on_click= lambda _: page.go("/")),
                    ft.TextField("Name"),
                    ft.TextField("Name"),
                ],
                bgcolor= BACKGROUND
            )
        )
        page.update()
    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        route = e.route
        if route == "/":
            main_page()
        elif route== "/login":
            login_page()

    main_page()
    page.on_route_change = route_change


ft.app(target= main)
