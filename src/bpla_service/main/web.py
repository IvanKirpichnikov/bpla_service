from contextlib import asynccontextmanager
from typing import AsyncIterator

import uvicorn
from dishka import AsyncContainer
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

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
    
    fastapi_app.include_router(auth.router)
    fastapi_app.include_router(login.router)
    fastapi_app.include_router(logout.router)
    fastapi_app.include_router(me.router)
    fastapi_app.include_router(uav.router)
    fastapi_app.include_router(uav_flight.router)
    
    setup_dishka(container, fastapi_app)
    
    uvicorn.run(fastapi_app, host="0.0.0.0", port=9000)
