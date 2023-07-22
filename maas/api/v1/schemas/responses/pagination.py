from typing import Sequence, TypeVar, Generic

from pydantic import BaseModel

from maas.api.v1.schemas.responses.base import BaseResourceResponse

DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100

T = TypeVar("T", bound=BaseResourceResponse)

class PaginatedResponse(BaseModel, Generic[T]):
    """
    Base class to wrap objects in a pagination.
    Derived classes should overwrite the items property
    """
    total: int
    page: int
    size: int
    items: Sequence[T]
