# RESTful API
from flask_restx import Namespace, Resource, fields

# 认证库
from flask_login import login_required

from datetime import datetime

# 导入数据库
from flaskr.db import db
from flaskr.models import record, product, user

api = Namespace('record', description='日志相关接口')

record_model = api.model('RecordModel', {
    'r_id': fields.Integer(required=True, description='记录编号'),
    'p_name': fields.String(required=True, description='产品名称'),
    'u_name': fields.String(required=True, description='用户名称'),
    'r_num': fields.Integer(required=True, description='产品数量'),
    'type': fields.String(max_length=10, required=True, description='操作类型'),
    'r_time': fields.String(required=True, description='操作时间'),
})


@api.route('/record')
class AllRecord(Resource):
    @api.doc(description='获取所有记录')
    @api.marshal_with(record_model)
    @login_required
    def get(self):
        '''
        所有记录列表
        '''
        records = db.session.execute(
            db.select(record).order_by(record.r_id)).scalars()

        products = db.session.execute(
            db.select(product).order_by(product.p_id)
        ).scalars()

        users = db.session.execute(
            db.select(user).order_by(user.u_id)
        ).scalars()

        print(type(records))
        print(records)
        # 转换为列表
        result = []
        p_names = {}
        u_names = {}

        result1 = []
        result2 = []
        result3 = []

        for res in records:
            result1.append({
                'r_id': res.r_id,
                'r_p_id': res.r_p_id,
                'r_u_id': res.r_u_id,
                'r_num': res.r_num,
                'r_type': res.r_type,
                'r_time': res.r_time
            })

        for pro in products:
            result2.append({
                'p_id': pro.p_id,
                'p_name': pro.p_name,
            })

        for ur in users:
            result3.append({
                'u_id': ur.u_id,
                'u_name': ur.u_name,
            })

        for re in result1:
            for po in result2:
                if re['r_p_id'] == po['p_id']:
                    p_names[re['r_p_id']] = po['p_name']

        for re in result1:
            for u in result3:
                if re['r_u_id'] == u['u_id']:
                    u_names[re['r_u_id']] = u['u_name']

        for res in result1:

            if res['r_p_id'] in p_names and res['r_u_id'] in u_names:
                result.append({
                    'r_id': res['r_id'],
                    'p_name': p_names[res['r_p_id']],
                    'u_name': u_names[res['r_u_id']],
                    'r_num': res['r_num'],
                    'type': "入库" if res['r_type'] == 1 else "出库",
                    # datetime转换为字符串
                    'r_time': res['r_time'].strftime('%Y-%m-%d %H:%M:%S')
                })

        return result, 200


@api.route('/record/<int:id>')
class Record(Resource):

    @api.doc(description='查看该产品记录')
    def get(self, id):
        '''
        查看该产品记录
        '''
        # 获取该产品记录
        records = db.session.execute(
            db.select(record, user).where(record.r_p_id == id).order_by(record.r_id)).scalars()

        products = db.session.execute(
            db.select(product).order_by(product.p_id)
        ).scalars()

        users = db.session.execute(
            db.select(user).order_by(user.u_id)
        ).scalars()

        print(type(records))
        print(records)
        # 转换为列表
        result = []
        p_names = {}
        u_names = {}

        result1 = []
        result2 = []
        result3 = []

        for res in records:
            result1.append({
                'r_id': res.r_id,
                'r_p_id': res.r_p_id,
                'r_u_id': res.r_u_id,
                'r_num': res.r_num,
                'r_type': res.r_type,
                'r_time': res.r_time
            })

        for pro in products:
            result2.append({
                'p_id': pro.p_id,
                'p_name': pro.p_name,
            })

        for ur in users:
            result3.append({
                'u_id': ur.u_id,
                'u_name': ur.u_name,
            })

        for re in result1:
            for po in result2:
                if re['r_p_id'] == po['p_id']:
                    p_names[re['r_p_id']] = po['p_name']

        for re in result1:
            for u in result3:
                if re['r_u_id'] == u['u_id']:
                    u_names[re['r_u_id']] = u['u_name']

        for res in result1:

            if res['r_p_id'] in p_names and res['r_u_id'] in u_names:
                result.append({
                    'r_id': res['r_id'],
                    'p_name': p_names[res['r_p_id']],
                    'u_name': u_names[res['r_u_id']],
                    'r_num': res['r_num'],
                    'type': "入库" if res['r_type'] == 1 else "出库",
                    # datetime转换为字符串
                    'r_time': res['r_time'].strftime('%Y-%m-%d %H:%M:%S')
                })

        return result, 200
