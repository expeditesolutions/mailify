from rest_framework import serializers

from subscriptions import models


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Subscription
        fields = ('email', 'created', 'created_ip_address')
