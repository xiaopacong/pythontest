import requests
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import write_file,read_file

# def test_01_xgtx():
#     u="http://192.144.148.91:2333/updateuserheadpic"
#     h={
#         "Content-Type":"application/json", 
#         "token":read_file("user_token.txt") 
#     }
#     d={"ximg" :"头像.jpg"}
#     res=requests.post(url=u,json=d,headers=h)

#     #断言结果
#     assert res.status_code==200
#     assert res.json()["status"]==200 
    
#     sql="select * from t_user where username)"

def test_01_xwz():
    u="http://192.144.148.91:2333/article/new"
    h={
        "Content-Type":"application/json",
        "token":read_file("user_token.txt")
        }
    d= {
        "title":"为什么要学习测试",
        "content":"内容", 
        "tags":"测试1234", 
        "brief":"介绍", 
        "ximg":"dsfsdf.jpg" 
        }  

    res=requests.post(url=u,json=d,headers=h)
    print(res)


    #断言
    assert res.status_code==200
    assert res.json()["status"]==200

    sql="select * from t_article where id='{}'".format(res.json()["data"]["articleid"]) 
    assert len(query(sql)) !=0

