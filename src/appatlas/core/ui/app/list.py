from appatlas.core.ui import ui_app, templates
from fastapi import Request
from fastapi.responses import HTMLResponse

from appatlas.core.models.app import ApplicationQuery


@ui_app.get("/apps", response_class=HTMLResponse)
async def page_apps(request: Request):
    return templates.TemplateResponse(request=request, name="pages/applications.html")


@ui_app.get("/content/apps", response_class=HTMLResponse)
async def content_apps(request: Request):
    apps_list = ApplicationQuery.list_all()
    return templates.TemplateResponse(
        request=request,
        name="content/applications.html",
        context={"applications": apps_list},
    )


@ui_app.get("/partial/app/new", response_class=HTMLResponse)
async def new_app_modal(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="partial/app/new.html",
    )
