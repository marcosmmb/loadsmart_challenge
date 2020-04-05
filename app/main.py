from fastapi import FastAPI
from app.endpoints import mapping

app = FastAPI(title="Loadsmart Challenge API")


app.include_router(mapping.router, prefix="/mapping")
