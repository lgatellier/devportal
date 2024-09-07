from fastapi import Request
from fastapi.responses import HTMLResponse

from appatlas.core import api, templates
from appatlas.core.models.app import ApplicationBase, ApplicationQuery


@api.post("/ui/app", response_class=HTMLResponse, status_code=201)
async def create_application(request: Request, app: ApplicationBase):
    ApplicationQuery.create(app)
    return templates.TemplateResponse(
        request=request,
        name="partial/app/alert.html",
        context={"app": app, "message": "apps.alert.new.success", "level": "success"},
    )
