#!/usr/bin/env python3
import pages.example_pages as example_pages
import pages.home_page as home_page
import design.theme as theme

# import pages.pictures as pictures
from pages.slides import slide_page
from pages.pictures import picture_page
from nicegui import ui,app


# here we use our custom page decorator directly and just put the content creation into a separate function
@ui.page('/')
def index_page() -> None:
    with theme.frame('Homepage'):
        home_page.content()


# this call shows that you can also move the whole page creation into a separate file
example_pages.create()

ui.run(title='Modularization Example')