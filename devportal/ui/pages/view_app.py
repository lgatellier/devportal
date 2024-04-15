from nicegui import ui


from devportal.ui import theme
from devportal.ui.components import vms as vms_ui, dbs as dbs_ui
from devportal.apps import main
from devportal.vms import main as vms
from devportal.dbs import main as dbs

def load():
    @ui.page("/app/{app_code}")
    def render(app_code: str):
        app = main.get_app(app_code)
        if not app:
            ui.label(f"Application {app['code']} does not exist")
            return
        with theme.page(f"Application {app_code} : {app['name']}"):
            content(app)


def content(app):
    with ui.card():
        ui.markdown("#### Application metadata")
        with ui.grid(columns=2):
            ui.label("Code") ; ui.label(app["code"])
            ui.label("Name") ; ui.label(app["name"])
            ui.label("Tags") ; ui.label(app["display_tags"])

    
    with ui.card():
        ui.markdown("#### Application Servers")
        app_vms = vms.list_vms(app['code'])
        if app_vms and len(app_vms) > 0:
            vms_ui.vm_list(app_vms)
        else:
            ui.label(f"No dedicated VMs for application {app['code']}")

    
    with ui.card():
        ui.markdown("#### Application Databases")
        app_dbs = dbs.list_dbs(app['code'])
        if app_dbs and len(app_dbs) > 0:
            dbs_ui.db_list(app_dbs)
        else:
            ui.label(f"No Databases for application {app['code']}")