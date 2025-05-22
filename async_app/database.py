"""This module has been handle the database connectiviy."""
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "postgresql+asyncpg://kruepsh:krupesh123@localhost:5432/learn"

engine = create_async_engine(DATABASE_URL)
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()


async def get_session():
    async with AsyncSessionLocal() as session:
        yield session
