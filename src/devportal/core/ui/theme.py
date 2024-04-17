from contextlib import contextmanager
from nicegui import ui


@contextmanager
def page(page_title):
    with ui.header():
        with ui.row().classes("container mx-auto"):
            ui.html('<h1 class="text-4xl font-bold">Portal</h1>').classes(
                "cursor-pointer"
            ).on("click", lambda e: ui.navigate.to("/"))

    with ui.row().classes("container mx-auto"):
        ui.markdown(f"## {page_title}").classes("capitalize text-4xl font-bold")

    with ui.row().classes("container mx-auto"):
        yield
