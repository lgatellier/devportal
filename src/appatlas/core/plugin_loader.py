import importlib
import pkgutil
from types import ModuleType

from appatlas import plugins
from appatlas.plugins import AppAtlasPlugin

__all__ = ["run"]

PLUGINS = {}


def run():
    for mod in pkgutil.iter_modules(plugins.__path__):
        mod_fqdn = f"appatlas.plugins.{mod.name}"
        print(f"[INFO] Trying to load plugin from python module '{mod_fqdn}'")

        plugin_mod: ModuleType = importlib.import_module(mod_fqdn)

        if plugin_mod.NAME not in PLUGINS.keys():
            load_plugin(plugin_mod)
        else:
            print(f"[WARN] Two plugins declare the same name '{plugin_mod.NAME}'")


def load_plugin(plugin_module: ModuleType) -> None:
    print(f"[INFO] Loading plugin {plugin_module.NAME}")
    plugin = plugin_module.load()
    if isinstance(plugin, AppAtlasPlugin):
        PLUGINS[plugin_module.NAME] = plugin
    else:
        print(
            f"[ERROR] Invalid plugin {plugin_module.NAME} from module {plugin_module}"
        )
