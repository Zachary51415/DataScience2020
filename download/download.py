import json
import db
from User import User
from Upload import Upload
from Question import Question
import urllib.request,urllib.parse
import os

f=open('test_data.json',encoding='utf-8')
res = f.read()
data = json.loads(res) #加载json数据
#取出json中第一个学生的cases数据cases = data['3544']['cases']
#遍历学生对象
for key,value in data.items():
    cases = value["cases"]
    userId = int(key)
    student = User(userId,0)
#遍历做题信息
    for case in cases:
        caseId = int(case["case_id"])
        title = Question(caseId,case["case_type"],case["case_zip"])
        db.insert_data(title)
        for upload in case["upload_records"]:
            uploadId = int(upload["upload_id"])
            codeurl = upload["code_url"]
            if(len(codeurl) > 254):
                codeurl = codeurl[49:]
            record = Upload(uploadId, upload["upload_time"],userId,caseId,codeurl,upload["score"])
            db.insert_data(record)


#filename = urllib.parse.unquote(os.path.basename(case["case_zip"]))#获取文件名
#urllib.request.urlretrieve(urllib.parse.unquote(url),filename)#下载题目包到本地