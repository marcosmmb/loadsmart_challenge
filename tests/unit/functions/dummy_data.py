from app.models.inputs import MappingInput, TruckModel, CargoModel
from app.models.outputs import MappingOutput

TRUCK1 = TruckModel(
    **{
        "truck": "Hartford Plastics Incartford",
        "city": "Florence",
        "state": "AL",
        "lat": 34.79981,
        "lng": -87.677251,
    }
)

TRUCK2 = TruckModel(
    **{
        "truck": "Beyond Landscape & Design Llcilsonville",
        "city": "Fremont",
        "state": "CA",
        "lat": 37.5482697,
        "lng": -121.9885719,
    }
)

TRUCK3 = TruckModel(
    **{
        "truck": "Empire Of Dirt Llcquality",
        "city": "Hampden",
        "state": "ME",
        "lat": 44.7445421,
        "lng": -68.8370436,
    }
)

TRUCKS = [TRUCK1, TRUCK2, TRUCK3]

CARGO1 = CargoModel(
    **{
        "product": "Light bulbs",
        "origin_city": "Sikeston",
        "origin_state": "MO",
        "origin_lat": 36.876719,
        "origin_lng": -89.5878579,
        "destination_city": "Grapevine",
        "destination_state": "TX",
        "destination_lat": 32.9342919,
        "destination_lng": -97.0780654,
    }
)

CARGO2 = CargoModel(
    **{
        "product": "Recyclables",
        "origin_city": "Christiansburg",
        "origin_state": "VA",
        "origin_lat": 37.1298517,
        "origin_lng": -80.4089389,
        "destination_city": "Apopka",
        "destination_state": "FL",
        "destination_lat": 28.6934076,
        "destination_lng": -81.5322149,
    }
)

CARGOS = [CARGO1, CARGO2]

MAPPER_INPUT = MappingInput(**{"trucks": TRUCKS, "cargos": CARGOS})


MAP_UNIT1 = {"cargo": CARGO1, "truck": TRUCK1}
MAP_UNIT2 = {"cargo": CARGO2, "truck": TRUCK3}

MAPPER_OUTPUT = {"map": [MAP_UNIT1, MAP_UNIT2]}
