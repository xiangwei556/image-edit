from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# 用户基础信息
class UserBase(BaseModel):
    username: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    nickname: Optional[str] = None
    avatar: Optional[str] = None
    gender: Optional[int] = 0

# 用户创建请求
class UserCreate(UserBase):
    password: str

# 用户登录请求
class UserLogin(BaseModel):
    username: str
    password: str

# 用户响应
class User(UserBase):
    id: int
    status: int
    last_login_at: Optional[datetime] = None
    last_login_ip: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# Token响应
class Token(BaseModel):
    access_token: str
    token_type: str

# Token数据
class TokenData(BaseModel):
    username: Optional[str] = None