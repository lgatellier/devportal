from devportal.plugins import DevPortalPlugin

NAME = "vsphere"


class VspherePlugin(DevPortalPlugin):
    def register_plugin(self):
        pass


def load():
    return VspherePlugin()


__all__ = ["NAME", "load"]
