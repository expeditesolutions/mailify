import pytest

from django.conf import settings
from django.core import mail

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
        sub1 = facs.SubscriptionFactory(email='foo@example.com')
        sub2 = facs.SubscriptionFactory(email='foo@example.com')

        assert models.Subscription.objects.count() == 2
        assert sub1.sent_emails == 0, 'no sending email on save'
        assert sub2.sent_emails == 0, 'no sending email on save'

    def test_notify(self):
        """
        Notifying a subscription should send out an email
        """
        assert models.Voucher.get_code() == 'pindakaas'

        # mailbox is empty to start
        assert len(mail.outbox) == 0
        sub1 = facs.SubscriptionFactory(email='foo@example.com')
        assert sub1.sent_emails == 0
        assert len(mail.outbox) == 0, 'no emails should be send on save'
        sub1.notify()
        assert sub1.sent_emails == 1
        assert len(mail.outbox) == 1
        email1 = mail.outbox[0]
        assert email1.subject == 'Here is Your Promo Code!'
        assert len(email1.to) == 1
        assert email1.to[0] == sub1.email
        assert email1.from_email == settings.DEFAULT_FROM_EMAIL
        assert 'Here is your voucher' in email1.body
        assert 'pindakaas' in email1.body

    def test_increase_sent_emails(self):
        sub1 = facs.SubscriptionFactory(email='foo@example.com')
        assert sub1.sent_emails == 0
        sub1.increase_sent_emails()
        assert sub1.sent_emails == 1
        sub1.increase_sent_emails()
        sub1.increase_sent_emails()
        assert sub1.sent_emails == 3


class TestVoucher(object):

    def test__str__(self):
        voucher1 = facs.VoucherFactory(code='pindakaas')

        assert str(voucher1) == 'pindakaas'

    def test_get_code(self):
        facs.VoucherFactory(code='pindakaas')
        assert models.Voucher.get_code() == 'pindakaas'
