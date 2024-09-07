from enum import Enum
from uuid import uuid4, UUID
from sqlmodel import Field, Relationship, SQLModel, select, Session
from sqlalchemy.orm import selectinload

from devportal.core.models import engine, get_session


class DomainBase(SQLModel):
    name: str = Field(min_length=1, nullable=False)
    description: str = Field(min_length=1, nullable=False)


class Domain(DomainBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    applications: list["Application"] = Relationship(back_populates="domain")


class ApplicationBase(SQLModel):
    code: str = Field(min_length=1, nullable=False)
    name: str = Field(min_length=1, nullable=False)
    description: str = Field(min_length=1, nullable=False)
    domain_id: UUID = Field(
        default=None, foreign_key="domain.id", nullable=False, index=True
    )


class Application(ApplicationBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    domain: Domain = Relationship(
        back_populates="applications", sa_relationship_kwargs={"lazy": "joined"}
    )
    components: list["Component"] = Relationship(back_populates="application")


class Type(Enum):
    batch = "batch"
    library = "library"
    service = "service"


class TechStackBase(SQLModel):
    name: str = Field(min_length=1, nullable=False)
    description: str = Field(min_length=1, nullable=False)


class TechStack(TechStackBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)


class ComponentBase(SQLModel):
    code: str = Field(min_length=1, nullable=False)
    name: str = Field(min_length=1, nullable=False)
    description: str = Field(min_length=1, nullable=False)
    type: Type = Field(default=Type.service, index=True)
    techstack_id: UUID = Field(
        default=None, foreign_key="techstack.id", nullable=True, index=True
    )
    application_id: UUID = Field(
        default=None, foreign_key="application.id", nullable=False, index=True
    )


class Component(ComponentBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    application: Application | None = Relationship(back_populates="components")
    tech_stack: TechStack | None = Relationship(
        sa_relationship_kwargs={"lazy": "joined"}
    )


class ApplicationQuery:
    @staticmethod
    def list():
        with get_session() as session:
            statement = select(Application)
            return session.exec(statement).all()

    @staticmethod
    def get(id: UUID):
        with get_session() as session:
            return session.get(Application, id)

    @staticmethod
    def create(app: ApplicationBase):
        with Session(engine) as session:
            session.add(Application.model_validate(app))
            session.commit()


class ComponentQuery:
    @staticmethod
    def list(application_id: UUID = None):
        with get_session() as session:
            statement = select(Component).where(
                Component.application_id == application_id
            )
            return session.exec(statement).all()

    @staticmethod
    def list_all():
        with get_session() as session:
            statement = select(Component).options(selectinload(Component.application))
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
