from nicegui import ui

from devportal.ui.pages import home, view_app

for page in [home, view_app]:
    page.load()

ui.run()
