from dotenv import dotenv_values

# NEVER HARDCODE YOUR CONFIGURATION IN YOUR CODE
# INSTEAD CREATE A .env FILE AND STORE IN IT
config = dotenv_values(".env")


class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    DEBUG = True
    SECRET_KEY = 'hvcEfKQRo6jQDF*4#bXhkjbZMkCIlGM48z9mCuS8tdeZ13e9$L'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///client.sqlite3'
    # SQLALCHEMY_DATABASE_URI = f"postgresql://client_management_gydc_user:jW4kRSa5DEBTs4baFbzs5dW76g3kDazS@dpg-cfuuefda499aogrk1qcg-a.oregon-postgres.render.com/client_management_gydc"
    # SQLALCHEMY_DATABASE_URI = f"postgresql://{config['DB_USER']}:{config['DB_PASSWORD']}@{config['DB_HOST']}:{config['DB_PORT']}/{config['DB_NAME']}"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:root@localhost:5432/client_management"

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'testing000123000@gmail.com'
    MAIL_PASSWORD = 'nyumktmwgceoaovl'

#
# class DevelopmentConfig(Config):
#     DEBUG = True
#     SECRET_KEY = 'hvcEfKQRo6jQDF*4#bXhkjbZMkCIlGM48z9mCuS8tdeZ13e9$L'
#
#     # database configuration
#     # SQLALCHEMY_DATABASE_URI = app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///client.sqlite3'
#     SQLALCHEMY_DATABASE_URI = f"postgresql://{config['DB_USER']}:{config['DB_PASSWORD']}@{config['DB_HOST']}:{config['DB_PORT']}/{config['DB_NAME']}"
#     SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(Config):
    TESTING = True
