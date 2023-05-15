import requests
from urllib.parse import unquote, quote
import logging
import pyarrow.parquet as pq
import pyarrow as pa
from nicegui import ui, app, events
from nicegui.events import KeyEventArguments
from fastapi import FastAPI


from pathlib import Path
import sys
src = Path(__file__).parent.parent
sys.path.append(str(src))

from design import theme
from utility import parquet_operations

logger =logging.getLogger(__name__)

df = None

def init(app: FastAPI) -> None:

    @ui.page('/parquet')
    def parquet_page() -> None:        
        with theme.frame("Upload Parquet file"):
            with ui.row():
                ui.label('Here the info about the parquet file will be dsiplayed')
            ui.upload(on_upload=on_upload_parquet_file,on_rejected=lambda: ui.notify('Rejected!'),
                            max_file_size=100_000_000) 
            
                   
            
    # Function to upload parquet file
    def on_upload_parquet_file(file: events.UploadEventArguments) -> None:
        logger.info(f'Uploading parquet file {file}')
        ui.notify(f'Uploading parquet file {file.name}')
        global df
        df = parquet_operations.ParquetOperations(pq.read_table(file.content))
        ui.open('/parquet-table')

    @ui.page('/parquet-table')
    def parquet_table_page() -> None:
        with theme.frame("Info about Parquet file"):
            try:
                with ui.left_drawer(top_corner=True, bottom_corner=True).style('background-color: #d7e3f4'):
                    ui.label(f"Number of columns: {df.num_columns()}")
                    ui.label(f"Number of rows: {df.num_rows()}")
                with ui.row():
                    ui.table(rows = [df.null_counts()], columns=df.table_columns(),title="Null counts")#.classes('max-h-70')
                    non_string_columns = df.numeric_lengths()
                    string_columns = df.string_lengths()
                    schema = df.schema()
                    ui.table(rows = non_string_columns, columns=[{"name": col, "label": col, "field": col} for col in non_string_columns[0].keys()],title="Max/Min Non-string columns")#.classes('max-h-70')
                    ui.table(rows = string_columns, columns=[{"name": col, "label": col, "field": col} for col in string_columns[0].keys()],title="Max/Min lengths string columns")#.classes('max-h-70')
                    ui.table(rows=[{col:str(val) for col,val in zip(schema.names,schema.types)}], columns=[{"name": str(col), "label": str(col), "field": str(col)} for col in schema.names],title="Schema")#.classes('max-h-70')
                with ui.row():
                    ui.table(rows = df.rows(limit=100), columns=df.table_columns(),title="Parquet table")#.classes('max-h-70')

            except AttributeError as e:
                ui.link(text=f'Please upload a parquet file first!',target='/parquet')

