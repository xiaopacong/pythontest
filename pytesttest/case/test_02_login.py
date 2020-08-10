import requests
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import write_file,read_file

#测试登入成功
def test_01_login():
    u="http://192.144.148.91:2333/login"
    h={"Content-Type":"application/json"}
    d={
        "username":"huang300k",
        "password":"a12345828" 
        }
    res=requests.post(url=u,json=d,headers=h)


    #断言结果
    assert res.status_code==200
    assert res.json()["status"]==200    


    sql="select * from t_user where username='{}'".format(d["username"])
    assert len(query(sql))!=0

    #tooken保存
    token=res.json()["data"]["token"]
    write_file("user_token.txt",token)
    