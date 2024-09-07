from appatlas.plugins import AppAtlasPlugin


class InValidPlugin(AppAtlasPlugin):
    pass


class ValidPlugin(AppAtlasPlugin):
    def register_plugin():
        pass


def test_invalid_plugin():
    assert not isinstance(InValidPlugin(), AppAtlasPlugin)


def test_valid_plugin():
    assert isinstance(ValidPlugin(), AppAtlasPlugin)
