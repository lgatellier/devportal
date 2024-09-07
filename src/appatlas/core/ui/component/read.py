from uuid import UUID
from appatlas.core.ui import ui_app, templates
from fastapi import Request
from fastapi.responses import HTMLResponse, RedirectResponse

from appatlas.core.models.app import ComponentQuery


@ui_app.get("/component/{id}", response_class=RedirectResponse, status_code=301)
async def get_component_root(id: str):
    return f"/ui/component/{id}/about"


@ui_app.get("/component/{id}/{partial}", response_class=HTMLResponse)
async def get_component_partial(request: Request, id: UUID, partial: str = "about"):
    component = ComponentQuery.get(id)
    return templates.TemplateResponse(
        request=request,
        name="pages/component.html",
        context={"component": component, "active": partial},
    )


@ui_app.get("/content/component/{id}", response_class=RedirectResponse, status_code=301)
async def get_component_content_root(id: UUID):
    return f"/ui/content/component/{id}/about"


@ui_app.get("/content/component/{id}/{partial}", response_class=HTMLResponse)
async def get_component(request: Request, id: UUID, partial: str = "about"):
    query_result = ComponentQuery.get(id)
    return templates.TemplateResponse(
        request=request,
        name="content/component.html",
        context={"component": query_result, "active": partial},
    )


@ui_app.get("/partial/component/{id}/about", response_class=HTMLResponse)
async def get_component_partial_about(request: Request, id: UUID):
    component = ComponentQuery.get(id)
    return templates.TemplateResponse(
        request=request,
        name="partial/component/about.html",
        context={"component": component},
    )
