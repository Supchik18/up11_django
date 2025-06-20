from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

class CustomCategoryPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.method == 'GET':
            return True
        perms_map = {
            'GET': ['manager.view_category'],
            'POST': ['manager.add_category'],
            'PUT': ['manager.change_category'],
            'PATCH': ['manager.change_category'],
            'DELETE': ['manager.delete_category'],
        }

        required_perms = perms_map.get(request.method, [])
        if not required_perms:
            return False
        return request.user.has_perms(required_perms)

class CustomManufacturerPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.method == 'GET':
            return True
        perms_map = {
            'GET': ['manager.view_manufacturer'],
            'POST': ['manager.add_manufacturer'],
            'PUT': ['manager.change_manufacturer'],
            'PATCH': ['manager.change_manufacturer'],
            'DELETE': ['manager.delete_manufacturer'],
        }
        required_perms = perms_map.get(request.method, [])
        if not required_perms:
            return False
        return request.user.has_perms(required_perms)

class CustomMaterialPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.method == 'GET':
            return True
        perms_map = {
            'GET': ['manager.view_material'],
            'POST': ['manager.add_material'],
            'PUT': ['manager.change_material'],
            'PATCH': ['manager.change_material'],
            'DELETE': ['manager.delete_material'],
        }
        required_perms = perms_map.get(request.method, [])
        if not required_perms:
            return False
        return request.user.has_perms(required_perms)

class CustomProductPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.method == 'GET':
            return True
        perms_map = {
            'GET': ['manager.view_product'],
            'POST': ['manager.add_product'],
            'PUT': ['manager.change_product'],
            'PATCH': ['manager.change_product'],
            'DELETE': ['manager.delete_product'],
        }
        required_perms = perms_map.get(request.method, [])
        if not required_perms:
            return False
        return request.user.has_perms(required_perms)

class CustomCustomerPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        perms_map = {
            'GET': ['manager.view_customer'],
            'POST': ['manager.add_customer'],
            'PUT': ['manager.change_customer'],
            'PATCH': ['manager.change_customer'],
            'DELETE': ['manager.delete_customer'],
        }
        required_perms = perms_map.get(request.method, [])
        if not required_perms:
            return False
        return request.user.has_perms(required_perms)

class CustomOrderPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.method == 'GET':
            return True
        perms_map = {
            'GET': ['manager.view_order'],
            'POST': ['manager.add_order'],
            'PUT': ['manager.change_order'],
            'PATCH': ['manager.change_order'],
            'DELETE': ['manager.delete_order'],
        }
        required_perms = perms_map.get(request.method, [])
        if not required_perms:
            return False
        return request.user.has_perms(required_perms)

class CustomOrderItemPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.method == 'GET':
            return True
        perms_map = {
            'GET': ['manager.view_orderitem'],
            'POST': ['manager.add_orderitem'],
            'PUT': ['manager.change_orderitem'],
            'PATCH': ['manager.change_orderitem'],
            'DELETE': ['manager.delete_orderitem'],
        }
        required_perms = perms_map.get(request.method, [])
        if not required_perms:
            return False
        if request.method == 'GET':
            return True
        return request.user.has_perms(required_perms)

class CustomReviewPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.method == 'GET':
            return True
        perms_map = {
            'GET': ['manager.view_review'],
            'POST': ['manager.add_review'],
            'PUT': ['manager.change_review'],
            'PATCH': ['manager.change_review'],
            'DELETE': ['manager.delete_review'],
        }
        required_perms = perms_map.get(request.method, [])
        if not required_perms:
            return False
        return request.user.has_perms(required_perms)
