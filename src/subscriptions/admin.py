from django.contrib import admin
from import_export.admin import ExportMixin

from subscriptions import models, resources


class SubscriptionAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('email', 'created', 'created_ip_address', 'sent_emails')
    search_fields = ('email', )
    ordering = ('-created', )
    readonly_fields = ('created', 'created_ip_address', 'sent_emails',)

    resource_class = resources.SubscriptionResource

    fieldsets = (
        (None, {
            'fields': (
                'email',
                'created',
                'created_ip_address',
                'sent_emails')
        }),
    )

    def get_actions(self, request):
        return

    def has_add_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        if change is False:
            obj.created_ip_address = request.META['REMOTE_ADDR']

        obj.save()


class VoucherAdmin(admin.ModelAdmin):
    list_display = ('code', )

    def get_actions(self, request):
        return []

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(models.Voucher, VoucherAdmin)
admin.site.register(models.Subscription, SubscriptionAdmin)
