import requests
from dbtools import query
#练习get自动化
#接口地址
# u="http://192.144.148.91:2333/get_title_img"
# res=requests.get(u)
# print(res.text)


#练习post接口请求
u="http://192.144.148.91:2333//login"     #接口地址
d={
"username":"huang163k",
"password":"a12345691"
}                                         #接口参数
res=requests.post(url=u,json=d)
print(res.text)


#断言判断状态码和结果码
assert res.status_code==200
assert res.json()["status"]==200


#数据库操作 断言判断登入的账号存在数据库中
sql="select * from t_user where username='{}'".format(d["username"])
query(sql)




