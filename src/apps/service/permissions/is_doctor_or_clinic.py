from rest_framework import permissions
from apps.user.models import Role


class IsDoctorOrClinic(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_doctor = request.user.name == Role.DOCTOR
        is_clinic = request.user.type == Role.CLINIC
        return is_doctor or is_clinic
