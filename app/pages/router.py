from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from fastapi_cache.decorator import cache

from app.hotels.router import get_hotels_by_location_and_time
from app.config import settings


router = APIRouter(
    prefix='/pages',
    tags=['frontend']
)


templates = Jinja2Templates(directory='app/templates')


@router.get('/hotels')
async def get_hotels_page(
    request: Request,
    hotels=Depends(get_hotels_by_location_and_time)
):
    return templates.TemplateResponse('hotels.html',
                                      context={'request': request,
                                               'hotels': hotels})
