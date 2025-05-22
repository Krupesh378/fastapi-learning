"""This module contians the APIs"""
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud, schemas
from .database import get_session


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


@app.get("/users/", response_model=JSONResponse)
async def get_users(
    skip: int = 0,
    limit: int = 10,
    session: AsyncSession = Depends(get_session)
):
    return await crud.get_all_users(session, skip, limit)
