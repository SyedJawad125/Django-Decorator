from rest_framework.exceptions import PermissionDenied
from .models import Role


def permission_required(permissions):
    def decorator(drf_custom_method):
        def _decorator(self, *args, **kwargs):
            if Role.objects.filter(id=self.request.user.role.pk, permissions__code__in=permissions).exists():
                return drf_custom_method(self, *args, **kwargs)
            else:
                raise PermissionDenied()
        return _decorator
    return decorator

