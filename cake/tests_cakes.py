import json
import pytest
from django.urls import reverse


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
        'milk_free': True
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
        'milk_free': True
    }
    response = client.post(url, data, format='json')
    data = json.loads(response.content)
    assert response.status_code == 400
    assert data.get('detail') == 'Name and description have to be filled out.'


@pytest.mark.django_db
def test_get_one_cake(authenticate_user, create_cake):
    client = authenticate_user
    url = reverse('one_cake', kwargs={'cake':'Cake'})
    response = client.get(url, format='json')
    data = json.loads(response.content)
    assert response.status_code == 200
    assert data.get('name') == 'Cake'


@pytest.mark.django_db
def test_get_cake_by_order(authenticate_user, create_cake):
    client = authenticate_user
    url = reverse('cake_order', kwargs={'order_id': 1})
    response = client.get(url, format='json')
    data = json.loads(response.content)
    assert response.status_code == 200
    assert data[0].get('name') == 'Cake'
