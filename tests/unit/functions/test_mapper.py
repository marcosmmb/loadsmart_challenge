from app.functions.mapper import Mapper, KdNode, TruckNode, CargoNode
from . import dummy_data


def test_kdnode_class():
    kdnode1 = KdNode((0, 1))
    assert kdnode1.latitude == 0
    assert kdnode1.longitude == 1
    assert KdNode._get_distance(kdnode1.point, (0, 0)) == 1


def test_trucknode_class():
    truck_node = TruckNode(dummy_data.TRUCK1)
    assert truck_node.point == (34.79981, -87.677251)
    assert truck_node.model == dummy_data.TRUCK1


def test_cargonode_class():
    cargo_node = CargoNode(dummy_data.CARGO1)
    assert cargo_node.point == (36.876719, -89.5878579)
    assert cargo_node.model == dummy_data.CARGO1


def test_mapper_class():
    mapper = Mapper(dummy_data.MAPPER_INPUT)
    mapper.build_tree()
    assert mapper.tree.root.model == dummy_data.TRUCK2
    assert mapper.map() == dummy_data.MAPPER_OUTPUT
