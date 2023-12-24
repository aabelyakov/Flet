import flet as ft

def main(page: ft.Page):
    t = ft.Text(value="Hello, world!", color="green")
    page.controls.append(t)
    page.update()

# ft.app(target=main)
ft.app(target=main, port=8550, view=ft.WEB_BROWSER)