from maas.api.base import API
from maas.api.v1.fabrics import FabricsHandler
from maas.api.v1.machines import MachinesHandler
from maas.api.v1.root import RootHandler
from maas.api.v1.spaces import SpacesHandler
from maas.api.v1.zones import ZonesHandler

APIv1 = API(
    prefix="/api/v1",
    tags=["v1"],
    handlers=[
        RootHandler(),
        ZonesHandler(),
        MachinesHandler(),
        FabricsHandler(),
        SpacesHandler(),
    ],
)