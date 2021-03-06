from django.http import HttpResponseRedirect
from django.conf import settings
from administration.models import GlobalConfig
from re import compile

EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]

class LoginRequiredMiddleware:
    def process_request(self, request):
        if not request.user.is_authenticated():
            path = request.path_info.lstrip('/')
            if not any(m.match(path) for m in EXEMPT_URLS):
                return HttpResponseRedirect(settings.LOGIN_URL)

class SetGlobalConfig:
    def process_request(self, request):
        request.can_user_edit = GlobalConfig.objects.all()[0].can_user_edit
        return