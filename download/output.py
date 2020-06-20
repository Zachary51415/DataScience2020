from Result import Result
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
import numpy as np


#初始化数据库连接
engine = create_engine(
    "mysql+pymysql://root:root@localhost:3306/analysis",
    encoding="utf-8", echo=True)
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)
session = DBSession()
resList = session.query(Result).all()
upnum = []

df = pd.DataFrame(data= data,columns=['upnum','score'])
df.plot.scatter(x='score',y='upnum')
session.close()
# a = np.random.rand(50, 4)
# df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
#df.plot.scatter(x='a', y='b')

