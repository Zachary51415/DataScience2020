from sqlalchemy.dialects.mysql import INTEGER,VARCHAR,DOUBLE
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
Base =declarative_base()

class Question(Base):
    __tablename__ = 'question'

    id = Column(INTEGER, primary_key=True)
    ctype= Column(VARCHAR, nullable=False)
    zip = Column(VARCHAR,nullable=False)
    difficulty = Column(INTEGER)
    remark = Column(DOUBLE)
    average_score = Column(DOUBLE)
    average_time = Column(DOUBLE)
    average_upnum = Column(INTEGER)

    def __init__(self, id, ctype, zip):
        self.id = id
        self.ctype = ctype
        self.zip = zip


