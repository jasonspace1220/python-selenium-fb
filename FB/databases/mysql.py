import pymysql
 
class mysql():

    def __init__(self):
        self.connect_config = {
        'host':'35.229.132.93',
        'port':3306,
        'user':'jwarrant',
        'password':'jasongod',
        'database':'jwarrant',
        'charset':'utf8mb4',
        'cursorclass':pymysql.cursors.DictCursor,
        }


    def getAll(self):
        self.connect = pymysql.connect(**self.connect_config)
        # 使用 cursor() 方法建立一個指標物件 cursor
        self.cursor = self.connect.cursor()
        # # 使用 execute()  方法執行 SQL 搜尋 
        self.cursor.execute("SELECT * FROM pytest")
        # 使用 fetchone() 方法取得單條資料.
        data = self.cursor.fetchall()
        # 關閉資料庫連線
        self.connect.close()

        return data
    
    def getCount(self):
        self.connect = pymysql.connect(**self.connect_config)
        # 使用 cursor() 方法建立一個指標物件 cursor
        self.cursor = self.connect.cursor()
        # # 使用 execute()  方法執行 SQL 搜尋 
        self.cursor.execute("SELECT * FROM pytest")
        # 使用 fetchone() 方法取得單條資料.
        data = self.cursor.fetchall()
        # 關閉資料庫連線
        self.connect.close()

        return len(data)
    
    def getFBKey(self):
        self.connect = pymysql.connect(**self.connect_config)
        # 使用 cursor() 方法建立一個指標物件 cursor
        self.cursor = self.connect.cursor()
        # # 使用 execute()  方法執行 SQL 搜尋 
        self.cursor.execute("SELECT fb_url_key FROM pytest")
        # 使用 fetchone() 方法取得單條資料.
        data = self.cursor.fetchall()
        # 關閉資料庫連線
        self.connect.close()

        returnData = []
        for row in data:
            returnData.append(row['fb_url_key'])

        return returnData

    def insertOne(self,fb_url_key,column,data):
        self.connect = pymysql.connect(**self.connect_config)
        # 使用 cursor() 方法建立一個指標物件 cursor
        self.cursor = self.connect.cursor()

        sql = "UPDATE pytest SET " + column + " ='" + data +"' WHERE fb_url_key ='"+ fb_url_key +"' "
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

    def getFBMessageUrlsById(self,id):
        self.connect = pymysql.connect(**self.connect_config)
        self.cursor = self.connect.cursor()
        self.cursor.execute("SELECT url FROM fb_message WHERE id = " + id)
        data = self.cursor.fetchone()
        self.connect.close()

        # returnData = []
        # for row in data:
        #     returnData.append(row['url'])

        return data['url']

    def getFBMessageCount(self):
        self.connect = pymysql.connect(**self.connect_config)
        self.cursor = self.connect.cursor()
        self.cursor.execute("SELECT url FROM fb_message")
        data = self.cursor.fetchall()
        self.connect.close()

        return len(data)

    def updateFBMessageOne(self,url,column,data):
        self.connect = pymysql.connect(**self.connect_config)
        # 使用 cursor() 方法建立一個指標物件 cursor
        self.cursor = self.connect.cursor()

        sql = "UPDATE fb_message SET " + column + " ='" + data +"' WHERE url ='"+ url +"' "
        # sql = """UPDATE fb_message SET %s = %s WHERE url = %s""" 
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