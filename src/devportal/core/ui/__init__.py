from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from devportal.core.app import app
from devportal.core.ui.pages import home, view_app  # noqa: F401


@app.get("/", response_class=RedirectResponse, status_code=301)
async def server_root():
    return "/ui/apps"


@app.get("/ui", response_class=RedirectResponse, status_code=301)
async def ui_root():
    return "/ui/apps"


app.mount("/static", StaticFiles(directory="src/static"), name="static")
