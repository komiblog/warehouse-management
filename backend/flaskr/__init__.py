from flask import Flask

# ORM框架，操作mysql数据库
from flaskr.db import db

# RESTful API
from flask_restx import Api

# 注册用户认证
from flaskr.auth import login_manager

# 跨域
from flask_cors import CORS


def create_app():
    # 创造并配置app, instance_relative_config=True表示配置文件是相对于instance folder的相对路径
    app = Flask(__name__, instance_relative_config=True)

    # RESTful API
    api = Api(app, version='1.0', title='WareHouse API',
              description='仓库管理接口文档')

    # 跨域
    CORS(app, supports_credentials=True)

    # 从 config.py 文件中读取配置
    app.config.from_pyfile('config.py')

    # 初始化数据库
    db.init_app(app)

    # 初始化用户认证
    login_manager.init_app(app)

    # 导入并注册命名空间
    from . import manage
    api.add_namespace(manage.api)

    from . import auth
    api.add_namespace(auth.api)

    from . import record
    api.add_namespace(record.api)

    # 开启debug模式
    if __name__ == '__main__':
        app.run(debug=True)

    return app
