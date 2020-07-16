"""Defines the YAML schema via Cerberus."""

main_schema = {
    'path': {
        'type': 'dict',
        'schema': {
            'data_raw': {'type': 'string'},
            'data_processed': {'type': 'string'},
            'logs': {'type': 'string'},
            'log_config': {'type': 'string'}
        }
    },
    'source': {
        'type': 'dict',
        'schema': {
            'bucket': {'type': 'string'},
            'files': {'type': 'list', 'schema': {'type': 'string'}}
        }
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
