import flet as ft 


def main(page: ft.Page):
    page.title = "Мое первое приложение на Flet!"
    greeting_text = ft.Text("Привет, мир!")

    page.theme_mode = ft.ThemeMode.LIGHT

    name_input = ft.TextField(label='Введите имя')

    def on_button_click(_):
        name = name_input.value.strip()
        print(name)

        # greeting_text = ft.Text(f'Привет, {name}')

        if name:
            greeting_text.value = f'Привет, {name}'
        else:
            greeting_text.value = "Пожалуйста, введите имя!"


        page.update()


    greet_button = ft.ElevatedButton('send', on_click=on_button_click)
    greet_button_text = ft.TextButton('send', on_click=on_button_click)

    greet_button_icon = ft.IconButton(
        icon=ft.Icons.SEND, tooltip='Отправить', on_click=on_button_click, icon_color=ft.Colors.GREEN)
    

    page.add(greeting_text, name_input, greet_button, greet_button_text, greet_button_icon)



# ft.app(target=main)
ft.app(target=main, view=ft.WEB_BROWSER)