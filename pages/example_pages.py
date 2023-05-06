from pathlib import Path
import theme

from nicegui import ui, app
from nicegui.events import KeyEventArguments

# folder = Path(__file__).resolve().parent / 'slides'  # image source: https://pixabay.com/
# files = sorted(f.name for f in folder.glob('*.jpg'))
# index = 0

# slide = ui.image(f'slides/{files[index]}')  # show the first image

# def handle_key(event: KeyEventArguments) -> None:
#     global index
#     if event.action.keydown:
#         if event.key.arrow_right:
#             index += 1
#         if event.key.arrow_left:
#             index -= 1
#         index = index % len(files)
#         slide.set_source(f'slides/{files[index]}')


def create() -> None:

    @ui.page('/a')
    def example_page():
        # app.add_static_files('/slides', folder)  # serve all files in this folder     
        with theme.frame('- Example A -'):
            ui.label('Example A').classes('text-h4 text-grey-8')
            # ui.keyboard(on_key=handle_key)  # handle keyboard events

    @ui.page('/b')
    def example_page():
        with theme.frame('- Example B -'):
            ui.label('Example B').classes('text-h4 text-grey-8')

    @ui.page('/c')
    def example_page():
        with theme.frame('- Example C -'):
            ui.label('Example C').classes('text-h4 text-grey-8')