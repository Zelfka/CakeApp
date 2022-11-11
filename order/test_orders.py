import json
import pytest
from django.urls import reverse
from addict import Dict


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