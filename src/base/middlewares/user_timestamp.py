from django.contrib.auth.models import AnonymousUser
from django.core.handlers.wsgi import WSGIRequest

from user.models import User


class UserTimestampMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: WSGIRequest):
        # setattr(request, '_dont_enforce_csrf_checks', True)
        if request.method in ["POST", "PUT", "DELETE"] and isinstance(
            request.user, User
        ):
            # setattr(
            #     request.data,
            #     "created_by",
            #     {
            #         "username": request.user.username,
            #         "first_name": request.user.first_name,
            #         "last_name": request.user.last_name,
            #         "email": request.user.email,
            #     },
            # )
            request.data["created_by"] = {
                "username": request.user.username,
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
                "email": request.user.email,
            }
        # import pprint
        # pp = pprint.PrettyPrinter(indent=2)
        # pp.pprint(request.__dict__)
        print(request.__dict__)
        response = self.get_response(request)
        return response
