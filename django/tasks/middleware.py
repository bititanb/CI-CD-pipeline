from threading import local
from django.utils.deprecation import MiddlewareMixin

_current_user = local()

class CurrentUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        _current_user.value = request.user

def get_current_user():
    return _current_user.value
