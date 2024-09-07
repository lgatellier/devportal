from fastapi import Request
from fastapi.responses import HTMLResponse

from appatlas.core.ui import ui_app, templates
from appatlas.core.models.app import ApplicationBase, ApplicationQuery


@ui_app.get("/partial/app/new", response_class=HTMLResponse)
async def new_app_modal(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="partial/app/new.html",
    )


@ui_app.post("/app", response_class=HTMLResponse, status_code=201)
async def create_application(request: Request, app: ApplicationBase):
    ApplicationQuery.create(app)
    return templates.TemplateResponse(
        request=request,
        name="partial/app/alert.html",
        context={"app": app, "message": "apps.alert.new.success", "level": "success"},
    )
