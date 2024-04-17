from nicegui import ui as nicegui_ui

from devportal.core import ui
from devportal.core import plugin_loader


# Loads all devportal plugins
plugin_loader.run()

ui.run()
nicegui_ui.run()
