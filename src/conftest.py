import pytest
from subscriptions.tests.factories import VoucherFactory


@pytest.fixture(autouse=True)
def default_voucher():
    return VoucherFactory(code='pindakaas')
