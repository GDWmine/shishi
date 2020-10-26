import pymysql

def du(sql):
    #数据库连接
    db = pymysql.connect (host="rm-2ze1t1stn33i3e936co.mysql.rds.aliyuncs.com",user="jrp_test",password="Jinbo123456",db="jrp1020")
    # 游标
    cursor = db.cursor()
    cursor.execute(sql)
    # 查询数据库返回
    res = cursor.fetchall() 
    db.close()
    return res

def xie(sql):
    #数据库连接
    db = pymysql.connect (host="rm-2ze1t1stn33i3e936co.mysql.rds.aliyuncs.com",user="jrp_test",password="Jinbo123456",db="jrp1020")
    # 游标
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        # 更新数据库提交
        db.commit()
    except:
        db.rollback()
    db.close()
