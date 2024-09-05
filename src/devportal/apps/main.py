from sqlmodel import select, Session

from devportal.core.model import Application, ApplicationBase, engine, get_session

APPS = "data/apps.json"

CACHE = {"APPS": None}


def list_apps():
    with get_session() as session:
        statement = select(Application)
        return session.exec(statement).all()


def get_app(app_code: str):
    apps = [app for app in list_apps() if app.code == app_code]
    return apps[0] if len(apps) > 0 else None


def create_app(app: ApplicationBase):
    with Session(engine) as session:
        session.add(Application.model_validate(app))
        session.commit()
