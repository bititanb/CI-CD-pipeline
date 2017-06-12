from django.conf import settings

def app_version(request):
    return {'app_version': settings.APP_VERSION}

def app_revision_short(request):
    return {'app_revision_short': settings.APP_REVISION_SHORT}

