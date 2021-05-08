dialect = 'mysql'
driver = 'pymysql'
username = 'root'
password = 'youzc'
host = '127.0.0.1'
port = 3306
database = 'wise_eye'


SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4'.format(dialect, driver, username, password, host,port, database)

SQLALCHEMY_TRACK_MODIFICATIONS = False