import pkgutil

class ConfigBase(object):
    DEBUG = True
    MONGO_DBNAME = 'acs_nginx'

    DOMAIN = dict()

    # Loading dynamically the resources
    schemas_dir = 'schemas'
    for importer, package_name, _ in pkgutil.iter_modules([schemas_dir]):
        module = importer.find_module(package_name).load_module('%s' % (package_name))
        if hasattr(module, 'schema'):
            DOMAIN[package_name] = dict(
                schema = getattr(module, 'schema'),
                transparent_schema_rules = False,
                allow_unknown = False,
                soft_delete = False,
                datasource = {
                    'source': package_name
                }
                # location = False,
            )



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

