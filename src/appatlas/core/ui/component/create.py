from fastapi import Request
from fastapi.responses import HTMLResponse

from appatlas.core.ui import ui_app, templates
from appatlas.core.models.app import ComponentBase, ComponentQuery, Type, TechStackQuery


@ui_app.get("/partial/component/new", response_class=HTMLResponse)
async def new_component_modal(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="partial/component/new.html",
        context={"types": Type, "techstacks": TechStackQuery.list_all()},
    )


@ui_app.post("/component", response_class=HTMLResponse, status_code=201)
async def create_component(request: Request, component: ComponentBase):
    ComponentQuery.create(component)
    return templates.TemplateResponse(
        request=request,
        name="partial/component/alert.html",
        context={
            "component": component,
            "message": "components.alert.new.success",
            "level": "success",
        },
    )
