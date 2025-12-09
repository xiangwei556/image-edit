from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=True, index=True)
    phone = Column(String(11), unique=True, nullable=True, index=True)
    nickname = Column(String(50), nullable=True)
    avatar = Column(String(255), nullable=True)
    gender = Column(Integer, default=0)  # 0: 未知, 1: 男, 2: 女
    hashed_password = Column(String(255), nullable=True)
    status = Column(Integer, default=1)  # 1: 启用, 0: 禁用, -1: 注销
    last_login_at = Column(DateTime, nullable=True)
    last_login_ip = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())