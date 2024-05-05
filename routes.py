from flet_route import path
from views import indexView
from views import museumInfoView

app_routes = [
    path(url="/", clear=True, view=indexView),
    path(url="/mus/:id", clear=False, view=museumInfoView),
]

