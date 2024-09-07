from fastapi import Request

from appatlas.core.api import api_app
from appatlas.core.models.app import Application, ApplicationQuery


@api_app.get("/applications", response_model=list[Application])
def search_applications(request: Request, search: str | None):
    query_result = ApplicationQuery.search(search)
    return query_result
