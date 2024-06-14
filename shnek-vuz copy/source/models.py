from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from source.database import Base

class GDS(Base):
    __tablename__ = 'GDS'

    id = Column(Integer, primary_key=True, nullable=False)

    GDS_ID = Column(Integer, unique=True, nullable=False)
    RegionID = Column(String(50), nullable=False)

    GDS_Temperature = relationship('GDS_Temperature', uselist=False, back_populates='GDS')
    GDS_Pressure = relationship('GDS_Pressure', uselist=False, back_populates='GDS')

class GDS_Temperature(Base):
    __tablename__ = 'GDS_Temperature'

    id = Column(Integer, primary_key=True, nullable=False)

    GDS_ID = Column(Integer, ForeignKey('GDS.GDS_ID', ondelete='CASCADE'), nullable=False)
    TempSensorID = Column(Integer, unique=True, nullable=False)

    GDS = relationship('GDS', uselist=False, back_populates='GDS_Temperature')
    Temperature = relationship('Temperature', uselist=False, back_populates='GDS_Temperature')

class GDS_Pressure(Base):
    __tablename__ = 'GDS_Pressure'

    id = Column(Integer, primary_key=True, nullable=False)

    GDS_ID = Column(Integer, ForeignKey('GDS.GDS_ID', ondelete='CASCADE'), nullable=False)
    PressureSensorID = Column(Integer, unique=True, nullable=False)

    GDS = relationship('GDS', uselist=False, back_populates='GDS_Pressure')
    Pressure = relationship('Pressure', uselist=False, back_populates='GDS_Pressure')

class Temperature(Base):
    __tablename__ = 'Temperature'

    id = Column(Integer, primary_key=True, nullable=False)

    TempSensorID = Column(Integer, ForeignKey('GDS_Temperature.TempSensorID', ondelete='CASCADE'), nullable=False)
    Temperature = Column(Float, default=0.0)
    DateTimeOfMeasure = Column(DateTime(timezone=True), default=func.now())

    GDS_Temperature = relationship('GDS_Temperature', uselist=False, back_populates='Temperature')


class Pressure(Base):
    __tablename__ = 'Pressure'

    id = Column(Integer, primary_key=True, nullable=False)

    PressureSensorID = Column(Integer, ForeignKey('GDS_Pressure.PressureSensorID', ondelete='CASCADE'), nullable=False)
    Pressure = Column(Float, default=0.0)
    DateTimeOfMeasure = Column(DateTime(timezone=True), default=func.now())

    GDS_Pressure = relationship('GDS_Pressure', uselist=False, back_populates='Pressure')
