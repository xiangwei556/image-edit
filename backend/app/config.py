from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # 应用配置
    app_name: str = "图片编辑API"
    debug: bool = True
    
    # 数据库配置
    database_username: str = "root"
    database_password: str = "password"
    database_hostname: str = "localhost"
    database_port: str = "3306"
    database_name: str = "image_edit"
    
    # JWT配置
    secret_key: str = "your-secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # 图片上传配置
    upload_dir: str = "uploads"
    max_file_size: int = 10 * 1024 * 1024  # 10MB
    
    # 阿里云配置
    aliyun_access_key_id: str = ""
    aliyun_access_key_secret: str = ""
    
    class Config:
        env_file = ".env"


settings = Settings()
