import json
from nicegui import ui

from devportal.ui import theme
from devportal.apps import main


def load():
    @ui.page("/")
    def render():
        with theme.page("My applications"):
            content()


def content():
    COLUMNS = [
        {"name": "code", "label": "App code", "field": "code", "align": "center"},
        {"name": "name", "label": "App name", "field": "name", "align": "left"},
        {"name": "tags", "label": "Tags", "field": "display_tags", "align": "left"},
    ]
    apps = main.list_apps()
    table = ui.table(
        columns=COLUMNS, rows=apps, row_key="code"
    ).classes("w-full")
    table.on("rowClick", lambda e: ui.navigate.to(f"/app/{e.args[1]['code']}"))
