class ConfigBase(object):
    MONGO_DBNAME = 'acs_nginx'

class Development(ConfigBase):
    pass

class Testing(ConfigBase):
    MONGO_HOST = 'mongo'
    DEBUG = True
    TESTING = True
    pass

class Production(ConfigBase):
    MONGO_HOST = 'mongo'
    pass

