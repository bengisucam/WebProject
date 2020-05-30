from django.conf import settings
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from .models import User

class EmailBackend(User):

    def authenticate(self, username=None, password=None, **kwargs):
        print("in customer authenticate")
        UserModel = get_user_model()
        try:
            user = User.objects.get(email=username)
            print("email exists")
        except UserModel.DoesNotExist:
            print("email not exists")
            return None
        else:
            print("user password check")
            if user.check_password(password):
                print("password exists, and so user")
                return user
        return None



    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None