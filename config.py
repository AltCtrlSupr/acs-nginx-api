class ConfigBase(object):
    MONGO_DBNAME = 'acs_nginx'

class Development(ConfigBase):
    pass

class Testing(ConfigBase):
    pass

class Production(ConfigBase):
    pass

