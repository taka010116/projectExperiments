import flet as ft


def main(page: ft.Page):
    page.title = "サンプルプログラム"  # タイトル
    page.window_width = 600  # 幅
    page.window_height = 300  # 高さ
    page.theme = ft.Theme(color_scheme_seed="green")

    # 部品を配置する
    page.add(
        ft.Column(
            [
                ft.Text("ここは1行目"),
                ft.Row(
                    [
                        ft.Text("ここは2行目"),
                        ft.TextField(hint_text="文字を入力してください"),
                    ]
                ),
                ft.Row([ft.ElevatedButton("OK"), ft.ElevatedButton("キャンセル")]),
            ]
        )
    )


ft.app(target=main)