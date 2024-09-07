from enum import Enum
from uuid import uuid4, UUID
from sqlmodel import Field, Relationship, SQLModel, select, Session

from devportal.core.models import engine, get_session


class ApplicationBase(SQLModel):
    code: str = Field(min_length=1, nullable=False)
    name: str = Field(min_length=1, nullable=False)
    description: str = Field(min_length=1, nullable=False)


class Application(ApplicationBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    components: list["Component"] = Relationship(back_populates="application")


class Type(Enum):
    batch = "batch"
    library = "library"
    service = "service"


class ComponentBase(SQLModel):
    code: str = Field(min_length=1, nullable=False)
    name: str = Field(min_length=1, nullable=False)
    description: str = Field(min_length=1, nullable=False)
    type: Type = Field(default=Type.service, index=True)
    application_id: UUID = Field(
        default=None, foreign_key="application.id", nullable=False, index=True
    )


class Component(ComponentBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    application: Application | None = Relationship(back_populates="components")


class ApplicationQuery:
    @staticmethod
    def list():
        with get_session() as session:
            statement = select(Application)
            return session.exec(statement).all()

    @staticmethod
    def get(app_code: str):
        apps = [app for app in ApplicationQuery.list() if app.code == app_code]
        return apps[0] if len(apps) > 0 else None

    @staticmethod
    def create(app: ApplicationBase):
        with Session(engine) as session:
            session.add(Application.model_validate(app))
            session.commit()


class ComponentQuery:
    @staticmethod
    def list(application_id: UUID):
        with get_session() as session:
            statement = select(Component).where(
                Component.application_id == application_id
            )
            return session.exec(statement).all()

    @staticmethod
    def get(id: UUID, lazy=False):
        with get_session() as session:
            result = session.get(Component, id)
            result.application
            return result


__all__ = [
    "Application",
    "ApplicationBase",
    "ApplicationQuery",
    "Component",
    "ComponentBase",
    "ComponentQuery",
]
