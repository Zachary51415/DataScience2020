from sqlalchemy.dialects.mysql import INTEGER,DOUBLE
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
Base =declarative_base()

class Result(Base):
    __tablename__ = 'result'

    id = Column(INTEGER, primary_key=True)
    question_id = Column(INTEGER, nullable=False)
    user_id = Column(INTEGER, nullable=False)
    up_num = Column(INTEGER)
    final_score = Column(DOUBLE)
    cost_time = Column(DOUBLE)

    def __init__(self, id, question_id, user_id,up_num,final_score,cost_time):
        self.id = id
        self.question_id = question_id
        self.user_id = user_id
        self.up_num = up_num
        self.final_score = final_score
        self.cost_time = cost_time


