from flask_expects_json import expects_json

settings_schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'logo': {'type': 'string'},
        'slider': {'type': 'string'},
        'text': {'type': 'string'},
        'last_actualization': {'type': 'float'}
    }
}

actions_schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'date': {'type': 'float'},
        'photo': {'type': 'string'},
        'text': {'type': 'string'}
    }
}

news_schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'date': {'type': 'float'},
        'photo': {'type': 'string'},
        'text': {'type': 'string'}
    }
}
