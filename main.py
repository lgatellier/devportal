from devportal.core import ui, plugin_loader  # noqa: F401
from devportal.core.app import app  # noqa: F401

# Loads all devportal plugins
plugin_loader.run()
