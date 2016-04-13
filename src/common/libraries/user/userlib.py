import hashlib
from django.core import exceptions as django_exc
from rest_framework.status import HTTP_400_BAD_REQUEST
from src.common.helpers import validators
from src.common.libraries.constants import *
from src.common.models import User , Token
import requests

from src.common.models.permit import AdminPermission

class UserLib():

    def is_unique_email(self, email):
        if not User.objects.filter(email=email).exists():
           return True
        raise django_exc.ValidationError('email address already exists', code=HTTP_400_BAD_REQUEST)

    def add_user(self, user_details):
        response = dict()
        if self.is_unique_email(user_details[KEY_EMAIL_ID]):
            try:
                AddRequest =  User.objects.create(**user_details)
                return "User Added"
            except Exception as e:
                print e


    def login(self, request):
        token = request['auth']
        URL = 'https://www.googleapis.com/oauth2/v1/userinfo?access_token={0}'.format(token)
        data = requests.get(URL)
        data = data.json()
        email = data['email']
        try:
            user = User.objects.get(email=email)
            token, created = Token.objects.get_or_create(user=user)
            return (token. access_token, created)
        except Exception as e:
            print "Not A Valid Email"


    def add_permissions(self, permissions):
        permissions_id = AdminPermission.objects.create(**permissions)
        return permissions_id
