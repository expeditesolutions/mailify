import pytest

from django.core.urlresolvers import reverse
from django.core import mail

from rest_framework.test import APIClient
from subscriptions import models


API_VERSION = '1.0'


@pytest.mark.django_db(transaction=True)
def test_root_get():
    client = APIClient()
    url = reverse('rest_api:root', kwargs=dict(version=API_VERSION))
    assert url == '/api/1.0/'
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db(transaction=True)
def test_subscriptions_get():
    client = APIClient()
    url = reverse('rest_api:subscription-list', kwargs=dict(version=API_VERSION))
    assert url == '/api/1.0/subscriptions/'
    assert len(mail.outbox) == 0

    response = client.get(url)
    assert response.status_code == 405  # invalid method
    assert len(mail.outbox) == 0


@pytest.mark.django_db(transaction=True)
def test_subscriptions_post_invalid():
    client = APIClient()
    url = reverse('rest_api:subscription-list', kwargs=dict(version=API_VERSION))
    assert url == '/api/1.0/subscriptions/'
    assert len(mail.outbox) == 0

    response = client.post(url)
    assert response.status_code == 400  # no email adress is found
    assert len(response.data) == 1 # only email is returned
    assert response.data['email'][0] == 'This field is required.'
    assert len(mail.outbox) == 0


@pytest.mark.django_db(transaction=True)
def test_subscriptions_post_invalid2():
    client = APIClient()
    url = reverse('rest_api:subscription-list', kwargs=dict(version=API_VERSION))
    assert url == '/api/1.0/subscriptions/'
    assert len(mail.outbox) == 0

    # invalid email address
    response2 = client.post(url, data={'email': 'info@@foo.com'})
    assert response2.status_code == 400  # no email adress is found
    assert len(response2.data) == 1 # only email is returned
    assert response2.data['email'][0] == 'Enter a valid email address.'
    assert len(mail.outbox) == 0


@pytest.mark.django_db(transaction=True)
def test_subscriptions_post_valid():
    client = APIClient()
    url = reverse('rest_api:subscription-list', kwargs=dict(version=API_VERSION))
    assert url == '/api/1.0/subscriptions/'
    assert len(mail.outbox) == 0

    # valid email address
    response2 = client.post(url, data={'email': 'info@foo.com'})
    assert response2.status_code == 201  # no email adress is found
    assert response2.data['email'] == 'info@foo.com'
    assert 'created_ip_address' in response2.data
    assert 'created' in response2.data
    assert len(mail.outbox) == 1
    sub1 = models.Subscription.objects.get(email='info@foo.com')
    assert sub1.sent_emails == 1

    # valid email address duplicate
    response3 = client.post(url, data={'email': 'info@foo.com'})
    assert response3.status_code == 201  # no email adress is found
    assert response3.data['email'] == 'info@foo.com'
    assert 'created_ip_address' not in response3.data
    assert 'created' not in response3.data
    assert len(mail.outbox) == 2
    sub1 = models.Subscription.objects.get(email='info@foo.com')
    assert sub1.sent_emails == 2


@pytest.mark.django_db(transaction=True)
def test_subscriptions_stress_test():
    client = APIClient()
    url = reverse('rest_api:subscription-list', kwargs=dict(version=API_VERSION))
    assert url == '/api/1.0/subscriptions/'

    for i in range(15):
        client.post(url, data={'email': 'info@foo.com'})

    response = client.post(url, data={'email': 'info@foo.com'})
    assert response.status_code == 429
    assert 'Request was throttled. Expected available in' in response.data['detail']
