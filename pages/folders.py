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

def open_folder(folder: str):
    ui.open(f"/videos/?folder_name={folder}")

def init(app: FastAPI) -> None:
    @ui.page('/folders')
    def folder_page() -> None:        
        ui.label('CONTENT')
        folders = VideoApi.get_folders()
        with ui.row():
            for folder in folders:
                ui.link(f"Open {folder}", f"/videos/?folder_name={folder}")
        with theme.frame("Folders"):
            with ui.left_drawer(top_corner=True, bottom_corner=True).style('background-color: #d7e3f4'):
                ui.label('LEFT DRAWER')
