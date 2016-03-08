from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_api import serializers
from project.authentication import CsrfExemptSessionAuthentication
from subscriptions import models


@api_view(('GET',))
def api_root(request, version, format=None):
    return Response({
        'version': '1.0',
        'subscriptions': reverse('rest_api:subscription-list', request=request, kwargs={'version': version}),
    })


class SubscriptionViewSet(CreateModelMixin,
                          viewsets.GenericViewSet):
    queryset = models.Subscription.objects.all()
    serializer_class = serializers.SubscriptionSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, )

    def perform_create(self, serializer):
        already_exists = self.queryset.filter(email=serializer.validated_data['email']).count() > 0

        if not already_exists:
            subscription = serializer.save(created_ip_address=self.request.META['REMOTE_ADDR'])
        else:
            subscription = self.queryset.get(email=serializer.validated_data['email'])

        # always notify!
        subscription.notify()
