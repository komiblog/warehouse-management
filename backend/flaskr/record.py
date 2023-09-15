# RESTful API
from flask_restx import Namespace, Resource, fields

# 认证库
from flask_login import login_required

# 导入数据库
from flaskr.db import db
from flaskr.models import record, product, user

api = Namespace('record', description='日志相关接口')

record_model = api.model('RecordModel', {
    'r_id': fields.Integer(required=True, description='记录编号'),
    'p_name': fields.Integer(required=True, description='产品名称'),
    'u_name': fields.Integer(required=True, description='用户名称'),
    'r_num': fields.Integer(required=True, description='产品数量'),
    'type': fields.String(max_length=10, required=True, description='操作类型'),
    'r_time': fields.DateTime(required=True, description='操作时间'),
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

        # stmt = (db.select(record, user)
        #         .join(user, record.r_u_id == user.u_id)
        #         # .join(product, record.r_p_id == product.p_id)

        #         .order_by(record.r_id))

        # print(stmt)

        # # 获取所有记录
        # records = db.session.execute(stmt
        #                              ).scalars()

        # records = db.session.query(
        #     db.select(record, product, user).where((product.p_id == record.r_p_id) & (user.u_id == record.r_u_id)).order_by(record.r_id)).all()

        # print(type(records))
        # print(records)
        # # 转换为列表
        # result = []
        # for res in records:
        #     result.append({
        #         'r_id': res.record.r_id,
        #         # 'p_name': res.p_name,
        #         # 'u_name': res.u_name,
        #         # 'r_num': res.r_num,
        #         # 'type': res.r_type,
        #         # 'r_time': res.r_time
        #     })
        records = db.session.execute(
            db.select(record).order_by(record.r_id)).scalars()

        products = db.session.execute(
            db.select(product).order_by(product.p_id).scalars()
        )

        users = db.session.execute(
            db.select(user).order_by(user.u_id).scalars()
        )

        print(type(records))
        print(records)
        # 转换为列表
        result = []
        pu_name = {}

        for res in records:
            for pro in products:
                if res.r_p_id == pro.p_id:
                    pu_name[res.r_p_id] = pro.p_name

        for res in records:
            for ur in users:
                if res.r_u_id == ur.u_id:
                    pu_name[res.r_u_id] = ur.u_id

        for res in records:
            result.append({
                'r_id': res.r_id,
                'p_name': pu_name[res.p_name],
                'u_name': pu_name[res.u_name],
                'r_num': res.r_num,
                'type': res.r_type,
                'r_time': res.r_time
            })

        return result, 200

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

        # 转换为字典
        result = []
        for r in records:
            result.append({
                'r_id': r.r_id,
                'r_p_id': r.r_p_id,
                'r_u_id': r.r_u_id,
                'r_num': r.r_num,
                'r_type': r.r_type,
                'r_time': r.r_time
            })

        return result, 200
