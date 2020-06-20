import json
import db
from User import User
from Upload import Upload
from Question import Question
from Result import Result

f=open('test_data.json',encoding='utf-8')
res = f.read()
data = json.loads(res) #加载json数据
#取出json中第一个学生的cases数据cases = data['3544']['cases']
#遍历学生对象
recordid = 0
for key,value in data.items():
    cases = value["cases"]
    userId = int(key)
    student = User(userId,0)
    pg_level = 0
    upload_num = 0
    sum_socre = 0
    sum_time = 0
    case_num = len(cases)
    for case in cases:
        caseId = int(case["case_id"])
        uploadlist = case["upload_records"]
        final_score = case["final_score"]
        up_num = len(uploadlist)
        cost_time = 0
        if(up_num>1):
             cost_time = (uploadlist[up_num-1]["upload_time"]-uploadlist[0]["upload_time"])/1000
        record = Result(recordid,caseId,userId,up_num,final_score,cost_time)
        recordid += 1
        db.insert_data(record)
        if(final_score>90):
            pg_level += 1
        upload_num += up_num
        sum_socre += final_score
        sum_time += cost_time

    # userdata ={'case_num':case_num,
    #            'pg_level':pg_level,
    #            'upload_num':upload_num,
    #            'average_score':sum_socre/case_num,
    #            'average_time':sum_time/case_num,
    #            'average_upnum':int(upload_num/case_num)}
    # db.updateUser(userId,userdata)


