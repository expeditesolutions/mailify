from django.conf import settings
from django.conf.urls import include, url
from django.http import HttpResponse
from django.views.generic import RedirectView
from django.contrib import admin


urlpatterns = [
    url(r'^robots.txt$', lambda r: HttpResponse('User-agent: *\nDisallow: /', content_type='text/plain')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('rest_api.urls', namespace='rest_api')),
    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.FAVICON_PATH, permanent=True), name='favicon'),
]
