#!/usr/bin/env python3
from fastapi import FastAPI
import nicegui
from pathlib import Path
import sys
import logging

src = Path(__file__).parent
sys.path.append(str(src))

from design import theme
from pages import home_page
from pages.video import media, videos
from pages.parquet import parquet

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

app = FastAPI(title="My Title")

nicegui.app.add_static_files('/icons',str(Path(__file__).parent / 'website' / 'icons'))

logger.info("Starting app")
home_page.init(app)
logger.info("Home page initialized")
videos.init(app)
logger.info("Videos page initialized")
media.init(app)
logger.info("Media page initialized")
# TODO: Make parquet page generic to support other file formats. Requires small refactoring
parquet.init(app)
logger.info("Parquet page initialized")

if __name__ == "__main__":
    print("Please run startup.sh")
