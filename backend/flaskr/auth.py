# RESTful API
from flask_restx import Namespace, Resource, fields

# 用户认证
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

# 导入数据库
from flaskr.db import db
from flaskr.models import user


api = Namespace('auth', description='认证相关接口')


# 定义校验字段，展示模型
user_model = api.model('UserModel', {
    'u_name': fields.String(max_length=20, required=True, description='用户名'),
    'u_pwd': fields.String(max_length=50, required=True, description='密码'),
})


login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(db.select(user).where(user.u_id == user_id)).scalar_one_or_none()


# 登录视图
@api.route('/login')
class Login(Resource):
    @api.doc(description='用户登录,数据库验证账号密码')
    @api.expect(user_model, validate=True)  # 校验输入,确认请求体不为空
    def post(self):
        '''
        用户登录
        '''
        if current_user.is_authenticated:  # type: ignore
            return {'message': '用户已登录'}, 200

        username = api.payload.get('u_name')
        password = api.payload.get('u_pwd')

        # 如果用户名或密码为空，返回错误信息
        if not username or not password:
            return {'message': '用户名或密码为空'}, 400

        # 获取用户
        d_user = db.session.execute(db.select(user)
                                    .where(user.u_name == username)).scalar_one_or_none()

        # 如果用户不存在或密码错误，返回错误信息
        if not d_user:

            return {'message': '用户不存在'}, 401

        if d_user.u_pwd != password:
            return {'message': '密码错误'}, 401

        # 登录用户
        login_user(d_user)

        return {'message': '登录成功'}, 200


# 登出视图
@api.route('/logout')
class Logout(Resource):
    @api.doc(description='用户登出，需求文档里没有，但是还是比较需要的。')
    @login_required  # 权限控制，必须先登录
    def get(self):
        '''
        用户登出
        '''
        logout_user()
        return {'message': '登出成功'}, 200


# 测试数据库连接
@api.route('/testdb')
class Test(Resource):
    @api.doc(description='测试数据库连接是否正常')
    def get(self):
        '''
        测试数据库连接
        '''
        if db.session.is_active:
            return '数据库连接成功', 200
        else:
            return '数据库连接失败', 500
