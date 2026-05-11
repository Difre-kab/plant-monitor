"""Plant Monitor - FastAPI application entry point."""
from fastapi import FastAPI
from app.sensors import read_temperature
app = FastAPI(
    title="Plant Monitor",
    description="Industrial OT/IT bridge - Modbus TCP PLC monitoring",
    version= "0.1.0",
)

@app.get("/")
def read_root() -> dict[str,str]:
    """Health check endpoint."""
    return {"message": "Hello, plant-monitor"}
@app.get("/api/sensors")
def list_sensors() -> list[dict]:
    """Return current readings for all sensors."""
    return [read_temperature()]
