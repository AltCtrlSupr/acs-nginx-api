from eve.io.mongo.validation import Validator
from eve.utils import config

"""
    Based on eve.io.mongo.validation by Nicola Iarocci

    :copyright: (c) 2016 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""

class Validator(Validator):

    def __init__(self, schema=None, resource=None, allow_unknown=False,
                 transparent_schema_rules=False):
        super(Validator, self).__init__(schema)
