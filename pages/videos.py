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
    @ui.page('/videos/')
    def video_page(folder_name: str) -> None:        
        logging.info(f"Showing videos from folder {folder_name}")
        with theme.frame('Videos'):
            videos = [ui.video(VideoApi.get_blob(title=video["name"],folder=folder_name)) for video in VideoApi.get_blob_list(folder_name)]
                


