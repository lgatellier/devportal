from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
import i18n
from jinja2 import Environment, FileSystemLoader


app = FastAPI()
jinja_env = Environment(loader=FileSystemLoader("src/templates"), autoescape=True)
jinja_env.filters["i18n"] = i18n.t
templates = Jinja2Templates(env=jinja_env)

i18n.set("locale", "fr")
i18n.set("fallback", "en")
i18n.load_path.append("src/i18n")

__all__ = ["app", "templates"]
