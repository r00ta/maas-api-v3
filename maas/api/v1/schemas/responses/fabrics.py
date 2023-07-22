from typing import Optional

from maas.api.v1.schemas.responses.base import BaseResourceResponse
from maas.api.v1.schemas.responses.pagination import PaginatedResponse
from pydantic import (
    Field,
)

class FabricResponse(BaseResourceResponse):
    """
    A MAAS Fabric
    """
    name: str
    class_type: Optional[str] = Field(None)

    def __init__(self, *args, **kargs):
        super().__init__(kind="Fabric", href="/fabrics", **kargs)


class FabricsResponse(PaginatedResponse[FabricResponse]):
    """
    The response for the fabrics
    """

class VlanResponse(BaseResourceResponse):
    """
    A MAAS VLAN
    """
    name: str
    vid: int
    mtu: int
    dhcp_on: bool
    external_dhcp: Optional[str]
    relay_vlan: Optional[str]
    secondary_rack: Optional[str]
    space: Optional[str]
    primary_rack: Optional[str]


    def __init__(self, *args, **kargs):
        super().__init__(kind="Fabric", href="/fabrics", **kargs)


class VlansResponse(PaginatedResponse[VlanResponse]):
    """
    The response for the fabrics
    """

class SubnetResponse(BaseResourceResponse):
    """
    A MAAS Fabric
    """
    name: str
    description: str
    cidr: str
    rdns_mode: int
    gateway_ip: str
    dns_servers: list[str]
    allow_dns: bool
    allow_proxy: bool
    active_discovery: bool
    managed: bool
    disabled_boot_architectures: list[str]

    def __init__(self, *args, **kargs):
        super().__init__(kind="Subnet", href="/subnets", **kargs)


class SubnetsResponse(PaginatedResponse[SubnetResponse]):
    """
    The response for the fabrics
    """
