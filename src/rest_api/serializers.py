from rest_framework import serializers

from subscriptions import models


class SubscriptionSerializer(serializers.ModelSerializer):

    voucher = serializers.SerializerMethodField()

    class Meta:
        model = models.Subscription
        fields = ('email', 'created', 'created_ip_address', 'voucher')

    def get_voucher(self, obj):
        """
        Returns current voucher code
        """
        return models.Voucher.get_code()
