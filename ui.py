import datetime

import flet as ft

import account

TEXT = "#2E3440"
COLOR = "3B4252"
BACKGROUND = "#ECEff4"

DEFAULT_TEXT_SIZE = 20
DEFAULT_BIG_TEXT_SIZE = 50


def main(page: ft.Page):
    page.title = "Е-Банк"
    page.bgcolor = BACKGROUND

    def main_page():
        text = ft.Text("Спасибо, за использование Е-банка!",
                       size=DEFAULT_BIG_TEXT_SIZE, bgcolor=BACKGROUND, color=TEXT)
        login_button = ft.Row([text, ft.Button(text="Войти", color="#2E3440", bgcolor="#D8DEE9",
                              on_click=lambda _: page.go("/login"))], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        balance_t = ft.Text(f"баланc: 0", size=DEFAULT_TEXT_SIZE,
                            bgcolor=BACKGROUND, color=TEXT)
        page.views.append(
            ft.View(
                "/",
                [
                    login_button,
                    balance_t,
                ],
                bgcolor=BACKGROUND
            )
        )

    def login_page():
        name = ft.TextField(hint_text="Name", color=TEXT,
                            bgcolor=BACKGROUND, border_color="#3B4252")
        last_name = ft.TextField(
            hint_text="last name", color=TEXT, bgcolor=BACKGROUND, border_color="#3B4252")
        email = ft.TextField(hint_text="example@example.com",
                             color=TEXT, bgcolor=BACKGROUND, border_color="#3B4252")

        def upd_data(e):
            date_text.value = str(date.value)
            page.update()
        date = ft.DatePicker(on_change=upd_data)
        date_text = ft.Text(color=TEXT, bgcolor=BACKGROUND)

        def show():
            date.open = True
            page.update()

        def password_update(_= None):
            if password1.value != password2.value:
                dialog = ft.AlertDialog(modal=True, title=ft.Text(
                    "Пароли не совпадают!", size=DEFAULT_TEXT_SIZE, bgcolor=BACKGROUND, color=TEXT))
                dialog.open = True
                return False
            page.update()
            return True 

        def register():
            nme = name.value
            lname = last_name.value
            em = email.value
            passw = password1.value
            date_ = date.value
            
            if password_update() and nme and lname and em and passw and date_:
                user = account.Person(nme, lname, date_, em, passw)
                user.register()
            else:
                print("failed to register")



        def login():
            nme = name.value
            lname = last_name.value
            em = email.value
            passw = password1.value
            date_ = date.value
            
            if nme and lname and em and passw and date_:
                user = account.Person(nme, lname, date_, em, passw)
                login = user.login()
                if not login:
                    print(f"user {em} is not in database")
                else:
                    print(f"user {em}")
        date_utils = ft.Row(
            [
                date_text,
                ft.Button("Выбрать дату", color="#2E3440", bgcolor="#D8DEE9", on_click=lambda _: show())
            ]
        )
        password1 = ft.TextField(password=True, can_reveal_password=True,
                                 on_change=password_update, color=TEXT, bgcolor=BACKGROUND, border_color="#3B4252")
        password2 = ft.TextField(password=True, can_reveal_password=True,
                                 on_change=password_update, color=TEXT, bgcolor=BACKGROUND, border_color="#3B4252")

        container = ft.Container(ft.Column([
            ft.Text("Имя", size=DEFAULT_TEXT_SIZE,
                    bgcolor=BACKGROUND, color=TEXT),
            name,
            ft.Text("Фамилия", size=DEFAULT_TEXT_SIZE,
                    bgcolor=BACKGROUND, color=TEXT),
            last_name,
            ft.Text("Почта", size=DEFAULT_TEXT_SIZE,
                    bgcolor=BACKGROUND, color=TEXT),
            email,
            ft.Text("Дата рождения", size=DEFAULT_TEXT_SIZE,
                    bgcolor=BACKGROUND, color=TEXT),
            date,
            date_utils,
            ft.Text("Введите пароль", size=DEFAULT_TEXT_SIZE,
                    bgcolor=BACKGROUND, color=TEXT),
            password1,

            ft.Text("Повторите пароль", size=DEFAULT_TEXT_SIZE,
                    bgcolor=BACKGROUND, color=TEXT),
            password2,
            ft.Row([
                ft.Button("Вход", color="#2E3440", bgcolor="#D8DEE9", on_click=lambda _: login()),
                ft.Button("Зарегестрироваться", color="#2E3440", bgcolor="#D8DEE9", on_click=lambda _: register()),
            ])

        ],)


        )
        page.views.append(
            ft.View(
                "/login",
                [
                    ft.Row(
                        [
                            ft.Button("Домашняя страница", color="#2E3440",
                                      bgcolor="#D8DEE9", on_click=lambda _: page.go("/")),
                        ],
                        alignment=ft.MainAxisAlignment.START
                    ),
                    ft.Row([container], alignment=ft.MainAxisAlignment.CENTER),
                ],
                bgcolor=BACKGROUND
            )
        )

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        route = e.route
        if route == "/":
            main_page()
        elif route == "/login":
            login_page()
        else:
            page.views.append(
                ft.View(
                    "/404",
                    [ft.Button("Домашняя страница", color="#2E3440",
                               bgcolor="#D8DEE9", on_click=lambda _: page.go("/"))]
                )
            )
        page.update()

    main_page()
    page.on_route_change = route_change
    page.update()


ft.app(target=main)
