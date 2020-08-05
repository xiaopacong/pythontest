#注册
from dbtools import query,commit

username=input("请输入账号:")
password=input("输入密码：")

sql='insert into t_pymysql_account values(null,"{}","{}")'.format(username,password)
print(sql)
commit(sql)