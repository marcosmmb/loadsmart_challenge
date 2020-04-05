from pydantic import BaseModel
from typing import List

from app.models.base import TruckModel, CargoModel


class MappingInput(BaseModel):
    trucks: List[TruckModel] = []
    cargos: List[CargoModel] = []
