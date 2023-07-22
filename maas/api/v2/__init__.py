from maas.api.base import API
from maas.api.v2.root import RootHandler

APIv2 = API(
    prefix="/api/v2",
    tags=["v2"],
    handlers=[
        RootHandler(),
    ],
)