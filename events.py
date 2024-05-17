def close_click(e):
    e.page.window_close()


def change_theme(e):
    e.page.theme_mode = 'light' if e.page.theme_mode == 'dark' else 'dark'
    e.page.update()
def carts(e):
    pass