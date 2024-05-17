import flet as ft
from flet_route import Routing
from routes import app_routes
from models import *


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_resizable = True
    Routing(
        page=page,
        app_routes=app_routes,
    )
    page.go(page.route)
    page.update()



if __name__ == '__main__':
    try:
        db.connect()
        db.create_tables([Museum])
        ft.app(target=main)
    except KeyboardInterrupt:
        db.close()
