from fastapi import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from uuid import UUID

from appatlas.core.models.app import ApplicationQuery
from appatlas.core.ui import ui_app, templates
from appatlas.vms import main as vms
from appatlas.dbs import main as dbs


@ui_app.get("/app/{id}", response_class=RedirectResponse, status_code=301)
async def get_application_root(id: UUID):
    return f"/ui/app/{id}/about"


@ui_app.get("/app/{id}/{partial}", response_class=HTMLResponse)
async def get_application_partial(request: Request, id: UUID, partial: str = "about"):
    app = ApplicationQuery.get(id)
    return templates.TemplateResponse(
        request=request,
        name="pages/single_application.html",
        context={"app": app, "active": partial},
    )


@ui_app.get("/content/app/{id}", response_class=RedirectResponse, status_code=301)
async def get_application_content_root(id: UUID):
    return f"/ui/content/app/{id}/about"


@ui_app.get("/content/app/{id}/{partial}", response_class=HTMLResponse)
async def get_application_content_partial(request: Request, id: UUID, partial: str):
    app = ApplicationQuery.get(id)
    return templates.TemplateResponse(
        request=request,
        name="content/single_application.html",
        context={"app": app, "active": partial},
    )


@ui_app.get("/partial/app/{id}/about", response_class=HTMLResponse)
async def get_application_partial_about(request: Request, id: UUID):
    app = ApplicationQuery.get(id)
    return templates.TemplateResponse(
        request=request, name="partial/app/about.html", context={"app": app}
    )


@ui_app.get("/partial/app/{app_code}/servers", response_class=HTMLResponse)
async def get_application_partial_servers(request: Request, app_code: str):
    servers = vms.list_vms(app_code)
    return templates.TemplateResponse(
        request=request,
        name="partial/app/servers.html",
        context={"app": {"code": app_code}, "servers": servers},
    )


@ui_app.get("/partial/app/{app_code}/databases", response_class=HTMLResponse)
async def get_application_partial_databases(request: Request, app_code: str):
    db_list = dbs.list_dbs(app_code)
    return templates.TemplateResponse(
        request=request,
        name="partial/app/databases.html",
        context={"app": {"code": app_code}, "databases": db_list},
    )
