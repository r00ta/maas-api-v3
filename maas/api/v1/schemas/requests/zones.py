from typing import Optional

from pydantic import BaseModel


class CreateZoneRequest(BaseModel):
    name: str
    description: Optional[str]

class UpdateZoneRequest(CreateZoneRequest):
    pass