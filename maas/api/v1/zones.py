from starlette import status

from maas.api.base import Handler, handler
from maas.api.v1.schemas.requests.zones import CreateZoneRequest, \
    UpdateZoneRequest
from maas.api.v1.schemas.responses.base import EmptyResponse
from maas.api.v1.schemas.responses.zones import ZonesResponse, ZoneResponse


class ZonesHandler(Handler):
    @handler(path="/zones", methods=["GET"], response_model=ZonesResponse)
    def get_zones(self) -> ZonesResponse:
        zones = ZonesResponse(total=0, page=0, size=0, items=[])
        return zones

    @handler(path="/zones", methods=["POST"], response_model=ZoneResponse,
             status_code=status.HTTP_201_CREATED)
    def create_zone(self, request: CreateZoneRequest) -> ZoneResponse:
        return ZoneResponse(id="0", name=request.name,
                            description=request.description)

    @handler(path="/zones/{id}", methods=["GET"], response_model=ZoneResponse)
    def get_zone(self, zone_id: str) -> ZoneResponse:
        return ZoneResponse(id=zone_id, name="")

    @handler(path="/zones/{zone_id}", methods=["PUT"],
             response_model=ZoneResponse)
    def update_zones(self, zone_id: str, request: UpdateZoneRequest) -> \
            ZoneResponse:
        return ZoneResponse(id=zone_id, name=request.name,
                            description=request.description)

    @handler(path="/zones/{zone_id}", methods=["DELETE"])
    def delete_zones(self, zone_id: str) -> EmptyResponse:
        return EmptyResponse()



