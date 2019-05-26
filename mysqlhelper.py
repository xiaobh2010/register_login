import pymysql

class MysqlHelper():
    def __init__(self,database,host='localhost',user='root',password='123456',charset='utf8'):
        self.database=database
        self.host=host
        self.user=user
        self.password=password
        self.charset=charset

    #定义open方法，创建两个对象
    def open(self):
        self.db=pymysql.connect(host=self.host,user=self.user,password=self.password,
            database=self.database,charset=self.charset)
        self.cursor=self.db.cursor()

    #定义close方法用来关闭两个对象
    def close(self):
        self.cursor.close()
        self.db.close()

    def execute_sql(self,sql,L=[]):
        #调用open函数，创建２个对象
        self.open()
        #执行sql命令
        self.cursor.execute(sql,L)
        self.db.commit()
        #调用close函数，关闭两个对象
        self.close() #上面定义的close函数

    #get_all方法，执行查询命令，返回查询结果
    def get_all(self,sql,L=[]):
        self.open()
        self.cursor.execute(sql,L)
        res=self.cursor.fetchall()
        #查询语句不用提交
        self.close()
        #将查询的最终结果返回
        return res
