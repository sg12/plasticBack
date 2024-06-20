from rest_framework import permissions
from apps.user.models import User, Role


class IsDoctorOrClinic(permissions.BasePermission):    
    def has_permission(self, request, view):
        user = None
        
        user_pk = view.kwargs.get('user_pk')
        if user_pk:
            user = User.objects.get(pk=user_pk)
        else:
            user = request.user
        
        if request.method == permissions.SAFE_METHODS:
            return True
        
        is_doctor = user.name == Role.DOCTOR
        is_clinic = user.type == Role.CLINIC
        
        return is_doctor or is_clinic
