from typing import Optional

from maas.api.v1.schemas.responses.base import BaseResourceResponse
from maas.api.v1.schemas.responses.pagination import PaginatedResponse
from pydantic import (
    Field,
)

class SpaceResponse(BaseResourceResponse):
    """
    A MAAS Space
    """
    name: str
    description: Optional[str] = Field(None)

    def __init__(self, *args, **kargs):
        super().__init__(kind="Space", href="/fabrics", **kargs)


class SpacesResponse(PaginatedResponse[SpaceResponse]):
    """
    The response for the spaces
    """