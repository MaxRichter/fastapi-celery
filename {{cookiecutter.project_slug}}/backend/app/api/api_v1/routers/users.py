from fastapi import APIRouter, Depends
import typing as t
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.db.crud import (
    get_users,
    get_user,
    create_user,
    delete_user,
    edit_user,
)
from app.db.schemas import UserCreate, UserEdit, User, UserAdmin
from app.core.auth import get_current_active_user, get_current_active_superuser
from app.db import models

users_router = r = APIRouter()


@r.get(
    "/users",
    response_model=t.List[UserAdmin],
    response_model_exclude_none=True,
)
async def users_list(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_superuser),
):
    """
    Get all users
    """
    return get_users(db=db)


@r.get("/users/me", response_model=User, response_model_exclude_none=True)
async def user_me(current_user=Depends(get_current_active_user)):
    """
    Get own user
    """
    return current_user


@r.put("/users/me", response_model=User, response_model_exclude_none=True)
async def user_me_edit(
    user_in: UserEdit,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user),
):
    """
    Update own user
    """
    return edit_user(db=db, user_id=current_user.id, user=user_in)


@r.get(
    "/users/{user_id}",
    response_model=UserAdmin,
    response_model_exclude_none=True,
)
async def user_details(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_superuser),
):
    """
    Get any user details
    """
    user = get_user(db=db, user_id=user_id)
    return user


@r.post("/users", response_model=UserAdmin, response_model_exclude_none=True)
async def user_create(
    user_in: UserCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_superuser),
):
    """
    Create a new user
    """
    return create_user(db=db, user=user_in)


@r.put(
    "/users/{user_id}",
    response_model=UserAdmin,
    response_model_exclude_none=True,
)
async def user_edit(
    user_id: int,
    user_in: UserAdmin,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_superuser),
):
    """
    Update existing user as admin
    """
    return edit_user(db=db, user_id=user_id, user=user_in)


@r.delete(
    "/users/{user_id}",
    response_model=UserAdmin,
    response_model_exclude_none=True,
)
async def user_delete(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_superuser),
):
    """
    Delete existing user
    """
    return delete_user(db, user_id)
