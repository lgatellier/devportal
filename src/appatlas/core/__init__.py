from fastapi import FastAPI
from fastapi.responses import RedirectResponse


fastapi_app = FastAPI()


@fastapi_app.get("/", response_class=RedirectResponse, status_code=301)
async def server_root():
    return "/ui"


__all__ = ["fastapi_app", "templates"]
