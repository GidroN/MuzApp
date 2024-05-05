import flet as ft
from flet_route import Params, Basket

imgings = [
    'https://upload.wikimedia.org/wikipedia/commons/a/ad/Dom_Goncharov1.jpg',
    'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/18/42/1a/16/caption.jpg?w=1400&h=-1&s=1'
]
muz = ['Ульяновский областной краеведческий музей им. И.А. Гончарова',
       'Дом-музей В.И. Ленина']


def indexView(page: ft.Page, params: Params, basket: Basket):
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
                                        src=imgings[i - 1],
                                        fit=ft.ImageFit.CONTAIN,
                                    )
                                ),
                                ft.Text(muz[i - 1]),
                                ft.ElevatedButton('Смотреть подробнее', on_click=lambda _: page.go(f"/mus/{i}")),
                            ],
                        ),
                    ) for i in range(2)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
        ],
        scroll=ft.ScrollMode.ALWAYS,
    )


def museumInfoView(page: ft.Page, params: Params, basket: Basket):
    id = int(params.get('id'))
    return ft.View(
        "/mus/:id",
        controls=[
            ft.Column(
                controls=[
                    ft.Text(f"{muz[id - 1]}"),
                    ft.Image(
                        height=400,
                        width=400,
                        src=imgings[id - 1],
                        fit=ft.ImageFit.FIT_WIDTH
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            ft.ElevatedButton("Назад", on_click=lambda _: page.go("/")),
        ],
        scroll=ft.ScrollMode.ALWAYS
    )
