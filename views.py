import flet as ft
from flet_route import Params, Basket

from events import close_click, change_theme
from models import Museum

def indexView(page: ft.Page, params: Params, basket: Basket):
    museums = Museum.select()
    print(museums)
    return ft.View(
        "/",
        [
            ft.AppBar(
                leading=ft.Icon(ft.icons.MUSEUM),
                leading_width=40,
                title=ft.Text("Музеи"),
                center_title=False,
                bgcolor=ft.colors.SURFACE_VARIANT,
                actions=[
                    ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, on_click=change_theme),
                    ft.PopupMenuButton(
                        items=[
                            ft.PopupMenuItem(
                                text="Выйти", on_click=close_click
                            ),
                        ]
                    ),
                ],
            ),
            ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Image(
                                    height=80,
                                    width=80,
                                    src=item.image,
                                    fit=ft.ImageFit.CONTAIN,
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Text(item.title),
                                        ft.ElevatedButton('Смотреть подробнее', on_click=lambda _, item_id=item.id: page.go(f"/mus/{item_id}")),
                                    ],
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                    ) for item in museums
                ],
            ),
        ],
        scroll=ft.ScrollMode.ALWAYS,
    )


def museumInfoView(page: ft.Page, params: Params, basket: Basket):
    id = int(params.get('id'))
    museum = Museum.get_by_id(id)
    return ft.View(
        "/mus/:id",
        controls=[
            ft.AppBar(
                leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: page.go("/")),
                leading_width=40,
                title=ft.Text(museum.title),
                center_title=False,
                bgcolor=ft.colors.SURFACE_VARIANT,
                actions=[
                    ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, on_click=change_theme),
                    ft.PopupMenuButton(
                        items=[
                            ft.PopupMenuItem(
                                text="Выйти", on_click=close_click
                            ),
                        ]
                    ),
                ],
            ),
            ft.Column(
                controls=[
                    ft.Text(museum.title),
                    ft.Image(
                        height=300,
                        width=300,
                        src=museum.image,
                        fit=ft.ImageFit.FIT_WIDTH
                    ),
                    ft.Text(museum.description),
                ],
            ),
            ft.Column(
                controls=[
                    ft.Text(museum.contacts),
                    ft.Text(museum.address),
                    ft.Text(museum.work_time),
                    ft.Text(museum.website),

                ],
            ),
            ft.ElevatedButton("Назад", on_click=lambda _: page.go("/")),
        ],
        scroll=ft.ScrollMode.ALWAYS
    )
