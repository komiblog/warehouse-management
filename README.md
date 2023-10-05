# warehouse-management 仓库管理系统
## 部分网站界面
### 登录界面
![image](https://github.com/komiblog/warehouse-management/assets/102006886/24a9c1b3-22d7-44fa-a7f9-f25293cb6604)

### 主界面
![image](https://github.com/komiblog/warehouse-management/assets/102006886/e95ef05a-c0e2-4cee-a469-72b4d186cbf8)

### 所有记录查询界面
![image](https://github.com/komiblog/warehouse-management/assets/102006886/4d28ce7c-67cc-4051-8a92-8654c0e961e2)

### 产品修改界面
![image](https://github.com/komiblog/warehouse-management/assets/102006886/926d7900-d81d-4288-9771-1ff1213c8eb8)


## 接口文档
![image](https://github.com/komiblog/warehouse-management/assets/102006886/8887a650-59d3-42fc-bb23-2896d75182c1)


# 技术栈
## 前端
- Vue框架
（之后填坑）

## 后端
- Flask
（之后填坑）

# 快速开始
## 创建数据库
（之后填坑）

## 修改文件
### 后端
1. ``git clone`` 主分支，进入后端文件夹
2. 创建虚拟环境，并切换到该虚拟环境，参考 [官方网站](https://flask.palletsprojects.com/en/3.0.x/installation/#virtual-environments)
3. 下载需要的包 ``pip install`` 
4. 创建 ``instance`` 文件夹,并在里面创建 ``config.py`` 文件
```python
# 用于保证数据安全，可以是任意值，生产环境中应该是一个随机值
# $ python -c 'import secrets; print(secrets.token_hex())'
SECRET_KEY = 'dev'

# 禁用 SQLAlchemy 的修改跟踪功能，减少性能开销
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 跨域设置，允许所有域名访问
SESSION_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SECURE = 'True'

# 数据库链接
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@127.0.0.1:3306/warehouse'
```

### 前端
1. 进入前端文件夹
2. 安装package.json文件中需要的vue\node版本
3. 下载需要的依赖 ``npm install`` 

## 启动！
1. 启动后端 ``flask --app flaskr run``
2. 查看接口文档 http://127.0.0.1:5000
3. 启动前端 ``npm run serve``
4. 查看界面 http://localhost:8080/





