from appatlas.core import plugin_loader
from appatlas.core import fastapi_app  # noqa: F401
from appatlas.core.api import apps  # noqa: F401
from appatlas.core.ui import app, component  # noqa: F401

# Loads all appatlas plugins
plugin_loader.run()
