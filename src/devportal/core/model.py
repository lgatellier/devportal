from enum import Enum
from sqlmodel import Field, SQLModel, create_engine, Session

engine = create_engine(
    "postgresql://devportal:devportal@localhost/devportal", echo_pool=True
)


class Type(Enum):
    batch = "batch"
    library = "library"
    service = "service"


class ApplicationBase(SQLModel):
    code: str = Field(min_length=1)
    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    type: Type = Field(default=Type.service, index=True)


class Application(ApplicationBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


def get_session():
    return Session(engine)


__all__ = ["engine", "get_session", "Application"]
