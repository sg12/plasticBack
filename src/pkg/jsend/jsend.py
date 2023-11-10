import json


class Jsend:
    def __init__(self, indent: int = None):
        self.indent = indent

    def success(self, data: dict | list[dict]) -> str:
        data = {
            'status': 'success',
            'data': data
        }
        
        return json.dumps(data, indent=self.indent)
        
    def fail(self, data: str) -> str:
        data = {
            'status': 'fail',
            'data': data
        }
        
        return json.dumps(data, indent=self.indent)
        
    def error(self, message: str) -> str:
        message = {
            'status': 'error',
            'message': str(message)
        }
        
        return json.dumps(message, indent=self.indent)