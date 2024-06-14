from sqlalchemy.orm import Session, joinedload
from sqlalchemy import desc

from . import models, schemas
#функции для извлечения данных по айди 
def get_GDS(db: Session, GDS_ID: int):
    return db.query(models.GDS).filter(models.GDS.GDS_ID == GDS_ID).first()

def get_GDS_count(db: Session):
    return db.query(models.GDS).count()

def get_GDS_Temperature(db: Session, GDS_ID: int):
    return db.query(models.GDS_Temperature).filter(models.GDS_Temperature.GDS_ID == GDS_ID).first()

def get_GDS_Pressure(db: Session, GDS_ID: int):
    return db.query(models.GDS_Pressure).filter(models.GDS_Pressure.GDS_ID == GDS_ID).first()

def get_Temerature(db: Session, TempSensorID: int):
    return db.query(models.GDS_Temperature).filter(models.GDS_Temperature.TempSensorID == TempSensorID).first()

def get_Pressure(db: Session, PressureSensorID: int):
    return db.query(models.GDS_Pressure).filter(models.GDS_Pressure.PressureSensorID == PressureSensorID).first()
# для получения всех записей из таблицы
def get_full_GDSes(db: Session, offset: int = 0, limit: int = 5):
    return db.query(models.GDS)\
        .options(
            joinedload(models.GDS.GDS_Temperature),
            joinedload(models.GDS.GDS_Pressure),
        )\
        .offset(offset)\
        .limit(limit)\
        .all()

def get_full_Temperature(db: Session, TempSensorID: int):
    return db.query(models.Temperature)\
        .filter(models.Temperature.TempSensorID == TempSensorID)\
        .order_by(desc(models.Temperature.DateTimeOfMeasure))\
        .all()

def get_full_Pressure(db: Session, PressureSensorID: int):
    return db.query(models.Pressure)\
        .filter(models.Pressure.PressureSensorID == PressureSensorID)\
        .order_by(desc(models.Pressure.DateTimeOfMeasure))\
        .all()

#создание записи в таблице
def create_GDS(db: Session, GDS: schemas.GDSCreate):
    new_GDS = models.GDS(
        GDS_ID=GDS.GDS_ID,
        RegionID=GDS.RegionID,
    )

    db.add(new_GDS)
    db.commit()
    db.refresh(new_GDS)

    return new_GDS

def create_GDS_Temperature(db: Session, GDS_Temperature: schemas.GDSTemperatureCreate):
    new_GDS_Temperature = models.GDS_Temperature(
        GDS_ID=GDS_Temperature.GDS_ID,
        TempSensorID=GDS_Temperature.TempSensorID,
    )

    db.add(new_GDS_Temperature)
    db.commit()
    db.refresh(new_GDS_Temperature)

    return new_GDS_Temperature

def create_GDS_Pressure(db: Session, GDS_Pressure: schemas.GDSPressureCreate):
    new_GDS_Pressure = models.GDS_Pressure(
        GDS_ID=GDS_Pressure.GDS_ID,
        PressureSensorID=GDS_Pressure.PressureSensorID,
    )

    db.add(new_GDS_Pressure)
    db.commit()
    db.refresh(new_GDS_Pressure)

    return new_GDS_Pressure

def create_Temperature(db: Session, Temperature: schemas.TemperatureCreate):
    new_Temperature = models.Temperature(
        TempSensorID=Temperature.TempSensorID,
        Temperature=Temperature.Temperature,
        DateTimeOfMeasure=Temperature.DateTimeOfMeasure,   
    )

    db.add(new_Temperature)
    db.commit()
    db.refresh(new_Temperature)

    return new_Temperature

def create_Pressure(db: Session, Pressure: schemas.PressureCreate):
    new_Pressure = models.Pressure(
        PressureSensorID=Pressure.PressureSensorID,
        Pressure=Pressure.Pressure,
        DateTimeOfMeasure=Pressure.DateTimeOfMeasure,   
    )

    db.add(new_Pressure)
    db.commit()
    db.refresh(new_Pressure)

    return new_Pressure
