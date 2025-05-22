"""This module contains the simple crud operations which directly used rest apis"""
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from . import models, schemas


async def create_user(session: AsyncSession, user: schemas.UserCreate):
    user_data = models.User(**user.dict())
    session.add(user_data)
    await session.commit()
    await session.refresh(user_data)
    return user_data


async def get_user(session: AsyncSession, user_id: int):
    result = await session.execute(select(models.User).where(models.User.id == user_id))
    return result.scalar_one_or_none()


async def get_all_users(session: AsyncSession, skip: int = 0, limit: int = 10):
    result = await session.execute(select(models.User).offset(skip).limit(limit))
    return result.scalars().all()
