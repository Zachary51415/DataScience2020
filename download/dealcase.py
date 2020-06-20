import db
from Question import Question
from Result import Result
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import numpy as np
import math
engine = create_engine(
    "mysql+pymysql://root:root@localhost:3306/analysis",
    encoding="utf-8", echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()
caseList = session.query(Question).all()

typeDif = {'排序算法':92.92,'查找算法':87.24,
            '图结构':76.91,'树结构':82.10,'数字操作':91.08,
            '字符串':84.36,'线性表':91.90,'数组':88.75,}
for caseItem in caseList:
    caseId = caseItem.id
    remark = typeDif[caseItem.ctype]
    resList = session.query(Result).filter(Result.case_id == caseId).all()

    scoreList =[]
    timeList = []
    upnumList = []
    for result in resList:
        scoreList.append(float(result.final_score))
        timeList.append(float(result.cost_time/60))
        upnumList.append(result.up_num)
    score = np.asarray(scoreList)
    costtime = np.asarray(timeList)
    npnum = np.asarray(upnumList)

    difficulty = math.ceil(remark - math.ceil(np.mean(score)))
    if difficulty<0:
        difficulty = 0
    session.query(Question).filter(Question.id == caseId).update({
        Question.difficulty: difficulty,
        Question.remark: remark,
        Question.average_score: float(np.mean(score)),
        Question.average_time: float(np.median(costtime)),
        Question.average_upnum: int(np.median(npnum))
    })
    session.commit()

session.close()
