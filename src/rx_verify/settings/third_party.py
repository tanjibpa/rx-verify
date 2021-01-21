REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.DjangoModelPermissions",
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "user.authentication.SafeJWTAuthentication",
    ),
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    # 'DEFAULT_PAGINATION_CLASS': 'base.helpers.CustomPagination',
    # 'PAGE_SIZE': 12,
    # 'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler'
}
