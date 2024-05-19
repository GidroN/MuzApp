import flet as ft
from flet_route import Params, Basket

from events import close_click, change_theme, show_drawer
from models import Museum


def indexView(page: ft.Page, params: Params, basket: Basket):
    museums = Museum.select()

    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Item 1",
                icon=ft.icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.DOOR_BACK_DOOR),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.MAIL_OUTLINED),
                label="Item 2",
                selected_icon=ft.icons.MAIL,
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.PHONE_OUTLINED),
                label="Item 3",
                selected_icon=ft.icons.PHONE,
            ),
        ],
    )

    return ft.View(
        "/",
        [
            ft.AppBar(
                leading=ft.IconButton(ft.icons.MUSEUM, on_click=show_drawer),
                leading_width=40,
                title=ft.Text("Музеи"),
                center_title=False,
                bgcolor=ft.colors.SURFACE_VARIANT,
                actions=[
                    ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, on_click=change_theme),
                    ft.PopupMenuButton(
                        items=[
                            ft.PopupMenuItem(
                                text="о приложении", on_click=...
                            ),
                            ft.PopupMenuItem(
                                text="о городе", on_click=...
                            ),
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
                                        ft.ElevatedButton('Смотреть подробнее',
                                                          on_click=lambda _, item_id=item.id: page.go(
                                                              f"/mus/{item_id}")),
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
                                text="о приложении", on_click=...
                            ),
                            ft.PopupMenuItem(
                                text="о городе", on_click=...
                            ),
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
                    ft.IconButton(ft.icons.MAP, on_click=map),

                ],

            ),
            ft.ElevatedButton("Назад", on_click=lambda _: page.go("/")),
        ],
        scroll=ft.ScrollMode.ALWAYS
    )
# testtt2
