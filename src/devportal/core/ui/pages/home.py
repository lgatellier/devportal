from devportal.core.app import app, templates
from fastapi import Request
from fastapi.responses import HTMLResponse


@app.get("/ui/apps", response_class=HTMLResponse)
async def page_apps(request: Request):
    return templates.TemplateResponse(request=request, name="pages/applications.html")


@app.get("/ui/content/apps", response_class=HTMLResponse)
async def content_apps(request: Request):
    from devportal.apps import main

    apps_list = main.list_apps()
    return templates.TemplateResponse(
        request=request,
        name="content/applications.html",
        context={"applications": apps_list},
    )


@app.get("/ui/partial/app/new", response_class=HTMLResponse)
async def new_app_modal(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="partial/app/new.html",
    )
