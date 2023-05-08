from nicegui import ui


def menu() -> None:
    ui.link('Home', '/').classes(replace='text-white')
    ui.link('Folders', '/folders').classes(replace='text-white')
    # ui.link('A', '/a').classes(replace='text-white')
    # ui.link('B', '/b').classes(replace='text-white')
    # ui.link('Slides', '/slides').classes(replace='text-white')