from dotenv import dotenv_values

# NEVER HARDCODE YOUR CONFIGURATION IN YOUR CODE
# INSTEAD CREATE A .env FILE AND STORE IN IT
config = dotenv_values(".env")


class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = 'hvcEfKQRo6jQDF*4#bXhkjbZMkCIlGM48z9mCuS8tdeZ13e9$L'
    SQLALCHEMY_DATABASE_URI = f"postgresql://client_management_aa54_user:67sMfUo1xP3OPATIvOthUcDkMgfb9oJX@dpg-cfutbapmbjsj9amog15g-a.oregon-postgres.render.com/client_management_aa54"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

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
