import math


class KdNode:

    DIMENSION = 2

    def __init__(self, point=(None, None)):
        self.point = point
        self.left, self.right = None, None

    @property
    def latitude(self):
        return self.point[0]

    @property
    def longitude(self):
        return self.point[1]

    @classmethod
    def build(cls, nodes, depth=0):
        length = len(nodes)
        if length == 0:
            return None

        axis = cls._get_axis(depth)
        nodes.sort(key=lambda node: node.point[axis])

        node = nodes[length // 2]
        node.left = cls.build(nodes[: length // 2], depth + 1)
        node.right = cls.build(nodes[length // 2 + 1 :], depth + 1)

        return node

    @classmethod
    def _get_axis(cls, depth):
        return depth % cls.DIMENSION

    @classmethod
    def get_closest(cls, root, target, mapping, depth=0):
        path = dict()
        cls._get_closest_node(root, target, depth, path, mapping)
        ranking = sorted(path.keys(), key=lambda key: path[key])
        closest = ranking.pop(0)
        while mapping.get(closest) is not None:
            closest = ranking.pop(0)
        mapping[closest] = target
        return closest

    @classmethod
    def _get_closest_node(cls, root, target, depth, path, mapping):
        if root is None:
            return

        axis = cls._get_axis(depth)
        next_node, opposite_node = cls._decide_next_node(root, target, axis)

        closest_node = lambda node: cls._get_closest_node(
            node, target, depth + 1, path, mapping
        )
        decide_best = lambda node: cls._decide_closer(target, closest, node)
        best_distance = lambda best: cls._get_distance(
            target.point, best.point
        )

        closest = closest_node(next_node)
        best = decide_best(root)
        if best_distance(best) > abs(target.point[axis] - root.point[axis]):
            closest = closest_node(opposite_node)
            best = decide_best(best)

        if mapping.get(best) is not None:
            return
        path[best] = best_distance(best)
        return best

    @staticmethod
    def _decide_next_node(root, target, axis):
        if target.point[axis] < root.point[axis]:
            return root.left, root.right
        return root.right, root.left

    @classmethod
    def _decide_closer(cls, target, point_a, point_b):
        if point_a is None:
            return point_b
        elif point_b is None:
            return point_a

        distance_a = cls._get_distance(target.point, point_a.point)
        distance_b = cls._get_distance(target.point, point_b.point)

        return point_a if distance_a < distance_b else point_b

    @classmethod
    def _get_distance(cls, point_a, point_b):
        x_a, y_a = point_a
        x_b, y_b = point_b

        dx, dy = (x_a - x_b), (y_a - y_b)
        return math.sqrt(dx ** 2 + dy ** 2)

    def __repr__(self):
        return "{} <lat: {}, lng: {}>".format(
            self.__class__.__name__, self.latitude, self.longitude
        )


class TruckNode(KdNode):
    def __init__(self, truck):
        super().__init__((truck.lat, truck.lng))
        self.model = truck


class CargoNode(KdNode):
    def __init__(self, cargo):
        super().__init__((cargo.origin_lat, cargo.origin_lng))
        self.model = cargo


class KdTree:
    def __init__(self, nodes):
        self.root = KdNode.build(nodes)
        self.mapping = dict()

    def get_closest(self, target):
        return KdNode.get_closest(self.root, target, self.mapping)


class Mapper:
    def __init__(self, mapping_input):
        self.truck_nodes = self._parse_list(mapping_input.trucks, TruckNode)
        self.cargo_nodes = self._parse_list(mapping_input.cargos, CargoNode)
        self.tree = None

    def _parse_list(self, input_list, node_class):
        return [node_class(item) for item in input_list]

    def build_tree(self):
        self.tree = KdTree(self.truck_nodes)

    def map(self):
        response = list()
        for cargo in self.cargo_nodes:
            truck = self.tree.get_closest(cargo)
            response.append({"cargo": cargo.model, "truck": truck.model})
        return {"map": response}
