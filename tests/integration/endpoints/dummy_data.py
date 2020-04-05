MAPPING_POST_200_INPUT = {
    "trucks": [
        {
            "truck": "Hartford Plastics Incartford",
            "city": "Florence",
            "state": "AL",
            "lat": 34.79981,
            "lng": -87.677251,
        },
        {
            "truck": "Beyond Landscape & Design Llcilsonville",
            "city": "Fremont",
            "state": "CA",
            "lat": 37.5482697,
            "lng": -121.9885719,
        },
        {
            "truck": "Empire Of Dirt Llcquality",
            "city": "Hampden",
            "state": "ME",
            "lat": 44.7445421,
            "lng": -68.8370436,
        },
    ],
    "cargos": [
        {
            "product": "Light bulbs",
            "origin_city": "Sikeston",
            "origin_state": "MO",
            "origin_lat": 36.876719,
            "origin_lng": -89.5878579,
            "destination_city": "Grapevine",
            "destination_state": "TX",
            "destination_lat": 32.9342919,
            "destination_lng": -97.0780654,
        },
        {
            "product": "Recyclables",
            "origin_city": "Christiansburg",
            "origin_state": "VA",
            "origin_lat": 37.1298517,
            "origin_lng": -80.4089389,
            "destination_city": "Apopka",
            "destination_state": "FL",
            "destination_lat": 28.6934076,
            "destination_lng": -81.5322149,
        },
    ],
}

MAPPING_POST_200_OUTPUT = {
    "map": [
        {
            "cargo": {
                "product": "Light bulbs",
                "origin_city": "Sikeston",
                "origin_state": "MO",
                "origin_lat": 36.876719,
                "origin_lng": -89.5878579,
                "destination_city": "Grapevine",
                "destination_state": "TX",
                "destination_lat": 32.9342919,
                "destination_lng": -97.0780654,
            },
            "truck": {
                "truck": "Hartford Plastics Incartford",
                "city": "Florence",
                "state": "AL",
                "lat": 34.79981,
                "lng": -87.677251,
            },
        },
        {
            "cargo": {
                "product": "Recyclables",
                "origin_city": "Christiansburg",
                "origin_state": "VA",
                "origin_lat": 37.1298517,
                "origin_lng": -80.4089389,
                "destination_city": "Apopka",
                "destination_state": "FL",
                "destination_lat": 28.6934076,
                "destination_lng": -81.5322149,
            },
            "truck": {
                "truck": "Empire Of Dirt Llcquality",
                "city": "Hampden",
                "state": "ME",
                "lat": 44.7445421,
                "lng": -68.8370436,
            },
        },
    ]
}


MAPPING_POST_422_INPUT = {
    "trucks": [
        {
            "city": "Florence",
            "state": "AL",
            "lat": 34.79981,
            "lng": -87.677251,
        },
        {
            "truck": "Beyond Landscape & Design Llcilsonville",
            "city": "Fremont",
            "state": "CA",
            "lat": 37.5482697,
            "lng": -121.9885719,
        },
        {
            "truck": "Empire Of Dirt Llcquality",
            "city": "Hampden",
            "state": "ME",
            "lat": 44.7445421,
            "lng": -68.8370436,
        },
    ],
    "cargos": [
        {
            "product": "Light bulbs",
            "origin_city": "Sikeston",
            "origin_state": "MO",
            "origin_lat": 36.876719,
            "origin_lng": -89.5878579,
            "destination_city": "Grapevine",
            "destination_state": "TX",
            "destination_lat": 32.9342919,
            "destination_lng": -97.0780654,
        },
        {
            "product": "Recyclables",
            "origin_city": "Christiansburg",
            "origin_state": "VA",
            "origin_lat": 37.1298517,
            "origin_lng": -80.4089389,
            "destination_city": "Apopka",
            "destination_state": "FL",
            "destination_lat": 28.6934076,
            "destination_lng": -81.5322149,
        },
    ],
}

MAPPING_POST_422_OUTPUT = {
    "detail": [
        {
            "loc": ["body", "mapping_input", "trucks", 0, "truck"],
            "msg": "field required",
            "type": "value_error.missing",
        }
    ]
}
