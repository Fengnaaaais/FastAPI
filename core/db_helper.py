from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncEngine,
    AsyncSession,
)

from core.config import settings


class DatabaseHelper:
    def __init__(
        self,
        url: str,
        echo=settings.db.echo,
        echo_pull=settings.db.echo_pull,
        poll_size=settings.db.poll_sizesettings,
        max_overflow=settings.db.max_overflow,
    ):
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,
            echo_pull=echo_pull,
            poll_size=poll_size,
            max_overflow=max_overflow,
        )
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def dispose(self):
        await self.engine.dispose()

    async def session_getter(self):
        async with session_factory() as session:
            yield session


db_helper = DatabaseHelper(url=str(settings.db.url))
