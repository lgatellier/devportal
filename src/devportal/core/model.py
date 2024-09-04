from sqlmodel import Field, SQLModel, create_engine, Session

engine = create_engine(
    "postgresql://devportal:devportal@localhost/devportal", echo_pool=True
)


class Application(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    code: str
    name: str
    description: str


def get_session():
    return Session(engine)


__all__ = ["get_session", "Application"]
