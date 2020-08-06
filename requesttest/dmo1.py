#导入requests
import requests
from dbtools import query

# u="http://192.144.148.91:2333/get_title_img"  #接口地址
# res = requests.get(u)   #使用get方法请求地址   返回值保存在res中，
# print(res.text)  #打印返回值   res.text就是返回值


u="http://192.144.148.91:2333/login"
d={
"username":"huang163k",
"password":"a12345691" 
}
res=requests.post(url=u,json=d)
print(res.text)

#判断http状态码和结果码
assert res.status_code ==200  #状态码
assert res.json()["status"]==200   #结果码   res.json()是为了把res字符串类型转换成字典
# print("测试通过！")


#判断数据自动查询功能
sql="select * from t_user where username='{}'".format(d["username"])
res=query(sql)
assert len(res)!=0
print("测试通过！")