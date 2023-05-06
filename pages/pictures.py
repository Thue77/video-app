from pathlib import Path
import theme

from nicegui import ui, app
from nicegui.events import KeyEventArguments

folder = Path(__file__).resolve().parent.parent / 'slides'  # image source: https://pixabay.com/
files = sorted(f.name for f in folder.glob('*.jpg'))
blob_file = "http://127.0.0.1:10000/devstoreaccount1/images/slide1.jpg?sv=2018-03-28&st=2023-05-05T07%3A36%3A06Z&se=2023-05-06T07%3A36%3A06Z&sr=b&sp=r&sig=qRJWzTSGjHaQOb%2Fotp%2Bl9BlSezP%2BwK8I7puCA2f1Nuc%3D"
blob_video = "http://127.0.0.1:10000/devstoreaccount1/video/swim.mp4?sv=2018-03-28&st=2023-05-05T08%3A05%3A13Z&se=2023-05-06T08%3A05%3A13Z&sr=b&sp=r&sig=44FH1b41khQHrh7yy4xfMxhezAjGbzNp4VgdgEmAAnE%3D"
index = 0



@ui.page('/pictures')
def picture_page():
    # app.add_static_files('/picture', folder)  # serve all files in this folder

    with theme.frame('- Example A -'):
        ui.label('Example A').classes('text-h4 text-grey-8')
        ui.image(blob_file)
        ui.video(blob_video)
        # ui.video
        # with ui.row():
            # ui.image(f'slides/{files[0]}')  # show the first image
            # ui.image(f'slides/{files[0]}')  # show the first image
            


