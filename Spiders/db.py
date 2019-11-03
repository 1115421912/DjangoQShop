import pymysql

class DBManage(object):
    #初始化方法
    def __init__(self):
        try:
            self.conn = pymysql.connect('127.0.0.1', 'root', '123456', 'SShop', charset='utf8')
            self.cursor = self.conn.cursor()
        except:
            print('数据库连接异常')

    def save_item(self, item):
        #sql语法
        sql = "insert into buyer_shop(c_title, c_price, c_weight, c_CO, c_taste, c_classify, c_picture) values (%s, %s, %s, %s, %s, %s, %s)"

        #准备数据库
        date = (item.c_title, item.c_price, item.c_weight, item.c_CO, item.c_taste, item.c_classify, item.c_picture)

        #执行。
        self.cursor.execute(sql, date)

        #提交
        self.conn.commit()

    #对象回收
    def __del__(self):
        self.cursor.close()
        self.conn.close()
