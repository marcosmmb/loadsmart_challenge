from pydantic import BaseModel
from typing import List

from app.models.base import TruckModel, CargoModel


class MapUnit(BaseModel):
    cargo: CargoModel
    truck: TruckModel


class MappingOutput(BaseModel):
    map: List[MapUnit]
