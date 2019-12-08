import jwt
from django.conf import settings

from rest_framework import authentication, exceptions
from .models import User


class JWTAuthentication(authentication.BaseAuthentication):
    auth_header_prefix = "Bearer".lower()

    def authenticate(self, request):
        """
        This method will be called everytime an endpoint is accessed.
        This method can return 'None' when we want authentication to
        fail, for example when no authentication credentials are provided.
        It can also return `(user, token)` when authentication is successful.
        If we encounter an error, we raise an `AuthenticationFailed` error.
        """
        request.user = None

        # we need the auth_header, which should be a list containing two
        # elements: 1) the name of the authentication header ('Bearer' in our
        # case) and 2) the JWT token.
        auth_header = authentication.get_authorization_header(request).split()
        if not auth_header:
            # Don't authenticate if no header is provided
            return None

        if len(auth_header) == 1:
            return None

        elif len(auth_header) > 2:
            # Invalid token header. The length must be 2. Do not attempt
            # to authenticate
            return None

        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if prefix.lower() != self.auth_header_prefix:
            return None

        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):
        """
        We will try to authenticate the token. If authentication is successful
        we return (user, token), otherwise we return an `AuthenticationFailed`
        error.
        """

        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except jwt.ExpiredSignatureError:
            msg = "Your token has expired, please login in again"
            raise exceptions.AuthenticationFailed(msg)

        except Exception as e:
            msg = str(e)
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = User.objects.get(pk=payload['id'])
        except User.DoesNotExist:
            msg = "user was not found"
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = "Forbidden!This user has been deactivated"
            raise exceptions.AuthenticationFailed(msg)

        return (user, token)
