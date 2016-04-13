from src.api.v1.serializers.dynamicfieldmodelserializer import DynamicFieldsModelSerializer
from src.common.libraries.constants import *
from src.common.models.permit import AdminPermission
from rest_framework import serializers

class PermissionsSerializer(DynamicFieldsModelSerializer):
# class UsersSerializer(serializers.ModelSerializer):
    """
    Serializing all the Users
    """
    class Meta:
        model = AdminPermission
        fields = (
            KEY_ADMIN_PORTAL,
            KEY_VENDOR_PORTAL
        )

