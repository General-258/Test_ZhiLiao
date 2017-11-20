# -*-coding:utf-8 -*-
import pymysql

class MySQLHelp(object):
    def __init__(self, host, port, user, password, database, charset):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.db = None
        self.curs = None

    #数据库连接
    def open(self):
        self.db = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                  database=self.database, charset=self.charset)
        self.curs = self.db.cursor()

    #数据库关闭
    def close(self):
        self.curs.close()
        self.db.close()

    #数据库增删改
    def cub(self,sql,params):
        self.open()
        try:
            self.curs.execute(sql, params)
            self.db.commit()
            print "OK"
        except :
            print "cud出现错误"
            self.db.rollback()  #回滚，撤销指定的sql语句，回滚到上一次的commit位置，只能用于：insert,update,delete
        self.close()

    #数据查询
    def find(self, sql, params):
        self.open()
        try:
            result = self.curs.execute(sql, params)
            self.close()
            print "查询成功"
            return result
        except :
            print "find出现错误"

if __name__=="__main__":
    my = MySQLHelp('127.0.0.1', 3306, 'root', '1234qwer', 'test', 'utf8')
    sql1 = "select * from student where name=%s"
    print my.find(sql1, 'tom')
    sql2 = "insert into student(name,class,age) values(%s,%s,%s)"
    my.cub(sql2, ('jin','3 year 2class',9))
