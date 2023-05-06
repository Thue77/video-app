from contextlib import contextmanager
from nicegui import ui

from pathlib import Path
import sys

src = Path(__file__).parent.parent
sys.path.append(src)

from design.menu import menu



@contextmanager
def frame(navtitle: str):
    '''Custom page frame to share the same styling and behavior across all pages'''
    ui.colors(primary='#6E93D6', secondary='#53B689', accent='#111B1E', positive='#53B689')
    with ui.header().classes('justify-between text-white'):
        ui.label('Modularization Example').classes('font-bold')
        ui.label(navtitle)
        with ui.row():
            menu()
    with ui.row().classes('absolute-center'):
        yield