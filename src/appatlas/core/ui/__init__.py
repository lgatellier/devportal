from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import request_validation_exception_handler
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import i18n
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader

from appatlas.core import fastapi_app

ui_app = FastAPI()

fastapi_app.mount("/static", StaticFiles(directory="src/static"), name="static")
fastapi_app.mount("/ui", ui_app)


@ui_app.get("/", response_class=RedirectResponse, status_code=301)
async def ui_root():
    return "/ui/apps"


@ui_app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    print(request.headers)
    if "HX-Request" in request.headers:
        return templates.TemplateResponse(
            request=request,
            name="partial/errors.html",
            context={"errors": exc.errors()},
            status_code=400,
        )
    return await request_validation_exception_handler(request, exc)


jinja_env = Environment(loader=FileSystemLoader("src/templates"), autoescape=True)
jinja_env.filters["i18n"] = i18n.t
templates = Jinja2Templates(env=jinja_env)

i18n.set("locale", "fr")
i18n.set("fallback", "en")
i18n.load_path.append("src/i18n")
