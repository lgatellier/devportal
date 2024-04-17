from devportal.core import ui
from devportal.core import plugin_loader


# Loads all devportal plugins
plugin_loader.run()

ui.run()