"""Plant Monitor - FastAPI application entry point."""
from fastapi import FastAPI
app = FastAPI(
    title="Plant Monitor",
    description="Industrial OT/IT bridge - Modbus TCP PLC monitoring",
    version= "0.1.0",
)

@app.get("/")
def read_root() -> dict[str,str]:
    """Health check endpoint."""
    return {"message": "Hello, Plant-Monitor"}