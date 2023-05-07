import requests
from urllib.parse import unquote, quote
import logging

from nicegui import ui, app
from nicegui.events import KeyEventArguments
from fastapi import FastAPI

from pathlib import Path
import sys
src = Path(__file__).parent.parent
sys.path.append(str(src))

from design import theme
from services import video_api

VideoApi = video_api.VideoApi()

def init(app: FastAPI) -> None:
    @ui.page('/pictures')
    def picture_page() -> None:        
        with theme.frame('- Example A -'):
            ui.label("Swimming").classes('text-h4 text-grey-8')
            with ui.row():
                title = ui.input(label="video title", placeholder="swim.mp4")
                logging.info(f"INPUT: {title}")
                videos = [video["name"] for video in VideoApi.get_blob_list("video")]

                choice = ui.select(videos,value=videos[0])
                ui.button("Watch",on_click=lambda _: ui.open(VideoApi.get_blob(title=choice.value)))
                


