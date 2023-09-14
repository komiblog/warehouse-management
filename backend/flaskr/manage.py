# RESTful API
from flask_restx import Namespace, Resource, fields

# 认证库
from flask_login import login_required, current_user

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


@api.route('/product')
class AllProduct(Resource):
    @api.doc(description='获取全部的产品列表')
    @api.marshal_with(product_model)
    @login_required
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
    @login_required
    def post(self):
        '''
        产品入库
        '''

        name = api.payload['p_name']
        type = api.payload['p_type']
        depiction = api.payload['p_depiction']
        price = api.payload['p_price']
        count = api.payload['p_count']

        # 名字为空
        if not name:
            return {'message': '名字为空'}, 400

        # 查询该名字是否存在
        exist = db.session.execute(
            db.select(product).where(product.p_name == name)
        ).scalar_one_or_none()

        # 如果存在，更新数量
        if exist:

            # 数量为空
            if not count:
                return {'message': '数量为空'}, 400

            # 更新数量
            db.session.execute(db.update(product)
                               .where(product.p_name == name)
                               .values(p_count=product.p_count + count))

            db.session.commit()

            # 新增记录日志
            db.session.execute(db.insert(record)
                               .values(r_p_id=exist.p_id,
                                       r_u_id=current_user.u_id,  # type: ignore
                                       r_num=count,
                                       r_type=1))
            db.session.commit()

            return {'message': '产品数量增加成功'}, 200

        # 如果不存在，新增产品
        else:
            # 判断存在性
            if not type or not price or not count:
                return {'message': '字段不完整'}, 400

            # 新增产品
            db.session.execute(db.insert(product)
                                 .values(p_name=name,
                                         p_type=type,
                                         p_depiction=depiction,
                                         p_price=price,
                                         p_count=count))
            db.session.commit()

            # 查询产品id
            product_id = db.session.execute(db.select(product.p_id)
                                            .where(product.p_name == name)).scalar_one_or_none()

            if not product_id:
                return {'message': '新增产品失败'}, 400

            # 新增记录日志
            db.session.execute(db.insert(record)
                                 .values(r_p_id=product_id,
                                         r_u_id=current_user.u_id,  # type: ignore
                                         r_num=count,
                                         r_type=1))
            db.session.commit()

            return {'message': '新增产品成功'}, 200


@api.route('/product/<int:id>')
class Product(Resource):
    @api.doc(description='产品修改，\
             数据库根据输入ID查找对应产品并且修改相应输入的产品信息。')
    @api.expect(product_model, validate=True)
    @login_required
    def put(self, id):
        '''
        产品修改
        '''
        name = api.payload['p_name']
        type = api.payload['p_type']
        depiction = api.payload['p_depiction']
        price = api.payload['p_price']

        # 存在性检查
        if not name or not type or not price:
            return {'message': '字段不完整'}, 400

        # 查询该产品是否存在
        if not checkid(id):
            return {'message': '产品不存在'}, 400

        # 更新产品
        db.session.execute(db.update(product)
                           .where(product.p_id == id)
                           .values(p_name=name,
                                   p_type=type,
                                   p_depiction=depiction,
                                   p_price=price))
        db.session.commit()

        return {'message': '修改成功'}, 200

    @api.doc(description='产品删除')
    @login_required
    def delete(self, id):
        '''
        产品删除
        '''
        # 查询该产品是否存在
        if not checkid(id):
            return {'message': '产品不存在'}, 400

        # 删除产品
        db.session.execute(db.delete(product).where(product.p_id == id))
        db.session.commit()

        return {'message': '删除成功'}, 200


@api.route('/search/<string:name>')
class Search(Resource):
    @api.doc(description='搜索查询，模糊查找')
    @api.marshal_with(product_model)
    @login_required
    def get(self, name):
        '''
        产品查询
        '''
        # 查询产品
        p = db.session.execute(
            db.select(product).where(product.p_name == name)).scalar_one_or_none()

        # 是否为空
        if not p:
            return {'message': '产品不存在'}, 400

        # 转换为列表
        result = []
        result.append({
            'p_id': p.p_id,
            'p_name': p.p_name,
            'p_type': p.p_type,
            'p_depiction': p.p_depiction,
            'p_price': p.p_price,
            'p_count': p.p_count
        })

        return result, 200


@api.route('/operate/<int:id>')
class Operate(Resource):
    @api.doc(description='首先进行产品数量检查，如果数量足够，那么就出库，并插入出库日志')
    @api.expect(product_model, validate=True)
    @login_required
    def put(self, id):
        '''
        产品出库
        '''
        count = api.payload['p_count']

        # 存在性检查
        if not count:
            return {'message': '数量为空'}, 400

        # 查询该产品是否存在
        if not checkid(id):
            return {'message': '产品不存在'}, 400

        # 查询该产品是否足够
        product_count = db.session.execute(db.select(product.p_count)
                                           .where(product.p_id == id)).scalar_one_or_none()

        if product_count < count:
            return {'message': '产品数量不足'}, 400
        else:
            # 出库
            db.session.execute(db.update(product)
                               .where(product.p_id == id)
                               .values(p_count=product.p_count - count))
            db.session.commit()

            # 新增记录日志
            db.session.execute(db.insert(record)
                               .values(r_p_id=id,
                                       r_u_id=current_user.u_id,  # type: ignore
                                       r_num=count,
                                       r_type=0))
            db.session.commit()

        return {'message': '产品出库成功'}, 200


# 检查产品是否存在
def checkid(id):
    exist = db.session.execute(db.select(product)
                               .where(product.p_id == id)).scalar_one_or_none()
    if not exist:
        return False

    return True
