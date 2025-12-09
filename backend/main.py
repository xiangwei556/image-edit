from fastapi import FastAPI
from app.api import auth, image, user
from app.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

# 创建数据库表
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="图片编辑API",
    description="提供图片编辑和处理的API服务",
    version="1.0.0"
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(auth.router, prefix="/api/auth", tags=["认证"])
app.include_router(user.router, prefix="/api/user", tags=["用户"])
app.include_router(image.router, prefix="/api/image", tags=["图片处理"])

@app.get("/")
def root():
    return {"message": "图片编辑API服务"}
