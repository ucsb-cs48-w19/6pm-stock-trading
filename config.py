import os 
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    #Added for postgres hosting?
    DEBUG = False
    TESTING = False
    
    #^^^
    SECRET_KEY = os.environ.get('SECRET_KEY')

    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    #Change according to tutorial (medium.com)
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']





#Added for postgres hosting?
class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

#^^^
