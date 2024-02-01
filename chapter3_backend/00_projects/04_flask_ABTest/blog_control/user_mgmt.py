from flask_login import UserMixin
from db_model.mysql import conn_mysqldb


class User(UserMixin):

    def __init__(self, user_id, user_email, blog_id):
        self.id = user_id
        self.user_email = user_email
        self.blog_id = blog_id

    def get_id(self):
        return str(self.id)

    @staticmethod
    def get(user_id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM user_info WHERE USER_ID = '" + \
            str(user_id) + "'"
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            db_cursor.close()
            return None

        user = User(user_id=user[0], user_email=user[1], blog_id=user[2])
        db_cursor.close()
        return user

    @staticmethod
    def find(user_email): # db에서 유저의 이메일이 있는지 찾는 메서드
        mysql_db = conn_mysqldb() 
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM user_info WHERE USER_EMAIL = '" + \
            str(user_email) + "'"
        db_cursor.execute(sql)
        user = db_cursor.fetchone() # db에서 유저가 입력한 이메일 정보를 가져옴
        if not user: # 이메일이 없다면 None 리턴
            db_cursor.close()
            return None 

        print(user) # db에
        user = User(user_id=user[0], user_email=user[1], blog_id=user[2])
        db_cursor.close()
        return user 

    @staticmethod
    def create(user_email, blog_id): # 이메일과 blog_id로
        user = User.find(user_email) # 해당 이메일이 db에 있는지 확인
        if user == None: # 해당 이메일이 없다면 db에 새로 넣음
            mysql_db = conn_mysqldb()
            db_cursor = mysql_db.cursor()
            sql = "INSERT INTO user_info (USER_EMAIL, BLOG_ID) VALUES ('%s', '%s')" % (
                str(user_email), str(blog_id))
            db_cursor.execute(sql)
            mysql_db.commit()
            return User.find(user_email) # 새로 받은 이메일 리턴
        else: # 해당 이메일이 있다면 이메일 리턴
            return user

    @staticmethod
    def delete(user_id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "DELETE FROM user_info WHERE USER_ID = %d" % (user_id)
        deleted = db_cursor.execute(sql)
        mysql_db.commit()
        return deleted
