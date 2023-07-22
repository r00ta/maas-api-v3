from typing import Optional

from pydantic import BaseModel


class CreateSpaceRequest(BaseModel):
    name: str
    description: Optional[str]

class UpdateSpaceRequest(CreateSpaceRequest):
    pass