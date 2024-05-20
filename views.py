import flet as ft
from flet_route import Params, Basket

from events import close_click, change_theme, show_drawer, change_route
from models import Museum




def indexView(page: ft.Page, params: Params, basket: Basket):
    museums = Museum.select()
    page.drawer = ft.NavigationDrawer(
        selected_index=-1,
        on_change=change_route,
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="О приложении",
                icon=ft.icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.DOOR_BACK_DOOR),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.MAIL_OUTLINED),
                label="О городе",
                selected_icon=ft.icons.MAIL,
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.PHONE_OUTLINED),
                label="События",
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
                                "Настройки", on_click=lambda _:page.go('/settings/')
                            ),
                            ft.PopupMenuItem(
                                text="Поддержка", on_click=...
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
                                text="Настройки", on_click=lambda _:page.go('/settings/')
                            ),
                            ft.PopupMenuItem(
                                text="Поддержка", on_click=...
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
                    #ft.IconButton(ft.icons.MAP, on_click=map),

                ],

            ),
            ft.ElevatedButton("Назад", on_click=lambda _: page.go("/")),
        ],
        scroll=ft.ScrollMode.ALWAYS
    )


def aboutAppView(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        '/about_app/',
        [
            ft.AppBar(
                leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: page.go("/")),
                leading_width=40,
                title=ft.Text('О приложении'),
                center_title=False,
                bgcolor=ft.colors.SURFACE_VARIANT,
                actions=[
                    ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, on_click=change_theme),
                    ft.PopupMenuButton(
                        items=[
                            ft.PopupMenuItem(
                                text="Настройки", on_click=lambda _:page.go('/settings/')
                            ),
                            ft.PopupMenuItem(
                                text="Поддержка", on_click=...
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
                    ft.Text(
                        'Разрабатываемое мобильное приложение "Музеи Ульяновской области" предназначено для популяризации '
                        'культурного наследия региона и улучшения взаимодействия посетителей с музеями.'
                        ' Приложение предоставляет пользователям удобный доступ к информации о музеях, событиях и выставках,'
                        ' а также предлагает ряд полезных функций для планирования и организации посещений.'
                    )
                ],
            ),
            ft.ElevatedButton("Назад", on_click=lambda _: page.go("/")),
        ],
        scroll=ft.ScrollMode.ALWAYS

    )
def aboutAppCity(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        '/about_city/',
        [
            ft.AppBar(
                leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: page.go("/")),
                leading_width=40,
                title=ft.Text('О городе'),
                center_title=False,
                bgcolor=ft.colors.SURFACE_VARIANT,
                actions=[
                    ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, on_click=change_theme),
                    ft.PopupMenuButton(
                        items=[
                            ft.PopupMenuItem(
                                text="Настройки", on_click=lambda _:page.go('/settings/')
                            ),
                            ft.PopupMenuItem(
                                text="Поддержка", on_click=...
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
                    ft.Image(
                        height=300,
                        width=600,
                        src='img/scale_1200.jpg',
                        fit=ft.ImageFit.FIT_WIDTH
                    ),
                    ft.Text(
                    'Ульяновск – это исторический и культурный центр Ульяновской области,'
                    ' расположенный на берегах реки Волги.'
                    'Город, основанный в 1648 году как крепость Синбирск, '
                    'богат своей многовековой историей и культурными традициями.'
                    'В 1924 году город был переименован в честь Владимира Ленина (Ульянова), который здесь родился.'
                    ),

                ],
            ),
            ft.ElevatedButton("Назад", on_click=lambda _: page.go("/")),
        ],
        scroll=ft.ScrollMode.ALWAYS

    )
def settings(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        '/settings/',
        [
            ft.AppBar(
                leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: page.go("/")),
                leading_width=40,
                title=ft.Text('Настройки'),
                center_title=False,
                bgcolor=ft.colors.SURFACE_VARIANT,
                actions=[
                    ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, on_click=change_theme),
                    ft.PopupMenuButton(
                        items=[
                            ft.PopupMenuItem(
                                text="Настройки", on_click=lambda _:page.go('/settings/')
                            ),
                            ft.PopupMenuItem(
                                text="Поддержка", on_click=...
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

                ],
            ),
            ft.ElevatedButton("Назад", on_click=lambda _: page.go("/")),
        ],
        scroll=ft.ScrollMode.ALWAYS

    )