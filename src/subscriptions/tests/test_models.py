import pytest

from subscriptions import models
from subscriptions.tests import factories as facs

pytestmark = pytest.mark.django_db(transaction=True)


class TestCostCenter(object):

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
