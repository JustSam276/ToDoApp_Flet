import flet as ft
from VED import build as b


def main(page: ft.Page):
    page.title = "Todo App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    # application instance of the class
    todo = b.build(page)
    # todo2 = TodoApp()

    # adding application's root control to the page
    page.add(todo)

ft.app(target=main)