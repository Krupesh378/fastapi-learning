"""This module contians the APIs"""
import json

from fastapi import FastAPI, Depends
from fastapi.responses import StreamingResponse
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from . import models
from . import crud, schemas
from .database import get_session
from sqlalchemy.future import select

app = FastAPI()


@app.post("/user/", response_model=schemas.User)
async def create_user(
    user: schemas.UserCreate,
    session: AsyncSession = Depends(get_session)
):
    return await crud.create_user(session=session, user=user)


@app.get("/user/{user_id}", response_model=schemas.User)
async def retrive_user(
    user_id: int,
    session: AsyncSession = Depends(get_session)
):
    return await crud.get_user(session=session, user_id=user_id)


@app.get("/users/", response_model=List[schemas.User])
async def get_users(
    skip: int = 0,
    limit: int = 10,
    session: AsyncSession = Depends(get_session)
):
    return await crud.get_all_users(session, skip, limit)


@app.get("/users/stream")
async def stream_users(
    skip: int = 0,
    limit: int = 10,
    session: AsyncSession = Depends(get_session)
):
    async def user_stream():
        chunk_size = 1000
        start_id = skip
        end_id = skip + limit

        while end_id > start_id:
            stmt = select(models.User).where(
                models.User.id >= start_id,
                models.User.id < min(end_id, start_id + chunk_size)
            ).order_by(models.User.id)

            result = await session.execute(stmt)
            users = result.scalars().all()

            if not users: break

            for user in users:
                yield json.dumps(schemas.User.from_orm(user).dict()) + "\n"

            start_id += chunk_size

    return StreamingResponse(user_stream(), media_type="application/json")
