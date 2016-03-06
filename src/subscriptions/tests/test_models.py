import pytest

from subscriptions import models
from subscriptions.tests import factories as facs

pytestmark = pytest.mark.django_db(transaction=True)


class TestSubscription(object):

    def test__str__(self):
        subscription1 = facs.SubscriptionFactory(email='foo@example.com')
        assert str(subscription1) == 'foo@example.com'

    def test_save(self):
        """
        Saving a duplicate emailaddress should be possible
        """
        facs.SubscriptionFactory(email='foo@example.com')
        facs.SubscriptionFactory(email='foo@example.com')

        assert models.Subscription.objects.count() == 2


class TestVoucher(object):

    def test__str__(self):
        voucher1 = facs.VoucherFactory(code='pindakaas')

        assert str(voucher1) == 'pindakaas'
