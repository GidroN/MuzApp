import flet as ft
from flet_route import Params, Basket
from models import Museum


def indexView(page: ft.Page, params: Params, basket: Basket):

    museums = Museum.select()

    return ft.View(
        "/",
        [
            ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    content=ft.Image(
                                        height=300,
                                        width=300,
                                        src=item.image,
                                        fit=ft.ImageFit.CONTAIN,
                                    )
                                ),
                                ft.Text(item.title),
                                ft.ElevatedButton('Смотреть подробнее', on_click=lambda _: page.go(f"/mus/{item.id}")),
                            ],
                        ),
                    ) for item in museums
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
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
            ft.Column(
                controls=[
                    ft.Text(museum.title),
                    ft.Image(
                        height=400,
                        width=400,
                        src=museum.image,
                        fit=ft.ImageFit.FIT_WIDTH
                    ),
                    ft.Text(museum.description)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            ft.ElevatedButton("Назад", on_click=lambda _: page.go("/")),
        ],
        scroll=ft.ScrollMode.ALWAYS
    )
