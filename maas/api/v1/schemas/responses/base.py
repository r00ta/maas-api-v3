from pydantic import BaseModel

class EmptyResponse(BaseModel):
    pass

class BaseResourceResponse(BaseModel):
    id: str
    kind: str
    href: str