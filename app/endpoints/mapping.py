from fastapi import APIRouter

from app.models.inputs import MappingInput
from app.models.outputs import MappingOutput
from app.functions.mapper import Mapper

router = APIRouter()


@router.post("/", response_model=MappingOutput)
async def _map_cargos_to_trucks(mapping_input: MappingInput):
    mapper = Mapper(mapping_input)
    mapper.build_tree()
    return mapper.map()
