from import_export import resources

from subscriptions import models


class SubscriptionResource(resources.ModelResource):

    class Meta:
        model = models.Subscription
        fields = ('created', 'created_ip_address', 'email',)
        export_order = ('created', 'created_ip_address', 'email',)
