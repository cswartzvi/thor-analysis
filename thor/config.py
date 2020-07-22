"""Defines the YAML schema via Cerberus."""

bucket = {
    'type': 'dict',
    'schema': {
        'bucket': {'type': 'string'},
        'folder': {'type': 'string'},
        'files': {'type': 'list', 'schema': {'type': 'string'}}
    }
}

main_schema = {
    'path': {
        'type': 'dict',
        'schema': {
            'data_raw': {'type': 'string'},
            'data_intermediate': {'type': 'string'},
            'data_processed': {'type': 'string'},
            'logs': {'type': 'string'},
            'log_config': {'type': 'string'}
        }
    },
    # 'sources': {
    #     'type': 'list',
    #     'schema': {
    #         'type': 'dict',
    #         'schema': {
    #             'bucket': {'type': 'string'},
    #             'files': {'type': 'list', 'schema': {'type': 'string'}}
    #         }
    #     }
    #  },
    'sources': {
        'type': 'list', 'schema': bucket
     },
    'process': {
        'type': 'dict',
        'schema': {
            'operations': {'type': 'string'},
            'aircraft': {'type': 'string'},
            'weapons': {'type': 'string'},
        }
    }
}
