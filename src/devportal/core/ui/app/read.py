from fastapi import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from uuid import UUID

from devportal.core.models.app import ApplicationQuery
from devportal.core import api, templates
from devportal.vms import main as vms
from devportal.dbs import main as dbs


@api.get("/ui/app/{id}", response_class=RedirectResponse, status_code=301)
async def get_application_root(id: UUID):
    return f"/ui/app/{id}/about"


@api.get("/ui/app/{id}/{partial}", response_class=HTMLResponse)
async def get_application_partial(request: Request, id: UUID, partial: str = "about"):
    app = ApplicationQuery.get(id)
    return templates.TemplateResponse(
        request=request,
        name="pages/single_application.html",
        context={"app": app, "active": partial},
    )


@api.get("/ui/content/app/{id}", response_class=RedirectResponse, status_code=301)
async def get_application_content_root(id: UUID):
    return f"/ui/content/app/{id}/about"


@api.get("/ui/content/app/{id}/{partial}", response_class=HTMLResponse)
async def get_application_content_partial(request: Request, id: UUID, partial: str):
    app = ApplicationQuery.get(id)
    return templates.TemplateResponse(
        request=request,
        name="content/single_application.html",
        context={"app": app, "active": partial},
    )


@api.get("/ui/partial/app/{id}/about", response_class=HTMLResponse)
async def get_application_partial_about(request: Request, id: UUID):
    app = ApplicationQuery.get(id)
    return templates.TemplateResponse(
        request=request, name="partial/app/about.html", context={"app": app}
    )


@api.get("/ui/partial/app/{app_code}/servers", response_class=HTMLResponse)
async def get_application_partial_servers(request: Request, app_code: str):
    servers = vms.list_vms(app_code)
    return templates.TemplateResponse(
        request=request,
        name="partial/app/servers.html",
        context={"app": {"code": app_code}, "servers": servers},
    )


@api.get("/ui/partial/app/{app_code}/databases", response_class=HTMLResponse)
async def get_application_partial_databases(request: Request, app_code: str):
    db_list = dbs.list_dbs(app_code)
    return templates.TemplateResponse(
        request=request,
        name="partial/app/databases.html",
        context={"app": {"code": app_code}, "databases": db_list},
    )
