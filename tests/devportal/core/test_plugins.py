from devportal.plugins import DevPortalPlugin

class InValidPlugin(DevPortalPlugin):
    pass

class ValidPlugin(DevPortalPlugin):
    def register_plugin():
        pass


def test_invalid_plugin():
    assert not isinstance(InValidPlugin(), DevPortalPlugin)

def test_valid_plugin():
    assert isinstance(ValidPlugin(), DevPortalPlugin)