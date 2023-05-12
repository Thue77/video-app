#!/usr/bin/env python3
from fastapi import FastAPI
from nicegui import ui
import nicegui
from pathlib import Path
import sys

src = Path(__file__).parent
sys.path.append(str(src))

from design import theme
from pages import home_page, media, videos

app = FastAPI(title="My Title")

nicegui.app.add_static_files('/icons',str(Path(__file__).parent / 'website' / 'icons'))

home_page.init(app)
videos.init(app)
media.init(app)

if __name__ == "__main__":
    print("Please run startup.sh")
