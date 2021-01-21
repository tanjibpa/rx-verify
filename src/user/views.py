import jwt
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.conf import settings
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from user.serializers import UserSerializer
from user.utils import generate_access_token, generate_refresh_token


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def profile(request: Request) -> Response:
    user = request.user
    serialized_user = UserSerializer(user).data
    return Response({"user": serialized_user})


@api_view(["POST"])
@permission_classes([AllowAny])
# @ensure_csrf_cookie
def login_view(request: Request) -> Response:
    user_model = get_user_model()
    print(request)
    username = request.data.get("username")
    password = request.data.get("password")
    response = Response()
    if (username is None) or (password is None):
        raise exceptions.AuthenticationFailed("username and password required")

    user = user_model.objects.filter(username=username).first()
    if user is None:
        raise exceptions.AuthenticationFailed("user not found")
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed("wrong password")

    serialized_user = UserSerializer(user).data

    access_token = generate_access_token(user)
    refresh_token = generate_refresh_token(user)

    response.set_cookie(key="refreshtoken", value=refresh_token, httponly=True)
    response.data = {
        "access_token": access_token,
        "user": serialized_user,
    }

    return response


@api_view(["POST"])
@permission_classes([AllowAny])
@csrf_protect
def refresh_token_view(request):
    user_model = get_user_model()
    print(request.COOKIES)
    refresh_token = request.COOKIES.get("refreshtoken")
    if refresh_token is None:
        raise exceptions.AuthenticationFailed(
            "Authentication credentials were not provided."
        )
    try:
        payload = jwt.decode(
            refresh_token, settings.REFRESH_TOKEN_SECRET, algorithms=["HS256"]
        )
    except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed(
            "expired refresh token, please login again."
        )

    user = user_model.objects.filter(id=payload.get("user_id")).first()
    if user is None:
        raise exceptions.AuthenticationFailed("User not found")

    if not user.is_active:
        raise exceptions.AuthenticationFailed("user is inactive")

    access_token = generate_access_token(user)
    return Response({"access_token": access_token})
