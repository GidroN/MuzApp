from flet_core import ListView
import flet as ft
from  routesevents import ROUTES
# from flet_map import FletMap



def close_click(e):
    e.page.window_close()


def change_theme(e):
    e.page.theme_mode = 'light' if e.page.theme_mode == 'dark' else 'dark'
    e.page.update()


def show_drawer(e):
    e.page.views[0].drawer = e.page.drawer
    e.page.update()
    e.page.views[0].drawer.open = True
    e.page.views[0].drawer.update()


def change_route(e):
    route = ROUTES[e.control.selected_index]
    e.page.go(route)
    print(route)

# def appbar(e, text):
#    return ft.AppBar(
#         leading=ft.IconButton(ft.icons.MUSEUM, on_click=show_drawer),
#         leading_width=40,
#         title=ft.Text(text),
#         center_title=False,
#         bgcolor=ft.colors.SURFACE_VARIANT, actions=[
#             ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, on_click=change_theme),
#             ft.PopupMenuButton(
#                 items=[
#                     ft.PopupMenuItem(
#                         "Настройки", on_click=lambda _: e.page.go('/settings/')
#                     ),
#                     ft.PopupMenuItem(
#                         text="Поддержка", on_click=...
#                     ),
#                     ft.PopupMenuItem(
#                         text="Выйти", on_click=close_click
#                     ),
#                 ]
#             ),
#         ],
#     ),