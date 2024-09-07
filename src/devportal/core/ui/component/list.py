from uuid import UUID
from devportal.core import api, templates
from fastapi import Request
from fastapi.responses import HTMLResponse

from devportal.core.models.app import ComponentQuery


@api.get("/ui/partial/components", response_class=HTMLResponse)
async def list_application_components(request: Request, application_id: UUID):
    query_result = ComponentQuery.list(application_id=application_id)
    return templates.TemplateResponse(
        request=request,
        name="partial/component/list.html",
        context={"components": query_result},
    )
