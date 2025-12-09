# API路由初始化文件
from fastapi import APIRouter

# 创建API路由组
api_router = APIRouter()

# 导入各模块路由
from app.api import auth, user

# 注册路由
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(user.router, prefix="/user", tags=["user"])