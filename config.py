class Config:
    SECRET_KEY = '123456'

class DevConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
#    MYSQL_DB = 'csb'
    MYSQL_DB = 'csb_prov'


config = {
    'development': DevConfig,
}