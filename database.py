import pymysql

class Database:
    def __init__(self):
        self.connection = None
        self.connect()

    def connect(self):
        # Подключение к БД
        try:
            self.connection = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                database='demoDB',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except Exception as e:
            self.connect = None

    def get_user(self, login, password):
        # Проверка пользователя при входе
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT id_user, role, full_name FROM user WHERE login=%s AND password=%s"
                cursor.execute(sql, (login, password))
                result = cursor.fetchone()

                return result
        except Exception as e:
            return None
    
    def close(self):
        # Закрытие соединения
        if self.connection:
            self.connection.close()
            self.connection = None