from rest_framework import generics
from rest_framework  import mixins
from rest_framework.status import HTTP_201_CREATED
from src.api.v1.libraries.permissions import AdminPortalPermissions
from src.api.v1.libraries.customresponse import CustomResponse
from src.api.v1.libraries.loggingmixin import LoggingMixin
from src.api.v1.serializers.usersserializer import UsersSerializer
from src.common.libraries.user.userlib import UserLib
from src.common.models.user import User
from src.common.libraries.constants import *
user_lib = UserLib()
from django_mysqlpool import auto_close_db
from src.common.helpers.Query2Dict import Query2DictConverter

'''
{
    "name": "Saurabh Pandey",
    "email": "saurabh.pandey@roder.in",
    "permissions" {
        "vendor_portal" : "read",
        "admin_portal": "read"
        }
}
'''

class AdminCheckView( LoggingMixin, generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):
    model = User
    serializer_class = UsersSerializer
    permission_classes = (AdminPortalPermissions, )

    @auto_close_db
    def get(self, request):

        return CustomResponse(message='User added', payload="Showing", code=HTTP_201_CREATED)

    @auto_close_db
    def post(self, request):

        return CustomResponse(message='User added', payload="Showing", code=HTTP_201_CREATED)


