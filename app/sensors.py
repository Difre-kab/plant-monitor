"""Sensor data simulation
Eachfunction returns a single, freshly computed reading that mimics how a real industrial sensor wold behave: slow sinussoidal drift plus gaussian noise.
"""
import math
import random   
import time
from datetime import datetime 

def read_temperature() -> dict:
    """Return a realistic reactor temperature reading."""
    base = 75.0
    cycle = math.sin(time.time() /30.0)  * 5.0
    noise = random.gauss(0.0, 1.25)
    value = round(base + cycle + noise, 2)

    return {
        "id": "temp_01",
        "label": "Reactor temperature",
        "value": value,
        "unit": "°C",
        "timestamp": datetime.now().isoformat(timespec="seconds"),
    }