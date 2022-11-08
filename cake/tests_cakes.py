import json
import pytest
from django.urls import reverse
from .models import PriceList


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

@pytest.mark.django_db
def test_create_pricelist(authenticate_user):
    client = authenticate_user
    url = reverse('price_list')
    data = {
            "sachr": 700,
            "schwarzwald": 600,
            "chocolate": 650,
            "vanilla": 680,
            "fruit": 750,
            "cheesecake": 700,
            "carrot": 650,
            "pumpkin": 670
        }
    response = client.post(url, data, format='json')
    pricelist = PriceList.objects.filter().last()
    assert response.status_code == 200
    assert pricelist.sachr_cake == 700

@pytest.mark.django_db
def test_update_price(authenticate_user, create_pricelist):
    client = authenticate_user
    url = reverse('price_list')
    data = {
        "name": "sachr_cake",
        "price": 830
    }
    client.put(url, data, format='json')
    price_list = PriceList.objects.filter().last()
    new_price = price_list.sachr_cake
    assert new_price == 830


@pytest.mark.django_db
def test_get_price_list(authenticate_user, create_pricelist):
    client = authenticate_user
    url = reverse('price_list')
    response = client.get(url, format='json')
    data = json.loads(response.content)
    assert response.status_code == 200
    assert data.get('sachr_cake') == 700


@pytest.mark.django_db
def test_get_price_list_with_no_price_list_created(authenticate_user):
    client = authenticate_user
    url = reverse('price_list')
    response = client.get(url, format='json')
    data = json.loads(response.content)
    assert response.status_code == 400
    assert data.get('detail') == 'No pricelist found'