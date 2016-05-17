schema = {
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 255,
        'required': True,
        # 'unique': True,
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
    },
    'virtual_host_alias': {
	'type': 'objectid',
        'data_relation': {
            'resource': 'virtual_host_alias',
            'field': '_id',
            'embeddable': True
        }
    },
}

