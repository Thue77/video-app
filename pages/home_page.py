#!/usr/bin/env python3
from fastapi import FastAPI
from nicegui import ui
import nicegui
from pathlib import Path
import sys

src = Path(__file__).parent.parent
sys.path.append(src)

from design import theme


def content() -> None:
    ui.icon('home',size='128px')
    # ui.label('This is the home page.').classes('text-h4 font-bold text-grey-8')

# here we use our custom page decorato/r directly and just put the content creation into a separate function
def init(app: FastAPI) -> None:
    @ui.page('/')
    def index_page() -> None:
        with theme.frame('Homepage'):
            with ui.row().classes('absolute-center'):
                content()
    ui.run_with(app=app,favicon=str(Path(__file__).parent.parent / 'website' / 'icons' / 'favicon.ico'),title="Sørensen Video")
