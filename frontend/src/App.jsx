import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { Button, Card, Layout, Menu } from 'antd'
import { UploadOutlined, EditOutlined, UserOutlined, LogoutOutlined } from '@ant-design/icons'
import { Upload, message } from 'antd'

const { Header, Content, Sider } = Layout
const { Dragger } = Upload

function App() {
  const [collapsed, setCollapsed] = useState(false)

  const uploadProps = {
    name: 'file',
    multiple: false,
    action: 'http://localhost:8000/api/image/upload',
    onChange(info) {
      const { status } = info.file
      if (status !== 'uploading') {
        console.log(info.file, info.fileList)
      }
      if (status === 'done') {
        message.success(`${info.file.name} file uploaded successfully.`)
      } else if (status === 'error') {
        message.error(`${info.file.name} file upload failed.`)
      }
    },
  }

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Sider collapsible collapsed={collapsed} onCollapse={setCollapsed}>
        <div className="logo" />
        <Menu theme="dark" defaultSelectedKeys={['1']} mode="inline">
          <Menu.Item key="1" icon={<UploadOutlined />}>
            图片上传
          </Menu.Item>
          <Menu.Item key="2" icon={<EditOutlined />}>
            图片编辑
          </Menu.Item>
          <Menu.Item key="3" icon={<UserOutlined />}>
            个人中心
          </Menu.Item>
          <Menu.Item key="4" icon={<LogoutOutlined />}>
            退出登录
          </Menu.Item>
        </Menu>
      </Sider>
      <Layout className="site-layout">
        <Header className="site-layout-background" style={{ padding: 0 }} />
        <Content style={{ margin: '0 16px' }}>
          <div className="site-layout-background" style={{ padding: 24, minHeight: 360 }}>
            <Card title="图片上传" bordered={false} style={{ marginBottom: 24 }}>
              <Dragger {...uploadProps}>
                <p className="ant-upload-drag-icon">
                  <UploadOutlined />
                </p>
                <p className="ant-upload-text">点击或拖拽文件到此区域上传</p>
                <p className="ant-upload-hint">支持单个文件上传，最大10MB</p>
              </Dragger>
            </Card>
            
            <Card title="图片编辑" bordered={false}>
              <p>图片编辑功能开发中...</p>
              <Button type="primary" style={{ marginTop: 16 }}>开始编辑</Button>
            </Card>
          </div>
        </Content>
      </Layout>
    </Layout>
  )
}

export default App