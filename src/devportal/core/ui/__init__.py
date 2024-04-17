from devportal.core.ui.pages import home, view_app


def run():
    for page in [home, view_app]:
        page.load()
