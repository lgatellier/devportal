from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from appatlas.core import api
from appatlas.core.ui import app, component  # noqa: F401


@api.get("/", response_class=RedirectResponse, status_code=301)
async def server_root():
    return "/ui/apps"


@api.get("/ui", response_class=RedirectResponse, status_code=301)
async def ui_root():
    return "/ui/apps"


api.mount("/static", StaticFiles(directory="src/static"), name="static")
