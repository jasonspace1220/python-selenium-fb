import pymysql
 
class mysqlV2():

    def __init__(self,connect_config):
        connect_config['cursorclass'] = pymysql.cursors.DictCursor
        self.connect_config = connect_config


    def getAll(self):
        self.connect = pymysql.connect(**self.connect_config)
        self.cursor = self.connect.cursor()
        self.cursor.execute("SELECT * FROM fb_comment")
        data = self.cursor.fetchall()
        self.connect.close()

        return data
    
    def getPostUrlById(self,id):
        self.connect = pymysql.connect(**self.connect_config)
        self.cursor = self.connect.cursor()
        self.cursor.execute("SELECT * FROM fb_comment WHERE id ='" + id + "'")
        data = self.cursor.fetchone()
        self.connect.close()

        return data['post_url']

    def insertOne(self,fb_url_key,column,data):
        self.connect = pymysql.connect(**self.connect_config)
        # 使用 cursor() 方法建立一個指標物件 cursor
        self.cursor = self.connect.cursor()

        sql = "UPDATE fb_comment SET " + column + " ='" + data +"' WHERE fb_url_key ='"+ fb_url_key +"' "
        try:
            # 執行sql陳述式
            self.cursor.execute(sql)
            # 提交到資料庫執行
            self.connect.commit()
        except:
            # 發生錯誤時回滾
            self.connect.rollback()
        # 關閉資料庫連線
        self.connect.close()

        return

    def updateFBMessageOne(self,id,column,data):
        self.connect = pymysql.connect(**self.connect_config)
        # 使用 cursor() 方法建立一個指標物件 cursor
        self.cursor = self.connect.cursor()

        sql = "UPDATE fb_comment SET " + column + " ='" + data +"' WHERE id ='"+ id +"' "
        # try:
        # 執行sql陳述式
        self.cursor.execute(sql)
        # 提交到資料庫執行
        self.connect.commit()
        # except:
        #     # 發生錯誤時回滾
        #     print("Mysql儲存錯誤" , sql)
        #     self.connect.rollback()
        # 關閉資料庫連線
        self.connect.close()

        return