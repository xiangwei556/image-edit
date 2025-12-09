from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
import app.utils.auth_utils as auth_utils
import app.schemas.user as user_schemas
import app.models.user as user_models
from app.database import get_db
from app.config import settings

router = APIRouter(
    prefix="/auth",
    tags=["认证"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

@router.post("/token", response_model=user_schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth_utils.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = auth_utils.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=user_schemas.User)
def read_users_me(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    username = auth_utils.verify_token(token, credentials_exception)
    user = db.query(user_models.User).filter(user_models.User.username == username).first()
    if user is None:
        raise credentials_exception
    return user

@router.post("/register", response_model=user_schemas.User)
def register(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(user_models.User).filter(user_models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = auth_utils.get_password_hash(user.password)
    new_user = user_models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        phone=user.phone
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user