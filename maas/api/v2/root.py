from fastapi import APIRouter

from maas.api.base import Handler, handler


class RootHandler(Handler):
    @handler(path="/", methods=["GET"])
    def get(self):
        return ''
