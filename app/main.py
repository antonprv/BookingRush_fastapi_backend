import uvicorn
import celery

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis

from app.config import settings
from app.bookings.router import router as router_bookings
from app.users.router import router as router_users
from app.hotels.rooms.router import router as router_users_hotels
from app.pages.router import router as router_pages
from app.images.router import router as router_images



app = FastAPI(redoc_url='/api/docs',
              swagger_ui_parameters={"tryItOutEnabled": True,
                                     "deepLinking": True})

@app.on_event('startup')
async def startup():
    redis = aioredis.from_url(
        f'redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}')
    FastAPICache.init(RedisBackend(redis=redis), prefix='cache')

app.mount("/static", StaticFiles(directory="app/static"), name="static")


app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_users_hotels)
app.include_router(router_pages)
app.include_router(router_images)

origins = [
    settings.CORS_URL,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Authorization",
                   "Access-Control-Allow-Origin",
                   "Access-Control-Allow-Headers",],
)


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
