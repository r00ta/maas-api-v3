from starlette import status

from maas.api.base import Handler, handler
from maas.api.v1.schemas.requests.machines import UpdateMachineRequest, \
    CreateMachineRequest, CreateVolumeGroupRequest, UpdateVolumeGroupRequest
from maas.api.v1.schemas.responses.base import EmptyResponse
from maas.api.v1.schemas.responses.machines import MachineResponse, \
    MachinesResponse, VolumeGroupsResponse, VolumeGroupResponse


class MachinesHandler(Handler):

    # Base machines objects

    @handler(path="/machines", methods=["GET"], response_model=MachinesResponse)
    def get_machines(self) -> MachinesResponse:
        machines = MachinesResponse(total=0, page=0, size=0, items=[])
        return machines

    @handler(path="/machines", methods=["POST"], response_model=MachineResponse,
             status_code=status.HTTP_201_CREATED)
    def create_machine(self, request: CreateMachineRequest) -> MachineResponse:
        return MachineResponse(id="0", name=request.name,
                            description=request.description)

    @handler(path="/machines/{machine_id}", methods=["GET"],
             response_model=MachineResponse)
    def get_machine(self, machine_id: str) -> MachineResponse:
        return MachineResponse(id=machine_id, name="")

    @handler(path="/machines/{machine_id}", methods=["PUT"], response_model=MachineResponse)
    def update_machines(self, machine_id: str, request:UpdateMachineRequest) -> MachineResponse:
        return MachineResponse(id="0", name=request.name,
                            description=request.description)

    @handler(path="/machines/{machine_id}", methods=["DELETE"])
    def delete_machines(self, machine_id: str) -> EmptyResponse:
        return EmptyResponse()


    # Volume groups
    @handler(path="/machines/{machine_id}/volume_groups", methods=["GET"], response_model=VolumeGroupsResponse)
    def get_volume_groups(self, machine_id: str) -> VolumeGroupsResponse:
        return VolumeGroupsResponse(total=0, page=0, size=0, items=[])

    @handler(path="/machines/{machine_id}/volume_groups", methods=["POST"], response_model=VolumeGroupResponse,
             status_code=status.HTTP_201_CREATED)
    def create_volume_group(self, machine_id: str, request: CreateVolumeGroupRequest) -> VolumeGroupResponse:
        return VolumeGroupResponse(id="0", name=request.name,
                            description=request.description)

    @handler(path="/machines/{machine_id}/volume_groups/{volume_group_id}", methods=["GET"],
             response_model=MachineResponse)
    def get_volume_group(self, machine_id: str, volume_group_id: str) -> VolumeGroupResponse:
        return VolumeGroupResponse(id=machine_id, name="")

    @handler(path="/machines/{machine_id}", methods=["PUT"], response_model=VolumeGroupResponse)
    def update_volume_group(self, machine_id: str, volume_group_id: str, request: UpdateVolumeGroupRequest) -> \
            VolumeGroupResponse:
        return VolumeGroupResponse(id="0", name=request.name,
                            description=request.description)

    @handler(path="/machines/{machine_id}/volume_groups/{volume_group_id}", methods=["DELETE"])
    def delete_volume_group(self) -> EmptyResponse:
        return EmptyResponse()