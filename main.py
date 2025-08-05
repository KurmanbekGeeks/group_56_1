import flet as ft 


def main(page: ft.Page):
    page.title = "Мое первое приложение на Flet!"
    greeting_text = ft.Text("Привет, мир!")

    page.add(greeting_text)



ft.app(target=main)
# ft.app(target=main, view=ft.WEB_BROWSER)