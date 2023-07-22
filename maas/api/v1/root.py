from fastapi import APIRouter

from maas.api.base import Handler, handler
from maas.api.v1.schemas.responses.base import EmptyResponse


class RootHandler(Handler):
    @handler(path="/", methods=["GET"])
    def get(self) -> EmptyResponse:
        return EmptyResponse()
