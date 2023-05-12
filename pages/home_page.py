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
        # ui.header()
        # ui.add_head_html((Path(__file__).parent.parent / 'website' / 'header.html').read_text())
        # ui.html('<link rel="icon" href="i/favicon.ico">')
        # ui.html('<link rel="apple-touch-icon" sizes="180x180" href="/icons/apple-touch-icon.png">')
        # ui.html('<link rel="icon" type="image/png" sizes="32x32" href="/icons/favicon-32x32.png">')
        # ui.html('<link rel="icon" type="image/png" sizes="16x16" href="/icons/favicon-16x16.png">')
        # ui.html('<link rel="manifest" href="/icons/site.webmanifest">')
        # ui.html('<meta name="msapplication-TileColor" content="#da532c">')
        # ui.html('<meta name="msapplication-config" content="/icons/browserconfig.xml">')
        # ui.html('<meta name="theme-color" content="#ffffff">')
        with theme.frame('Homepage'):
            with ui.row().classes('absolute-center'):
                content()
    ui.run_with(app=app,favicon=str(Path(__file__).parent.parent / 'website' / 'icons' / 'favicon.ico'),title="Sørensen Video")
