from User import User
from Upload import Upload
from Question import Question
from Result import Result
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def insert_data(data):
    # 初始化数据库连接
    engine = create_engine(
        "mysql+pymysql://root:root@localhost:3306/analysis",
        encoding="utf-8",echo=True)
    # 创建DBSession类型
    DBSession = sessionmaker(bind=engine)

    # 创建session对象
    session = DBSession()
    newData = query_data(data)
    if(len(newData)==0):
        # 插入单条数据,添加到session
        session.add(data)
        # 提交即保存到数据库
        session.commit()
    # 关闭session
    session.close()

def query_data(data):
    # 初始化数据库连接
    engine = create_engine(
        "mysql+pymysql://root:root@localhost:3306/analysis",
        encoding="utf-8", echo=True)
    # 创建DBSession类型
    DBSession = sessionmaker(bind=engine)
    # 创建session对象
    session = DBSession()

    if isinstance(data,User):
        newData = session.query(User).filter(User.id == data.id).all()
    elif isinstance(data,Question):
        newData = session.query(Question).filter(Question.id == data.id).all()
    elif isinstance(data, Upload):
        newData = session.query(Upload).filter(Upload.id == data.id).all()
    elif isinstance(data, Result):
        newData = session.query(Result).filter(Result.id == data.id).all()
    # 提交即保存到数据库
    session.commit()
    # 关闭session
    session.close()
    return newData

def updateUser(userID,data):
    engine = create_engine(
        "mysql+pymysql://root:root@localhost:3306/analysis",
        encoding="utf-8", echo=True)
    # 创建DBSession类型
    DBSession = sessionmaker(bind=engine)

    # 创建session对象
    session = DBSession()
    session.query(User).filter(User.id == userID).update({
        User.pg_level: data["pg_level"],
        User.upload_num: data["upload_num"],
        User.case_num: data["case_num"],
        User.average_score: data["average_score"],
        User.average_time: data["average_time"],
        User.average_upnum: data["average_upnum"]
    })
    session.commit()
    # 关闭session
    session.close()

