from contextlib import asynccontextmanager
from typing import AsyncIterator

import uvicorn
from dishka import AsyncContainer
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from bpla_service.adapters.api import auth, login, logout, me, uav, uav_flight
from bpla_service.config import Config


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    yield None
    await app.state.dishka_container.close()


def run_web(
    config: Config,
    container: AsyncContainer,
) -> None:
    fastapi_app = FastAPI(lifespan=lifespan)
    
    fastapi_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # REPLACE TO NGINX STATIC FILES
    fastapi_app.mount('/login', StaticFiles(directory='src/frontend/login', html=True))
    
    fastapi_app.mount('/auth', StaticFiles(directory='src/frontend/auth', html=True))
    
    fastapi_app.mount('/me', StaticFiles(directory='src/frontend/me', html=True))
    fastapi_app.mount('/me/uav', StaticFiles(directory='src/frontend/me/uav', html=True))
    fastapi_app.mount('/me/uavs', StaticFiles(directory='src/frontend/me/uavs', html=True))
    fastapi_app.mount('/me/uav/add', StaticFiles(directory='src/frontend/me/uav/add', html=True))
    
    fastapi_app.mount('/me/uav_flight', StaticFiles(directory='src/frontend/me/uav_flight', html=True))
    fastapi_app.mount('/me/uav_flights', StaticFiles(directory='src/frontend/me/uav_flights', html=True))
    fastapi_app.mount('/me/uav_flight/add', StaticFiles(directory='src/frontend/me/uav_flight/add', html=True))
    
    fastapi_app.mount('/_internal', StaticFiles(directory='src/frontend/_internal'))
    fastapi_app.mount('/_internal/types', StaticFiles(directory='src/frontend/_internal/types'))
    
    fastapi_app.include_router(auth.router)
    fastapi_app.include_router(login.router)
    fastapi_app.include_router(logout.router)
    fastapi_app.include_router(me.router)
    fastapi_app.include_router(uav.router)
    fastapi_app.include_router(uav_flight.router)
    
    setup_dishka(container, fastapi_app)
    
    uvicorn.run(fastapi_app, host="localhost", loop="asyncio")
