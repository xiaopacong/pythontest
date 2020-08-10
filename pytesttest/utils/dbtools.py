# 导入pymysql  为了连接mysql数据库而存在的
import pymysql

def query(sql):
    """
        查询mysql数据库：只能用造select，不能delete update insert
    """
    # 连接数据库 固定的，只需要变参数
    db = pymysql.connect(host="192.144.148.91", user="ljtest", password="123456", db="ljtestdb")
    cur = db.cursor()    # 获取游标：查询窗口
    cur.execute(sql)     # 指定sql语句
    res = cur.fetchall() # 获取执行的结果
    db.close()

    return res

# sql = "select * from t_user where id=272"
# r = query(sql)
# print(r)

def commit(sql):
    """
        增加/删除/修改方法：delete update insert不要传select
    """
    db = pymysql.connect(host="192.144.148.91", user="ljtest", password="123456", db="ljtestdb")
    cur = db.cursor()    # 获取游标：查询窗口
    cur.execute(sql)     # 指定sql语句
    db.commit()          # 提交修改
    db.close()

# sql = 'update t_user set username="zyhf" where id=272'
# commit(sql)
# sql = "select * from t_user where id=272"
# r = query(sql)
# print(r)