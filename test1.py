import flet as ft


def main(page: ft.Page):
    def show_drawer(e):
        page.drawer.open = True
        page.drawer.update()

    page.add(
        ft.AppBar(
            leading=ft.IconButton(ft.icons.MUSEUM, on_click=show_drawer),
            leading_width=40,
            title=ft.Text("Музеи"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, on_click=...),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(
                            text="о приложении", on_click=...
                        ),
                        ft.PopupMenuItem(
                        text="о городе", on_click=...
                        ),
                        ft.PopupMenuItem(
                        text="Выйти", on_click=...
                        ),
                    ]
                ),
            ],
        ),
    )
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
    page.update()



    #page.add(ft.ElevatedButton("Show drawer", on_click=show_drawer))


ft.app(main)