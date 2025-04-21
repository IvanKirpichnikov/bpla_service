from typing import AsyncIterable

from dishka import AnyOf, provide, Provider, Scope
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine

from bpla_service.application.commitable import Commitable
from bpla_service.config import DatabaseConfig


class ConnectionProvider(Provider):
    scope = Scope.REQUEST
    
    @provide(scope=Scope.APP)
    async def session_maker(
        self,
        config: DatabaseConfig,
    ) -> AsyncIterable[async_sessionmaker[AsyncSession]]:
        engine = create_async_engine(config.url)
        session_maker = async_sessionmaker(
            bind=engine,
            expire_on_commit=True,
            autoflush=True
        )
        yield session_maker
        await engine.dispose(True)
    
    @provide
    async def get_session(
        self, pool: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AnyOf[AsyncSession, Commitable]]:
        async with pool() as session:
            await session.begin()
            yield session
