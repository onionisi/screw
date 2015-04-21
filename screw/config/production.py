# Django settings for screw project.

DEBUG = False


MONGODB_USER = 'root'
MONGODB_PASSWD = 'root'
MONGODB_HOST = 'net'
MONGODB_NAME = 'screw'
MONGODB_DATABASE_HOST = \
       'mongodb://%s:%s@%s/%s' \
       % (MONGODB_USER, MONGODB_PASSWD, MONGODB_HOST, MONGODB_NAME)
