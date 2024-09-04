from rest_framework.permissions import BasePermission
from django.conf import settings

class HasSecretKey(BasePermission):
    def has_permission(self, request, view):
        # Check for the 'X-Secret-Key' header in the request
        secret_key = request.headers.get('X-Secret-Key')

        # Compare it with the secret key stored in Django settings
        return secret_key == settings.SECRET_KEY
