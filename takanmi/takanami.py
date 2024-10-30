#円と四角形が描けます

import flet as ft
from flet import Text, ElevatedButton, PopupMenuItem, Row, Icon, Container, Stack, PopupMenuButton, margin, colors, icons

class AppHeader(ft.Column):
    def __init__(self, file, edit, tool, display, page, on_shape_select):
        super().__init__()
        self.page = page
        self.on_shape_select = on_shape_select

        file_button = ElevatedButton(text="file")
        edit_button = ElevatedButton(text="edit")
        tool_button = ElevatedButton(text="tool")
        display_button = ElevatedButton(text="display")
        self.appbar_items = [
            PopupMenuItem(text="Draw Circle", on_click=lambda e: self.on_shape_select("circle")),
            PopupMenuItem(text="Draw Square", on_click=lambda e: self.on_shape_select("square")),
        ]

        self.page.appbar = ft.AppBar(
            leading=Icon(icons.TRIP_ORIGIN_ROUNDED),
            leading_width=60,
            title=Text(value="Project name", size=24, text_align="center"),
            center_title=False,
            toolbar_height=50,
            bgcolor=colors.SURFACE_VARIANT,
            actions=[
                Container(
                    content=Row(
                        [
                            file_button,
                            edit_button,
                            tool_button,
                            display_button,
                            PopupMenuButton(
                                items=self.appbar_items
                            ),
                        ],
                        alignment="spaceBetween",
                    ),
                    margin=margin.only(left=25, right=50)
                )
            ],
        )

    def build(self):
        return self.page.appbar


class ShapeDrawer:
    def __init__(self, page):
        self.page = page
        self.shape_container = Stack(expand=True)
        self.current_shape = None

    def draw_shape(self, shape):
        self.current_shape = shape

        if shape == "circle":
            shape_element = ft.Draggable(
                content=Container(
                    width=100,
                    height=100,
                    bgcolor=colors.BLUE,
                    border_radius=50,
                    alignment=ft.alignment.center,
                )
            )
        elif shape == "square":
            shape_element = ft.Draggable(
                content=Container(
                    width=100,
                    height=100,
                    bgcolor=colors.RED,
                    alignment=ft.alignment.center,
                )
            )

        self.shape_container.controls.append(shape_element)
        self.page.update()


def main(page: ft.Page):
    page.title = "Shape Drawer"
    page.padding = 10
    shape_drawer = ShapeDrawer(page)

    def on_shape_select(shape):
        shape_drawer.draw_shape(shape)

    AppHeader("file", "edit", "tool", "display", page, on_shape_select)

    layout = Row(
        controls=[shape_drawer.shape_container],
        tight=False,
        expand=True,
        vertical_alignment="start",
    )

    page.add(layout)
    page.update()


ft.app(target=main)
