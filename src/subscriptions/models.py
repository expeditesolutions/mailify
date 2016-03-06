from django.db import models


class Subscription(models.Model):
    created = models.DateTimeField(editable=False, auto_now_add=True)
    created_ip_address = models.GenericIPAddressField(editable=False, null=True, blank=True)

    email = models.EmailField()

    def __str__(self):
        return self.email
