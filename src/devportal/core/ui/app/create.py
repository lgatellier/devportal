from fastapi import Request
from fastapi.responses import HTMLResponse

from devportal.apps import main as apps
from devportal.core import api, templates
from devportal.core.model import ApplicationBase


@api.post("/ui/app", response_class=HTMLResponse, status_code=201)
async def create_application(request: Request, app: ApplicationBase):
    apps.create_app(app)
    return templates.TemplateResponse(
        request=request,
        name="partial/app/alert.html",
        context={"app": app, "message": "apps.alert.new.success", "level": "success"},
    )
