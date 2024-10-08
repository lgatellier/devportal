from uuid import UUID
from appatlas.core.ui import ui_app, templates
from fastapi import Request
from fastapi.responses import HTMLResponse

from appatlas.core.models.app import ComponentQuery


@ui_app.get("/components", response_class=HTMLResponse)
async def page_apps(request: Request):
    return templates.TemplateResponse(request=request, name="pages/components.html")


@ui_app.get("/content/components", response_class=HTMLResponse)
async def content_apps(request: Request):
    query_result = ComponentQuery.list()
    return templates.TemplateResponse(
        request=request,
        name="content/components.html",
        context={"components": query_result},
    )


@ui_app.get("/partial/components", response_class=HTMLResponse)
async def list_application_components(request: Request, application_id: UUID = None):
    if application_id:
        query_result = ComponentQuery.list(application_id=application_id)
        show_application = False
    else:
        query_result = ComponentQuery.list_all()
        show_application = True
    return templates.TemplateResponse(
        request=request,
        name="partial/component/list.html",
        context={"components": query_result, "show_application": show_application},
    )
