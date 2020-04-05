from pydantic import BaseModel


class TruckModel(BaseModel):
    truck: str
    city: str
    state: str
    lat: float
    lng: float


class CargoModel(BaseModel):
    product: str
    origin_city: str
    origin_state: str
    origin_lat: float
    origin_lng: float
    destination_city: str
    destination_state: str
    destination_lat: float
    destination_lng: float
