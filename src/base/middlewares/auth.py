import jwt
import logging
from typing import Dict, Tuple, List, Union

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.http import HttpRequest, JsonResponse
from django.conf import settings
from rest_framework import exceptions

from user.models import User

logger = logging.getLogger("django")


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    @staticmethod
    def get_user(data: Dict) -> Union[Tuple[User, List[Group]], object]:
        try:
            user, created = User.objects.get_or_create(username=data.get('username'))

            if created:
                user.is_superuser = data.get('is_superuser')
                user.first_name = data.get('first_name')
                user.last_name = data.get('last_name')
                user.is_staff = data.get('is_staff')
                user.is_active = data.get('is_active')
                user.email = data.get('email')
                user.is_new = True
                # user.date_joined = parser.isoparse(data.get('date_joined'))
                # if data.get('groups'):
                #     for group in data.get('groups'):
                #         group_obj, _ = Group.objects.get_or_create(name=group)
                #         group_obj.user_set.add(user)
                user.save()
            return user, user.groups
        except Exception as err:
            logger.error(f'error creating or retrieving user. reason: {err}')
            return

    def __call__(self, request: HttpRequest):
        import pdb; pdb.set_trace()
        authorization_header = request.headers.get("Authorization")

        # if not authorization_header:
        #     return None
        try:
            # header = 'Token xxxxxxxxxxxxxxxxxxxxxxxx'
            access_token = authorization_header.split(" ")[1]
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=["HS256"]
            )
            user_obj, groups = self.get_user(data=payload)

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("access_token expired")
        except IndexError:
            raise exceptions.AuthenticationFailed("Token prefix missing")

        user = User.objects.filter(id=payload["user_id"]).first()
        if user is None:
            raise exceptions.AuthenticationFailed("User not found")

        if not user.is_active:
            raise exceptions.AuthenticationFailed("user is inactive")

        # self.enforce_csrf(request)
        setattr(request, 'user', user_obj)
        response = self.get_response(request)
        return response
