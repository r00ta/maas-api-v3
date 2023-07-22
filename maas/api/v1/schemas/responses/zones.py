from typing import Optional

from maas.api.v1.schemas.responses.base import BaseResourceResponse
from maas.api.v1.schemas.responses.pagination import PaginatedResponse
from pydantic import (
    Field,
)

class ZoneResponse(BaseResourceResponse):
    """
    A MAAS AZ
    """
    name: str
    description: Optional[str] = Field(None)

    def __init__(self, *args, **kargs):
        super().__init__(kind="Zone", href="/zones", **kargs)


class ZonesResponse(PaginatedResponse[ZoneResponse]):
    """
    The response for the list zones
    """
