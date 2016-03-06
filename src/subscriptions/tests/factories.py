import factory


class SubscriptionFactory(factory.django.DjangoModelFactory):
    email = factory.sequence(lambda n: 'foo{0}@example.com'.format(n))
    created_ip_address = '127.0.0.1'

    class Meta:
        model = 'subscriptions.Subscription'


class VoucherFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'subscriptions.Voucher'
