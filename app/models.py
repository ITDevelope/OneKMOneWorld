from app import db
from datetime import datetime
from sqlalchemy.dialects.mysql import LONGTEXT

# 用户信息表


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    uid = db.Column(db.String(225), unique=True)
    username = db.Column(db.String(225))
    password = db.Column(db.String(225))
    icon = db.Column(db.String(225))  # 头像
    email = db.Column(db.String(225))
    phone_number = db.Column(db.String(225))
    wechat = db.Column(db.String(225))  # 微信账号
    qq = db.Column(db.String(225))  # qq账号
    weibo = db.Column(db.String(225))  # 微博账号
    name = db.Column(db.String(225))
    gender = db.Column(db.String(225))
    birthdate = db.Column(db.DateTime())
    ID_number = db.Column(db.String(225))  # 身份证号
    register_date = db.Column(db.DateTime())  # 注册时间


# 客户信息表
class Client(User):

    __tablename__ = 'clients'

    sign = db.Column(LONGTEXT)  # 个性签名
    money = db.Column(db.Integer)  # 钱包
    credit_card_number = db.Column(db.String(225))  # 银行卡号
    address = db.Column(db.String(225))  # 常住地
    feedback = db.Column(LONGTEXT)  # 反馈信息
    membership = db.Column(db.Integer)  # 会员信息
    logging_status = db.Column(db.Integer)  # 登录状态
    score = db.Column(db.Integer)  # 总积分

    def __init__(self, uid, username, password, icon, email, phone_number, wechat, qq, weibo, name, gender, birthdate, ID_number, register_date, sign, money, credit_card_number, address, feedback, membership, logging_status, score):
        self.uid = uid
        self.username = username
        self.password = password
        self.icon = icon
        self.email = email
        self.phone_number = phone_number
        self.wechat = wechat
        self.qq = qq
        self.weibo = weibo
        self.name = name
        self.gender = gender
        self.birthdate = birthdate
        self.ID_number = ID_number
        self.register_date = register_date
        self.sign = sign
        self.money = money
        self.credit_card_number = credit_card_number
        self.address = address
        self.feedback = feedback
        self.membership = membership
        self.logging_status = logging_status
        self.score = score

        db.create_all()

    def __repr__(self):
        return "<clients uid '{}'>".format(self.uid)

# 浏览记录信息表


class Record(db.Model):

    __tablename__ = 'records'

    id = db.Column(db.Integer, unique=True)
    record_id = db.Column(db.String(225), primary_key=True, unique=True)
    uid = db.Column(db.String(225))
    comment = db.Column(LONGTEXT)  # 评论内容
    like = db.Column(db.Integer)  # 是否点赞
    collect = db.Column(db.Integer)  # 是否收藏
    share_id = db.Column(db.String(225))  # 分享内容的id

    def __init__(self, record_id, uid, comment, like, collect, share_id):
        self.record_id = record_id
        self.uid = uid
        self.comment = comment
        self.like = like
        self.collect = collect
        self.share_id = share_id

        db.create_all()

    def __repr__(self):
        return "<user uid '{}'>".format(self.uid)

# 分享内容信息表


class Share(db.Model):
    id = db.Column(db.Integer, unique=True)
    share_id = db.Column(db.String(225), primary_key=True, unique=True)
    text = db.Column(LONGTEXT)  # 描述
    tag = db.Column(db.String(225))  # 标签
    share_time = db.Column(db.DateTime())  # 发布时间
    view_count = db.Column(db.Integer)  # 浏览次数
    comment_count = db.Column(db.Integer)  # 评论数
    like_count = db.Column(db.Integer)  # 点赞数
    collected_count = db.Column(db.Integer)  # 被收藏次数
    gps = db.Column(db.String(225))  # 位置信息
    pid = db.Column(db.String(225))  # 照片id
    vid = db.Column(db.String(225))  # 视频id

    def __init__(self, share_id, text, tag, share_time, view_count, comment_count, like_count, collected_count, gps, pid, vid):
        self.share_id = share_id
        self.text = text
        self.tag = tag
        self.share_time = share_time
        self.view_count = view_count
        self.comment_count = comment_count
        self.like_count = like_count
        self.collected_count = collected_count
        self.gps = gps
        self.pid = pid
        self.vid = vid

        db.create_all()

    def __repr__(self):
        return "<share id '{}'>".format(self.share_id)

# 照片信息表


class Photo(db.Model):

    __tablename__ = 'photos'

    id = db.Column(db.Integer, unique=True)
    pid = db.Column(db.String(225), primary_key=True, unique=True)
    psize = db.Column(db.String(225))  # 照片大小
    purl = db.Column(db.String(225))  # 照片的url

    def __init__(self, pid, psize, purl):
        self.pid = pid
        self.psize = psize
        self.purl = purl

        db.create_all()

    def __repr__(self):
        return "<photo id '{}'>".format(self.pid)

# 视频信息表


class Video(db.Model):

    __tablename__ = 'videos'

    id = db.Column(db.Integer, unique=True)
    vid = db.Column(db.String(225), primary_key=True, unique=True)
    vsize = db.Column(db.String(225))  # 视频大小
    vtime = db.Column(db.Time())  # 视频时长
    vurl = db.Column(db.String(225))  # 视频的url

    def __init__(self, vid, vsize, vtime, vurl):
        self.vid = vid
        self.vsize = vsize
        self.vtime = vtime
        self.vurl = vurl

        db.create_all()

    def __repr__(self):
        return "<video id '{}'>".format(self.vid)
