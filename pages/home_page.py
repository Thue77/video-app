#!/usr/bin/env python3
from fastapi import FastAPI
from nicegui import ui,app
from pathlib import Path
import sys

src = Path(__file__).parent.parent
sys.path.append(src)

from design import theme


def content() -> None:
    ui.label('This is the home page.').classes('text-h4 font-bold text-grey-8')

# here we use our custom page decorator directly and just put the content creation into a separate function
def init(app: FastAPI) -> None:
    @ui.page('/')
    def index_page() -> None:
        with theme.frame('Homepage'):
            content()
    ui.run_with(app=app)
