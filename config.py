from dotenv import dotenv_values
config = dotenv_values(".env_sample")


class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    DEBUG = True
    SECRET_KEY = config['SECRET_KEY']

    SQLALCHEMY_DATABASE_URI = f"postgresql://{config['DB_USER']}:{config['DB_PASSWORD']}@{config['DB_HOST']}:{config['DB_PORT']}/{config['DB_NAME']}"


    SQLALCHEMY_TRACK_MODIFICATIONS = True

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 
    MAIL_PASSWORD = 

class TestingConfig(Config):
    TESTING = True
