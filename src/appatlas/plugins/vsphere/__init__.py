from appatlas.plugins import AppAtlasPlugin

NAME = "vsphere"


class VspherePlugin(AppAtlasPlugin):
    def register_plugin(self):
        pass


def load():
    return VspherePlugin()


__all__ = ["NAME", "load"]
