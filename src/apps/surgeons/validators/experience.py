from cerberus import Validator
from rest_framework.validators import ValidationError


POST_SCHEMA = {
    "data": {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'post': {'type': 'string'},
                'start_year': {'type': 'integer'},
                'end_year': {'type': 'integer'}
            }
        }
    }
}


def workplace_validator(value):
    json_data = {
        'data': value
    }
    
    v = Validator()
    
    if v.validate(json_data, POST_SCHEMA):
        raise ValidationError(v.errors)
    
