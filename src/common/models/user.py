from django.db import models
from src.common.libraries.constants import *
import binascii, os, uuid

class UserManager(models.Manager):
    def generate_userid(self):
        return str(uuid.uuid4())

    def generate_salt(self):
        return binascii.hexlify(os.urandom(SALT_LENGTH/2)).decode()

class User(models.Model):
    email = models.EmailField(max_length=MAX_EMAIL_LENGTH, unique=True)
    user_id = models.CharField(max_length=UID_LENGTH, primary_key=True, editable=False)
    vendors_portal = models.IntegerField(default=0)
    admin_portal = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def is_authenticated(self, admin_portal=None):

        if admin_portal:
            return self.admin_portal
        #
        # if vendors_portal:
        #     return self.vendors_portal

        return True

    def save(self, *args, **kwargs):

        if not self.user_id:
            self.user_id = User.objects.generate_userid()

        return super(User, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user_id

    class Meta:
        db_table = 'icab_admin'
        app_label = 'common'