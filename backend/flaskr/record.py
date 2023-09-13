# RESTful API
from flask_restx import Namespace, Resource, fields

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
    def get(self):
        '''
        产品列表
        '''
        # 获取所有记录
        records = db.session.execute(
            db.select(record).order_by(record.r_id)).scalars()

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


@api.route('/record/<int:id>')
class Record(Resource):

    @api.doc(description='查看该产品记录')
    def get(self, id):
        '''
        查看该产品记录
        '''
        # 获取该产品记录
        records = db.session.execute(
            db.select(record).where(record.r_p_id == id).order_by(record.r_id)).scalars()

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
