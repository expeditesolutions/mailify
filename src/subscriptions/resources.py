from import_export import resources

from subscriptions import models


class SubscriptionResource(resources.ModelResource):

    class Meta:
        model = models.Subscription
        fields = ('email', )
        export_order = ('email',)
