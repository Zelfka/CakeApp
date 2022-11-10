import json
import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_get_all_cakes(authenticate_user, create_cake):
    client = authenticate_user
    url = reverse('cakes')
    response = client.get(url, format='json')
    data = json.loads(response.content)
    assert response.status_code == 200
    assert data[0].get('name') == 'Cake'


@pytest.mark.django_db
def test_create_cake(authenticate_user):
    client = authenticate_user
    url = reverse('cakes')
    data = {
        'name': 'Sachr',
        'description': 'Old fashioned cake',
        'milk_free': True,
        'eggs_free': False,
        'price': 320
    }
    response = client.post(url, data, format='json')
    data = json.loads(response.content)
    assert response.status_code == 200
    assert data.get('name') == 'Sachr'
    assert data.get('milk_free') == True


@pytest.mark.django_db
def test_create_cake_without_name(authenticate_user):
    client = authenticate_user
    url = reverse('cakes')
    data = {
        'name': None,
        'description': 'Old fashioned cake',
        'milk_free': True,
        'eggs_free': False,
        'price': 320
    }
    response = client.post(url, data, format='json')
    data = json.loads(response.content)
    assert response.status_code == 400
    assert data.get('detail') == 'Name and description have to be filled out.'


@pytest.mark.django_db
def test_get_one_cake(authenticate_user, create_cake):
    client = authenticate_user
    url = reverse('one_cake', kwargs={'cake': 'Cake'})
    response = client.get(url, format='json')
    data = json.loads(response.content)
    assert response.status_code == 200
    assert data.get('name') == 'Cake'


def test_get_change_cake(admin_user, create_cake):
    client = APIClient()
    client.force_authenticate(admin_user)
    url = reverse('cake_update', kwargs={'pk': 1})
    response = client.get(url, format='json')
    data = json.loads(response.content)
    assert response.status_code == 200
    assert data.get('name') == 'Cake'


@pytest.mark.django_db
def test_get_change_cake_normal_user(authenticate_user, create_cake):
    client = authenticate_user
    url = reverse('cake_update', kwargs={'pk': 1})
    response = client.get(url, format='json')
    assert response.status_code == 403


def test_update_cake(admin_user, create_cake):
    client = APIClient()
    client.force_authenticate(admin_user)
    data = {
        'name': 'New Cake'
    }
    url = reverse('cake_update', kwargs={'pk': 1})
    response = client.put(url, data, format='json')
    assert response.status_code == 200


@pytest.mark.django_db
def test_update_cake(authenticate_user, create_cake):
    client = authenticate_user
    data = {
        'name': 'New Cake'
    }
    url = reverse('cake_update', kwargs={'pk': 1})
    response = client.put(url, data, format='json')
    assert response.status_code == 403
