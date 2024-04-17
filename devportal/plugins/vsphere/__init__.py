from devportal.plugins import DevPortalPlugin

IDENTIFIER = "vsphere"

class VspherePlugin(DevPortalPlugin):
    def register_plugin(self):
        pass

def load():
    return VspherePlugin()

__all__ = ["IDENTIFIER", "load"]