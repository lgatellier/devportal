from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import request_validation_exception_handler
from fastapi.templating import Jinja2Templates
import i18n
from jinja2 import Environment, FileSystemLoader


api = FastAPI()


@api.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
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

__all__ = ["api", "templates"]
