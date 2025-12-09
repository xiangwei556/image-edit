# 图片编辑项目

这是一个图片编辑项目，包含后端API和前端界面。

## 项目结构

```
image-edit/
├── backend/    # 后端API
├── frontend/   # 前端界面
├── PRD文档.md  # 产品需求文档
└── README.md   # 项目说明
```

## 功能特性

- 图片上传与处理
- 图片编辑功能
- AI商品图合成
- 统一登录管理

## 技术栈

### 后端
- FastAPI
- Python 3.10+
- SQLAlchemy
- MySQL

### 前端
- React
- Vite

## 安装与运行

### 后端

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 前端

```bash
cd frontend
npm install
npm run dev
```

## 开发计划

查看 `统一登录管理系统开发计划.md` 文件获取详细的开发计划。

## 许可证

MIT