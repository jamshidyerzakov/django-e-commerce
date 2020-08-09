import json

from braces.views import CsrfExemptMixin
from oauth2_provider.settings import oauth2_settings
from oauth2_provider.views.mixins import OAuthLibMixin
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_social_oauth2.oauth2_backends import KeepRequestCore
from rest_framework_social_oauth2.oauth2_endpoints import SocialTokenServer


class ConvertTokenView(CsrfExemptMixin, OAuthLibMixin, APIView):
    """
    Implements an endpoint to convert a provider token to an access token

    The endpoint is used in the following flows:

    * Authorization code
    * Client credentials
    """
    server_class = SocialTokenServer
    validator_class = oauth2_settings.OAUTH2_VALIDATOR_CLASS
    oauthlib_backend_class = KeepRequestCore
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        # Use the rest framework `.data` to fake the post body of the django request.
        request._request.POST = request._request.POST.copy()
        for key, value in request.data.items():
            request._request.POST[key] = value
        print("View:", request.__dict__, args, kwargs, sep="\n\n")
        url, headers, body, status = self.create_token_response(request._request)
        response = Response(data=json.loads(body), status=status)

        for k, v in headers.items():
            response[k] = v
        return response