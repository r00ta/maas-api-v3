from starlette import status

from maas.api.base import Handler, handler
from maas.api.v1.schemas.requests.spaces import CreateSpaceRequest, UpdateSpaceRequest
from maas.api.v1.schemas.responses.base import EmptyResponse
from maas.api.v1.schemas.responses.spaces import SpacesResponse, SpaceResponse


class SpacesHandler(Handler):
    # FABRICS
    @handler(path="/spaces", methods=["GET"], response_model=SpacesResponse)
    def get_spaces(self) -> SpacesResponse:
        spaces = SpacesResponse(total=0, page=0, size=0, items=[])
        return spaces

    @handler(path="/spaces", methods=["POST"], response_model=SpaceResponse,
             status_code=status.HTTP_201_CREATED)
    def create_space(self, request: CreateSpaceRequest) -> SpaceResponse:
        return SpaceResponse(id="0", name=request.name,
                              description=request.description)

    @handler(path="/spaces/{id}", methods=["GET"], response_model=SpaceResponse)
    def get_space(self, space_id: str) -> SpaceResponse:
        return SpaceResponse(id=space_id, name="")

    @handler(path="/spaces/{space_id}", methods=["PUT"],
             response_model=SpaceResponse)
    def update_spaces(self, space_id: str, request: UpdateSpaceRequest) -> \
            SpaceResponse:
        return SpaceResponse(id=space_id, name=request.name,
                              description=request.description)

    @handler(path="/spaces/{space_id}", methods=["DELETE"])
    def delete_spaces(self, space_id: str) -> EmptyResponse:
        return EmptyResponse()
