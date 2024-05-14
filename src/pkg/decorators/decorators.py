from apps.user.models import Role
from django.utils.decorators import method_decorator
from .compare_role import compare_role
from .or_compare_role import or_compare_role


is_client = method_decorator(compare_role(Role.CLIENT), name='dispatch')
is_doctor = method_decorator(compare_role(Role.DOCTOR), name='dispatch')
is_clinic = method_decorator(compare_role(Role.CLINIC), name='dispatch')
is_doctor_or_clinic = method_decorator(or_compare_role(Role.DOCTOR, Role.CLINIC), name='dispatch')
