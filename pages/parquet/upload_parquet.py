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
    @ui.page('/media')
    def media_page() -> None:        
        # ui.label('CONTENT')
        folders = VideoApi.get_folders()
        # with ui.row():
        with theme.frame("Videos and images"):
            with ui.row().classes('absolute-center'):
                for folder in folders:
                    ui.link(f"Open {folder}", f"/videos/?folder_name={folder}")
