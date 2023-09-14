from flaskr.db import db
from flask_login import UserMixin


class user(db.Model, UserMixin):
    """
    用户表
    """
    # 指定字段
    u_id = db.Column(db.Integer, nullable=False,
                     primary_key=True, autoincrement=True)
    u_name = db.Column(db.String(20), nullable=False, unique=True)
    u_pwd = db.Column(db.String(50), nullable=False)

    def get_id(self):
        try:
            return str(self.u_id)
        except AttributeError:
            raise NotImplementedError(
                "No `id` attribute - override `get_id`") from None


class product(db.Model):
    """
    产品表
    """
    p_id = db.Column(db.Integer, nullable=False,
                     primary_key=True, autoincrement=True)
    p_name = db.Column(db.String(20), nullable=False, unique=True)
    p_type = db.Column(db.String(20), nullable=False)
    p_depiction = db.Column(db.String(100))
    p_price = db.Column(db.Integer, nullable=False)
    p_count = db.Column(db.Integer, nullable=False)


class record(db.Model):
    """
    记录表
    """
    r_id = db.Column(db.Integer, nullable=False,
                     primary_key=True, autoincrement=True)
    r_p_id = db.Column(db.Integer, nullable=False)
    r_u_id = db.Column(db.Integer, nullable=False)
    r_num = db.Column(db.Integer, nullable=False)
    r_type = db.Column(db.Integer, nullable=False)
    r_time = db.Column(db.DateTime, nullable=False)
