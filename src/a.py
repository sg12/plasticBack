
class Path:
    def __init__(self, base_path):
        self._base_path = base_path
        
        
    def value(self):
        return self._base_path

    def __truediv__(self, other):
        # Объединение путей с помощью '/'
        return '/'.join([self._base_path] + other.split('/'))

    def __str__(self):
        # Возвращение пути в виде строки
        return self._base_path

PROFILE_URL = Path('profile').value
PROFILE_PK_URL = PROFILE_URL / '<int:user_pk>'
print()
