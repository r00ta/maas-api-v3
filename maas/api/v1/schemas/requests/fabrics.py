from typing import Optional

from pydantic import BaseModel


class CreateFabricRequest(BaseModel):
    name: str
    class_type: Optional[str]

class UpdateFabricRequest(CreateFabricRequest):
    pass

class CreateVlanRequest(BaseModel):
    name: str
    class_type: Optional[str]

class UpdateVlanRequest(CreateVlanRequest):
    pass

class CreateSubnetRequest(BaseModel):
    name: str
    cidr: Optional[str]
    dns_servers: list[str]
    gateway_ip: str

class UpdateSubnetRequest(CreateSubnetRequest):
    pass