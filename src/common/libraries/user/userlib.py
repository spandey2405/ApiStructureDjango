import hashlib
from django.core import exceptions as django_exc
from rest_framework.status import HTTP_400_BAD_REQUEST
from src.common.helpers import validators
from src.common.libraries.constants import *
from src.common.models import User , Token
from src.api.v1.serializers.usersserializer import UsersSerializer
from src.common.libraries.otp.otplib import OTPLib

otp_lib = OTPLib()

class UserLib():

    def password_hashing(self, password_hash, salt=None):
        if not salt:
            salt = User.objects.generate_salt()
        salted_client_hash = str(password_hash + salt)
        hash_library = hashlib.new(HASH_METHOD_USER_ADD)
        hash_library.update(salted_client_hash)
        server_hash = hash_library.hexdigest()
        return (server_hash, salt)

    def get_phoneno(self, email):
        return int(UsersSerializer(User.objects.get(email=email)).data[KEY_PHONE_NO])

    def is_unique_email(self, email):

        if not User.objects.filter(email=email).exists():
            return True
        elif User.objects.filter(email=email).exists() and self.get_phoneno(email) == 0:
            return False

        raise django_exc.ValidationError('email address already exists', code=HTTP_400_BAD_REQUEST)


    def add_user(self, user_details, ThirdParty=False):
        response = dict()
        if validators.validate_user_details(user_details) and  self.is_unique_email(user_details[KEY_EMAIL_ID]):
            user_details[KEY_PHONE_NO] = str(user_details[KEY_PHONE_NO])[-10:]
            server_hash, salt = self.password_hashing(user_details[KEY_PASSWORD_HASH])
            user_details[KEY_EMAIL_ID] = user_details[KEY_EMAIL_ID]
            user_details[KEY_USER_NAME] = user_details[KEY_USER_NAME]
            user_details[KEY_SALT] = salt
            user_details[KEY_PASSWORD_HASH] = server_hash
            AddRequest =  User.objects.create(**user_details)
            response['access_token'], created = self.authenticate_social_login(user_details[KEY_EMAIL_ID])
            response['otp-verified'] = 'false'
            return response

    def update_user(self, user, options):
        #@todo make it more dinymic so that authorized field can be updated on request

        update_user = User.objects.get(user_id=user)

        for key in options:
            value = options[key]
            if key == KEY_PHONE_NO:
                value = str(value)[-10:]
            setattr(update_user, key, value)

        update_user.save()

        return True

    def get_user(self, user, options):
        fields = (KEY_USER_ID, KEY_USER_NAME, KEY_EMAIL_ID, KEY_PHONE_NO)
        return UsersSerializer(user, fields=fields).data


    def authenticate_user(self, signin_details, ThirdParty=False):
        email = signin_details[KEY_EMAIL_ID]
        password_hash = signin_details[KEY_PASSWORD_HASH]
        validators.validate_signin_details(signin_details=signin_details)
        try:
            user = User.objects.get(email=email)
            print "success"
        except Exception as e:
            raise django_exc.ValidationError('Invalid Email Address', code=HTTP_400_BAD_REQUEST)
        hashed_salted_client_hash, salt = self.password_hashing(password_hash=password_hash, salt=user.salt)
        hash_stored_in_db = user.password_hash
        if hash_stored_in_db == hashed_salted_client_hash:
            token, created = Token.objects.get_or_create(user=user)
            return (token. access_token, created)
        raise django_exc.ValidationError('Invalid Password', code=HTTP_400_BAD_REQUEST)

    def authenticate_social_login(self,email):
        user = User.objects.get(email=email)
        token, created = Token.objects.get_or_create(user=user)
        return (token. access_token, created)





