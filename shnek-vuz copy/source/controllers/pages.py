import math

from fastapi import APIRouter, status, responses, Request, Depends, Query

from sqlalchemy.orm import Session

from fastapi.templating import Jinja2Templates

from source.database import get_db
from source import crud
#инициализация функции чтения html страниц
templates = Jinja2Templates(directory="source/pages/html")
#инициализация роутера на подпути pages
router = APIRouter(prefix=f'/pages',
                    tags=['API'],
                    responses={status.HTTP_404_NOT_FOUND: {'message': 'Not Found'}})
#покажет страницу с гдс
@router.get('/table', response_class=responses.HTMLResponse)
async def get_table(
    request: Request,
    page: int | None = Query(default=1),
    size: int | None = Query(default=5),
    db: Session = Depends(get_db),
):
    count = crud.get_GDS_count(db=db)
    pages = math.ceil(count / size)

    GDSes = crud.get_full_GDSes(db=db, limit=size, offset=(page-1)*size)

    context = {
        'request': request,
        'GDSes': GDSes, 
        'page': page,
        'pages': pages,
        'nextPage': pages if pages <= page else page + 1,
        'prevPage': 1 if page - 1 <= 1 else page - 1,
    }

    return templates.TemplateResponse(name='table.html', context=context)


@router.get('/table/temperature/{id}', response_class=responses.HTMLResponse)
async def get_table(
    request: Request,
    id: int,
    db: Session = Depends(get_db),
):
    temperatures = crud.get_full_Temperature(db=db, TempSensorID=id)

    context = {
        'request': request,
        'id': id,
        'temperatures': temperatures,
    }

    return templates.TemplateResponse(name='temperature.html', context=context)

@router.get('/table/pressure/{id}', response_class=responses.HTMLResponse)
async def get_table(
    request: Request,
    id: int,
    db: Session = Depends(get_db),
):
    pressures = crud.get_full_Pressure(db=db, PressureSensorID=id)

    context = {
        'request': request,
        'id': id,
        'pressures': pressures,
    }

    return templates.TemplateResponse(name='pressure.html', context=context)
