from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsPharmacistOrGO(BasePermission):

    def has_permission(self, request, view):
        user = request.user if request.user.is_authenticated else None
        return user.role == "PH" or user.role == "GO"


class ReadOnly(BasePermission):
    """Allow ReadOnly permissions if the request is a safe method"""

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsGovernmentAdmin(BasePermission):
    """ Allow only government admins to perform actions """

    def has_permission(self, request, view):
        user = request.user if request.user.is_authenticated else None
        return user.role == "GO"
