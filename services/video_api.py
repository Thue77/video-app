import requests
from typing import List

from pathlib import Path
import sys
src = Path(__file__).parent.parent
sys.path.append(str(src))

import services.secrets as secrets

class VideoApi:
    def __init__(self) -> None:
        self.base_url = secrets.config("VIDEOAPI_URL")
        self.code = secrets.config("VIDEOAPI_KEY", default="anonymous")

    def set_api_url(self, path_parameter: str, query_parameters: dict = {}) -> str:
        # collect query parameters in list
        query_list = [f"{name}={value}" for name,value in query_parameters.items()]
        # format for url
        query_string = "&".join(query_list)
        # collect url
        return self.base_url + path_parameter + f"?code={self.code}&" + query_string
         

    def get_blob(self, title: str, folder: str = "video"):
        response = requests.get(url=self.set_api_url("item/"+folder, query_parameters= {"video_name":title}))
        return response.json()["url"]

    def get_blob_list(self, folder: str):
        response = requests.get(url=self.set_api_url("item/"+folder+"/"))
        return response.json()["videos"]
