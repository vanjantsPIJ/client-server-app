
from pydantic import BaseModel

from datetime import datetime

# GDS

class GDSBase(BaseModel):
    GDS_ID: int
    RegionID: str

class GDSCreate(GDSBase):
    pass

class GDS(GDSBase):
    id: int



# GDS Temperature

class GDSTemperatureBase(BaseModel):
    GDS_ID: int
    TempSensorID: int

class GDSTemperatureCreate(GDSTemperatureBase):
    pass

class GDSTemperature(GDSTemperatureBase):
    id: int



# GDS Pressure

class GDSPressureBase(BaseModel):
    GDS_ID: int
    PressureSensorID: int

class GDSPressureCreate(GDSPressureBase):
    pass

class GDSPressure(GDSPressureBase):
    id: int



# Temperature

class TemperatureBase(BaseModel):
    TempSensorID: int
    Temperature: float
    DateTimeOfMeasure: datetime

class TemperatureCreate(TemperatureBase):
    pass

class Temperature(TemperatureBase):
    id: int



# Pressure

class PressureBase(BaseModel):
    PressureSensorID: int
    Pressure: float
    DateTimeOfMeasure: datetime

class PressureCreate(PressureBase):
    pass

class Pressure(PressureBase):
    id: int




class FullGDSCreate(BaseModel):
    GDS: GDSCreate
    GDS_Temperature: GDSTemperatureCreate
    GDS_Pressure: GDSPressureCreate
