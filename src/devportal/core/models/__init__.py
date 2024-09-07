from sqlmodel import create_engine, Session

engine = create_engine(
    "postgresql://devportal:devportal@localhost/devportal", echo_pool=True
)


def get_session():
    return Session(engine)


__all__ = ["engine", "get_session"]
