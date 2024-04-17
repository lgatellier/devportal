import importlib
import pkgutil
from types import ModuleType

from devportal import plugins
from devportal.plugins import DevPortalPlugin

__all__ = ["run"]

PLUGINS = {}

def run():
    for mod in pkgutil.iter_modules(plugins.__path__):
        mod_fqdn = f"devportal.plugins.{mod.name}"
        print(f"[INFO] Trying to load plugin from python module '{mod_fqdn}'")
        plugin_module: ModuleType = importlib.import_module(mod_fqdn)

        if plugin_module.IDENTIFIER not in PLUGINS.keys():
            load_plugin(plugin_module)
        else:
            print(f"[WARN] Detected two plugnis with same identifier '{plugin_module.IDENTIFIER}'")

def load_plugin(plugin_module: ModuleType) -> None:
    print(f"[INFO] Loading plugin {plugin_module.IDENTIFIER}")
    plugin = plugin_module.load()
    if isinstance(plugin, DevPortalPlugin):
        PLUGINS[plugin_module.IDENTIFIER] = plugin
    else:
        print(f"[ERROR] Plugin {plugin_module.IDENTIFIER} from module {plugin_module.__name__} is not a valid DevPortalPlugin subclass")