from flask import jsonify

# RESTful API
from flask_restx import Namespace, Resource, fields

# 导入数据库
from flaskr.db import db
from flaskr.models import product, record, user

api = Namespace('manage', description='仓库管理相关接口')


product_model = api.model('ProductModel', {
    'p_id': fields.Integer(required=True, description='产品编号'),
    'p_name': fields.String(max_length=20, required=True, description='产品名称'),
    'p_type': fields.String(max_length=20, required=True, description='产品类型'),
    'p_depiction': fields.String(max_length=100, description='产品描述'),
    'p_price': fields.Integer(required=True, description='产品价格'),
    'p_count': fields.Integer(required=True, description='产品数量'),
})

record_model = api.model('RecordModel', {
    'r_id': fields.Integer(required=True, description='记录编号'),
    'p_name': fields.Integer(required=True, description='产品名称'),
    'u_name': fields.Integer(required=True, description='用户名称'),
    'r_num': fields.Integer(required=True, description='产品数量'),
    'type': fields.String(max_length=10, required=True, description='操作类型'),
    'r_time': fields.DateTime(required=True, description='操作时间'),
})


@api.route('/product')
class AllProduct(Resource):
    @api.doc(description='获取全部的产品列表')
    @api.marshal_with(product_model)
    def get(self):
        '''
        获取产品列表
        '''
        # 获取所有产品
        products = db.session.execute(
            db.select(product).order_by(product.p_id)).scalars()

        # 转换为字典
        result = []
        for p in products:
            result.append({
                'p_id': p.p_id,
                'p_name': p.p_name,
                'p_type': p.p_type,
                'p_depiction': p.p_depiction,
                'p_price': p.p_price,
                'p_count': p.p_count
            })

        return result, 200

    @api.doc(description='首先是产品存在性检查：存在就更新数量，不存在就增加这个产品。\
             然后是字段完整性检查：名称，价格，数量都不能为空。\
             最后，产品存入数据库。新增入库操作日志')
    @api.expect(product_model, validate=True)
    def post(self):
        '''
        产品入库
        '''

        # 如果请求体不为空，获取请求体
        # if api.payload is not None:

        return {'message': '添加成功'}, 200


@api.route('/product/<int:id>')
class Product(Resource):
    @api.doc(description='产品修改，\
             数据库根据输入ID查找对应产品并且修改相应输入的产品信息。')
    def put(self):
        '''
        产品修改
        '''

        return {'message': '修改成功'}, 200

    @api.doc(description='产品删除')
    def delete(self):
        '''
        产品删除
        '''
        return {'message': '删除成功'}, 200


@api.route('/search/<string:name>')
class Search(Resource):
    @api.doc(description='搜索查询')
    def get(self):
        '''
        产品查询
        '''
        return {'message': '获取成功'}, 200


@api.route('/operate/<int:id>')
class Operate(Resource):

    @api.doc(description='首先进行产品数量检查，如果数量足够，那么就出库，并插入出库日志')
    def put(self):
        '''
        产品出库
        '''

        return {'message': '修改成功'}, 200
