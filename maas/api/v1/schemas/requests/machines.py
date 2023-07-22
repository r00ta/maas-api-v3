from typing import Optional

from pydantic import BaseModel


class CreateMachineRequest(BaseModel):
    name: str
    description: Optional[str]

class UpdateMachineRequest(CreateMachineRequest):
    pass

class CreateVolumeGroupRequest(BaseModel):
    name: str
    description: Optional[str]

class UpdateVolumeGroupRequest(CreateVolumeGroupRequest):
    pass