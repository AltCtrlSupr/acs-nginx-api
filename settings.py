# Enabling DEBUG
DEBUG = True

# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
# MONGO_USERNAME = 'user'
# MONGO_PASSWORD = 'user'
MONGO_DBNAME = 'apitest'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# Defining schema
schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 255,
        'required': True,
        'unique': True,
    },
    'ssl_cert': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 255,
        'required': False,
    },
    'ssl_key': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 255,
        'required': False,
    },
    'ssl_chain': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 255,
        'required': False,
    },
    'ports_plain': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 255,
        'required': False,
    },
    'ports_ssl': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 255,
        'required': False,
    }
}

virtual_host = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'virtual_host',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'name'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': schema
}

# Schemas
DOMAIN = {'virtual_host': virtual_host}

