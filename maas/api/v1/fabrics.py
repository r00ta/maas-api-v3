from starlette import status

from maas.api.base import Handler, handler
from maas.api.v1.schemas.requests.fabrics import CreateFabricRequest, \
    UpdateFabricRequest, CreateSubnetRequest, UpdateSubnetRequest, UpdateVlanRequest, CreateVlanRequest
from maas.api.v1.schemas.responses.base import EmptyResponse
from maas.api.v1.schemas.responses.fabrics import FabricsResponse, FabricResponse, VlansResponse, VlanResponse, SubnetsResponse, \
    SubnetResponse


class FabricsHandler(Handler):
    # FABRICS
    @handler(path="/fabrics", methods=["GET"], response_model=FabricsResponse)
    def get_fabrics(self) -> FabricsResponse:
        fabrics = FabricsResponse(total=0, page=0, size=0, items=[])
        return fabrics

    @handler(path="/fabrics", methods=["POST"], response_model=FabricResponse,
             status_code=status.HTTP_201_CREATED)
    def create_fabric(self, request: CreateFabricRequest) -> FabricResponse:
        return FabricResponse(id="0", name=request.name,
                              description=request.description)

    @handler(path="/fabrics/{id}", methods=["GET"], response_model=FabricResponse)
    def get_fabric(self, fabric_id: str) -> FabricResponse:
        return FabricResponse(id=fabric_id, name="")

    @handler(path="/fabrics/{fabric_id}", methods=["PUT"],
             response_model=FabricResponse)
    def update_fabrics(self, fabric_id: str, request: UpdateFabricRequest) -> \
            FabricResponse:
        return FabricResponse(id=fabric_id, name=request.name,
                              description=request.description)

    @handler(path="/fabrics/{fabric_id}", methods=["DELETE"])
    def delete_fabrics(self, fabric_id: str) -> EmptyResponse:
        return EmptyResponse()

    # VLANS
    @handler(path="/fabrics/{fabric_id}/vlans", methods=["GET"], response_model=VlansResponse)
    def get_vlans(self, fabric_id: str) -> VlansResponse:
        return VlansResponse(total=0, page=0, size=0, items=[])

    @handler(path="/fabrics/{fabric_id}/vlans", methods=["POST"], response_model=VlanResponse,
             status_code=status.HTTP_201_CREATED)
    def create_vlan(self, fabric_id: str, request: CreateVlanRequest) -> VlanResponse:
        return VlanResponse(id="0", name=request.name,
                            class_type=request.class_type)

    @handler(path="/fabrics/{fabric_id}/vlans/{vlan_id}", methods=["GET"], response_model=VlanResponse)
    def get_vlan(self, fabric_id: str, vlan_id: str) -> VlanResponse:
        return VlanResponse(
            id=vlan_id,
            name="test",
            vid=0,
            mtu=1500,
            dhcp_on=False,
            external_dhcp=None,
            relay_vlan=None,
            secondary_rack=None,
            space="unassigned",
            primary_rack=None
        )

    @handler(path="/fabrics/{fabric_id}/vlans/{vlan_id}", methods=["PUT"],
             response_model=VlanResponse)
    def update_vlan(self, fabric_id: str, vlan_id:str, request: UpdateVlanRequest) -> \
            VlanResponse:
        return VlanResponse(
            id=vlan_id,
            name=request.name,
            vid=0,
            mtu=1500,
            dhcp_on=False,
            external_dhcp=None,
            relay_vlan=None,
            secondary_rack=None,
            space="unassigned",
            primary_rack=None
        )

    @handler(path="/fabrics/{fabric_id}/vlans/{vlan_id}", methods=["DELETE"])
    def delete_vlan(self, fabric_id: str, vlan_id: str) -> EmptyResponse:
        return EmptyResponse()

    # SUBNETS
    @handler(path="/fabrics/{fabric_id}/vlans/{vlan_id}/subnets", methods=["GET"], response_model=SubnetsResponse)
    def get_subnets(self, fabric_id: str) -> SubnetsResponse:
        return SubnetsResponse(total=0, page=0, size=0, items=[])

    @handler(path="/fabrics/{fabric_id}/vlans/{vlan_id}/subnets", methods=["POST"], response_model=SubnetResponse,
             status_code=status.HTTP_201_CREATED)
    def create_subnet(self, fabric_id: str, request: CreateSubnetRequest) -> SubnetResponse:
        return SubnetResponse(
            id="0",
            name="test",
            vid=0,
            mtu=1500,
            dhcp_on=False,
            external_dhcp=None,
            relay_vlan=None,
            secondary_rack=None,
            space="unassigned",
            primary_rack=None
        )

    @handler(path="/fabrics/{fabric_id}/vlans/{vlan_id}/subnets/{subnet_id}", methods=["GET"], response_model=SubnetResponse)
    def get_subnet(self, fabric_id: str, vlan_id: str, subnet_id: str) -> SubnetResponse:
        return SubnetResponse(
            id=subnet_id,
            name="test",
            vid=0,
            mtu=1500,
            dhcp_on=False,
            external_dhcp=None,
            relay_vlan=None,
            secondary_rack=None,
            space="unassigned",
            primary_rack=None
        )

    @handler(path="/fabrics/{fabric_id}/vlans/{vlan_id}/subnets/{subnet_id}", methods=["PUT"],
             response_model=SubnetResponse)
    def update_subnet(self, fabric_id: str, vlan_id:str, subnet_id: str, request: UpdateSubnetRequest) -> \
            SubnetResponse:
        return SubnetResponse(
            id=subnet_id,
            name="test",
            description=None,
            cidr="",
            rdns_mode=0,
            gateway_ip="",
            dns_servers=[],
            allow_dns=False,
            allow_proxy=True,
            active_discovery=True,
            managed=True,
            disabled_boot_architectures=[]
        )

    @handler(path="/fabrics/{fabric_id}/vlans/{vlan_id}/subnets/{subnet_id}", methods=["DELETE"])
    def delete_subnet(self, fabric_id: str, vlan_id: str, subnet_id: str) -> EmptyResponse:
        return EmptyResponse()
