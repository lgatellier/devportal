from devportal.core import api, templates
from fastapi import Request
from fastapi.responses import HTMLResponse

from devportal.core.models.app import ApplicationQuery


@api.get("/ui/apps", response_class=HTMLResponse)
async def page_apps(request: Request):
    return templates.TemplateResponse(request=request, name="pages/applications.html")


@api.get("/ui/content/apps", response_class=HTMLResponse)
async def content_apps(request: Request):
    apps_list = ApplicationQuery.list()
    return templates.TemplateResponse(
        request=request,
        name="content/applications.html",
        context={"applications": apps_list},
    )


@api.get("/ui/partial/app/new", response_class=HTMLResponse)
async def new_app_modal(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="partial/app/new.html",
    )
