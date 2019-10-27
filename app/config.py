class Configuration(object):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dbuser:dbpass@localhost/dbmaps'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
