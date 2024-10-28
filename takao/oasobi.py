import flet as ft

txt = ft.Text(value="Hello, world!")

def main(page: ft.Page):
    page.title = "Flet example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    def tile_clicked(e):
        page.add(ft.Text("Clicked!"))

    page.add(
        ft.Image(
            src="titlekamo.png",
            width=860,
            height=200,
            fit=ft.ImageFit.CONTAIN,
        ),
        ft.Row(
            [
                ft.Container(
                    content=ft.Text("ばつ"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLACK,
                    width=50,
                    height=50,
                    border_radius=5,
                ),
                ft.Container(
                    content=ft.Text("ここ，なぜか時刻が出るよ．"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BROWN,
                    width=700,
                    height=50,
                    border_radius=5,
                ),
                ft.Container(
                    content=ft.Text("H"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLACK,
                    width=50,
                    height=50,
                    border_radius=5,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.Container(
                    content=ft.Text("見るとこ"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.CYAN_200,
                    width=300,
                    height=200,
                    border_radius=5,
                    ink=True,
                    on_click=lambda e: print("見るよ～"),
                ),
                ft.Container(
                    content=ft.Text("ここ絵だね．"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.WHITE,
                    width=200,
                    height=200,
                    border_radius=5,
                ),
                ft.Container(
                    content=ft.Text("作るとこ"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.CYAN_200,
                    width=300,
                    height=200,
                    border_radius=5,
                    ink=True,
                    on_click=lambda e: print("作るよ～"),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.Container(
                    content=ft.Text("説明はよく読もう．"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.WHITE,
                    width=860,
                    height=50,
                    border_radius=5,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

ft.app(target=main)

#https://rakuraku-engineer.com/posts/flet-base/