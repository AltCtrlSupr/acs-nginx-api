class ConfigBase(object):
    DEBUG = True
    MONGO_DBNAME = 'acs_nginx'

class Development(ConfigBase):
    pass

class Testing(ConfigBase):
    MONGO_DBNAME = 'acs_nginx_test'
    MONGO_HOST = 'mongo'
    TESTING = True
    pass

class Production(ConfigBase):
    MONGO_HOST = 'mongo'
    pass

