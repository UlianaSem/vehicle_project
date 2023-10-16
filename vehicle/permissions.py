from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrStaff(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_authenticated

        if request.method in ('PUT', 'PATCH', 'DELETE'):
            return request.user == view.get_object().owner or request.user.is_staff

        if request.method in SAFE_METHODS:
            return request.user.is_authenticated
