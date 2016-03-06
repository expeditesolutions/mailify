from django.conf.urls import url
from rest_framework import routers

from rest_api import views

router = routers.SimpleRouter()


router.register(r'(?P<version>1\.0)/subscriptions', views.SubscriptionViewSet, base_name='subscription')

urlpatterns = [
    url(r'^(?P<version>1\.0)/$', views.api_root),
] + router.urls
