from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import User, UserCreate, UserBase
from app.models.user import User as UserModel
from app.utils.auth_utils import get_password_hash, verify_password
from app.utils.auth_utils import create_access_token
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from app.config import settings
from datetime import datetime

router = APIRouter()

# 获取当前用户
def get_current_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl="/auth/login")), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(UserModel).filter(UserModel.username == username).first()
    if user is None:
        raise credentials_exception
    return user

# 获取当前用户信息
@router.get("/me", response_model=User)
def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user

# 更新用户信息
@router.put("/me", response_model=User)
def update_user_info(user_update: UserBase, current_user: UserModel = Depends(get_current_user), db: Session = Depends(get_db)):
    # 更新用户信息
    for field, value in user_update.model_dump().items():
        setattr(current_user, field, value)
    
    db.commit()
    db.refresh(current_user)
    return current_user