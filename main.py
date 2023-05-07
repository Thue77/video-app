#!/usr/bin/env python3
from fastapi import FastAPI
from nicegui import ui
from pathlib import Path
import sys

src = Path(__file__).parent
sys.path.append(str(src))

import pages.home_page as home_page
from design import theme
from pages import home_page, pictures

app = FastAPI()

home_page.init(app)
pictures.init(app)

if __name__ == "__main__":
    print("Please run startup.sh")
