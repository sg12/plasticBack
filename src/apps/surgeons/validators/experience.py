from cerberus import Validator
from django.core.exceptions import ValidationError


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


def experience_validator(value):
    json_data = {
        'data': value
    }
    
    v = Validator()
    
    if v.validate(json_data, POST_SCHEMA):
        raise ValidationError(v.errors)
    
