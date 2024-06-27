from rest_framework import permissions
from apps.user.models import Role


class IsDoctorOrClinic(permissions.BasePermission):    
    def has_permission(self, request, view):
        if request.method == permissions.SAFE_METHODS:
            return True
        
        is_doctor = request.user.role.name == Role.DOCTOR
        is_clinic = request.user.role.name == Role.CLINIC
        
        return is_doctor or is_clinic
