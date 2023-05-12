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
    def video_page(folder_name: str, subfolders: str = "") -> None:        
        logging.info(f"Showing videos from folder {folder_name}")
        content = VideoApi.get_content(folder_name, prefix=subfolders)
        with ui.row().classes('absolute-center'):
            images = [ui.image(VideoApi.get_blob(title=image["name"],folder=folder_name)) for image in content["images"]]
            videos = [ui.video(VideoApi.get_blob(title=video["name"],folder=folder_name)) for video in content["videos"]]
        with theme.frame('Videos'):
            with ui.left_drawer(top_corner=True, bottom_corner=True).style('background-color: #d7e3f4'):
                ui.label('Folders')
                with ui.column():
                    [ui.link(f"Open {folder['name'].rsplit('/',2)[-2]}", f"/videos/?folder_name={folder_name}&subfolders={folder['name']}") for folder in content["folders"]]
        
                


