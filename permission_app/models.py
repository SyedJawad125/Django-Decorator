from django.db import models

from chat_site.settings import AUTH_USER_MODEL

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    # role_added_by_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='role_added_by_user1', null=True, blank=True)
    # role_updated_by_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='role_updated_by_user1', null=True, blank=True)
    code_name = models.CharField(max_length=50)

class Permission(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    code = models.CharField(max_length=50)
    per_added_by_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='per_added_by_user1', null=True, blank=True)
    per_updated_by_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='per_updated_by_user1', null=True, blank=True)
    permission_has_role = models.ManyToManyField(Role, related_name='permission_has_role1', null=True, blank=True)

    # https://github.com/Afraheem/htms_backend/blob/master/api/views/hotel_detail_view.py

class Make(models.Model):
    name = models.CharField(max_length=100)