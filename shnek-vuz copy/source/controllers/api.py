from fastapi import APIRouter, Depends, status, Body, HTTPException

from sqlalchemy.orm import Session

from source.database import get_db
from source.crud import *
from source.schemas import FullGDSCreate, TemperatureCreate, PressureCreate
#инициализация роутера на подпути апи
router = APIRouter(prefix=f'/api',
                    tags=['API'],
                    responses={status.HTTP_404_NOT_FOUND: {'message': 'Not Found'}})

@router.get('/list')
async def test_get_posts(db: Session = Depends(get_db)):
    return get_full_GDSes(db=db)

@router.post('/new', status_code=status.HTTP_201_CREATED)
async def test_get_posts(
    data: FullGDSCreate = Body(...),
    db: Session = Depends(get_db),
):
    foundGDS = get_GDS(db=db, GDS_ID=data.GDS.GDS_ID)
    foundGDSTemperature = get_GDS_Temperature(db=db, GDS_ID=data.GDS.GDS_ID)
    foundGDSPressure = get_GDS_Pressure(db=db, GDS_ID=data.GDS.GDS_ID)

    if foundGDS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail='This GDS is already exists',
        )
    if foundGDSTemperature:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='This GDS temperature is already exists',
        )
    if foundGDSPressure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='This GDS pressure is already exists',
        )

    create_GDS(db=db, GDS=data.GDS)
    create_GDS_Temperature(db=db, GDS_Temperature=data.GDS_Temperature)
    create_GDS_Pressure(db=db, GDS_Pressure=data.GDS_Pressure)

    return {'message': 'created'}

@router.post('/new/temperature', status_code=status.HTTP_201_CREATED)
async def test_get_posts(
    data: TemperatureCreate = Body(...),
    db: Session = Depends(get_db),
):
    foundTemperature = get_Temerature(db=db, TempSensorID=data.TempSensorID)

    if not foundTemperature:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail='This temperature is not found',
        )

    create_Temperature(db=db, Temperature=data)

    return {'message': 'created'}

@router.post('/new/pressure', status_code=status.HTTP_201_CREATED)
async def test_get_posts(
    data: PressureCreate = Body(...),
    db: Session = Depends(get_db),
):
    foundPressure = get_Pressure(db=db, PressureSensorID=data.PressureSensorID)

    if not foundPressure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail='This pressure is not found',
        )

    create_Pressure(db=db, Pressure=data)

    return {'message': 'created'}