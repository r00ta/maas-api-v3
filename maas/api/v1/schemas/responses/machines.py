from typing import Optional

from maas.api.v1.schemas.responses.base import BaseResourceResponse
from maas.api.v1.schemas.responses.pagination import PaginatedResponse
from pydantic import (
    Field,
)

class MachineResponse(BaseResourceResponse):
    """
    A MAAS machine
    """
    name: str
    description: Optional[str] = Field(None)

    def __init__(self, *args, **kargs):
        super().__init__(kind="Machine", href="/machines", **kargs)


class MachinesResponse(PaginatedResponse[MachineResponse]):
    """
    The response for the list machines
    """

class VolumeGroupResponse(BaseResourceResponse):
    pass

class VolumeGroupsResponse(PaginatedResponse[MachineResponse]):
    pass
