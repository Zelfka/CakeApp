import json
import pytest
from django.urls import reverse
from addict import Dict
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_get_order(authenticate_user, create_order):
    client = authenticate_user
    url = reverse('order')
    response = client.get(url, format='json')
    data = Dict(response.json())
    assert response.status_code == 200
    assert data.sum_cakes == 1


@pytest.mark.django_db
def test_create_order(authenticate_user, create_cake):
    client = authenticate_user
    url = reverse('order')
    data = {
        'cake_id': 1,
    }
    response = client.post(url, data, fromat='json')
    data2 = json.loads(response.content)
    assert response.status_code == 200
    assert data2.get('finished') == False


@pytest.mark.django_db
def test_close_order(authenticate_user, create_order):
    client = authenticate_user
    url = reverse('order')
    data = {
        'date': '2022-12-11',
        'details': 'For 10 people'
    }
    response = client.put(url, data, format='json')
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_cake_from_order(authenticate_user, create_order):
    client = authenticate_user
    url = reverse('order_delete', kwargs={'id': 1})
    response = client.delete(url, format='json')
    assert response.status_code == 202


def test_get_all_orders(admin_user, create_order):
    client = APIClient()
    client.force_authenticate(admin_user)
    url = reverse('admin_orders')
    response = client.get(url, format='json')
    data = json.loads(response.content)
    assert response.status_code == 200
    assert data[0].get('state') == 'Open'
    assert len(data) == 1


def test_filter_orders(admin_user, create_order):
    client = APIClient()
    client.force_authenticate(admin_user)
    url = reverse('admin_orders')
    data = {
        'name': 'ake',
        'state': 'Open'
    }
    response = client.post(url, data, format='json')
    data = json.loads(response.content)
    assert response.status_code == 200
    assert data[0].get('id') == 1


def test_change_order_state(admin_user, create_order):
    client = APIClient()
    client.force_authenticate(admin_user)
    url = reverse('admin_orders')
    data = {
        'order_id': 1
    }
    response = client.put(url, data, format='json')
    assert response.status_code == 200


def test_delete_order(admin_user, create_order):
    client = APIClient()
    client.force_authenticate(admin_user)
    url = reverse('admin_orders_delete', kwargs={'id': 1})
    response = client.delete(url, format='json')
    assert response.status_code == 202
