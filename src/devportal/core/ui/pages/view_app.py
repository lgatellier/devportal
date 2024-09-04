from devportal.apps import main as apps
from devportal.core.app import app, templates
from devportal.vms import main as vms
from devportal.dbs import main as dbs
from fastapi import Request
from fastapi.responses import HTMLResponse, RedirectResponse


@app.get("/ui/app/{app_code}", response_class=RedirectResponse, status_code=301)
async def get_application_root(app_code: str):
    return f"/ui/app/{app_code}/about"


@app.get("/ui/app/{app_code}/{partial}", response_class=HTMLResponse)
async def get_application_partial(
    request: Request, app_code: str, partial: str = "about"
):
    app = apps.get_app(app_code)
    return templates.TemplateResponse(
        request=request,
        name="pages/single_application.html",
        context={"app": app, "active": partial},
    )


@app.get("/ui/content/app/{app_code}", response_class=RedirectResponse, status_code=301)
async def get_application_content_root(app_code: str):
    return f"/ui/content/app/{app_code}/about"


@app.get("/ui/content/app/{app_code}/{partial}", response_class=HTMLResponse)
async def get_application_content_partial(
    request: Request, app_code: str, partial: str
):
    app = apps.get_app(app_code)
    return templates.TemplateResponse(
        request=request,
        name="content/single_application.html",
        context={"app": app, "active": partial},
    )


@app.get("/ui/partial/app/{app_code}/about", response_class=HTMLResponse)
async def get_application_partial_about(request: Request, app_code: str):
    app = apps.get_app(app_code)
    return templates.TemplateResponse(
        request=request, name="partial/app/about.html", context={"app": app}
    )


@app.get("/ui/partial/app/{app_code}/servers", response_class=HTMLResponse)
async def get_application_partial_servers(request: Request, app_code: str):
    servers = vms.list_vms(app_code)
    return templates.TemplateResponse(
        request=request,
        name="partial/app/servers.html",
        context={"app": {"code": app_code}, "servers": servers},
    )


@app.get("/ui/partial/app/{app_code}/databases", response_class=HTMLResponse)
async def get_application_partial_databases(request: Request, app_code: str):
    db_list = dbs.list_dbs(app_code)
    return templates.TemplateResponse(
        request=request,
        name="partial/app/databases.html",
        context={"app": {"code": app_code}, "databases": db_list},
    )
