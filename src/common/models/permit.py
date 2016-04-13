from django.db import models
from src.common.libraries.constants import *
import binascii, os, uuid

class AdminPermissionManager(models.Manager):
    def generate_permitid(self):
        return str(uuid.uuid4())

class AdminPermission(models.Model):
    admin_permission_id = models.CharField(max_length=UID_LENGTH, primary_key=True, editable=False)
    vendor_portal = models.CharField(max_length=5, default="none")
    admin_portal = models.CharField(max_length=5, default="none")
    objects = AdminPermissionManager()

    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    def save(self, *args, **kwargs):
        if not self.admin_permission_id:
            self.admin_permission_id = AdminPermission.objects.generate_permitid()

        return super(AdminPermission, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.admin_permission_id

    class Meta:
        db_table = 'icab_admin_permissions'
        app_label = 'common'