import json
import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_get_orders(authenticate_user, create_orders):
    client = authenticate_user
    url = reverse('orders')
    response = client.get(url, format='json')
    data = response.content
    data2 = json.loads(response.content)
    assert response.status_code == 200
    assert len(data) > 1
    assert data2[0].get('details') == 'for 10 people'


@pytest.mark.django_db
def test_create_order(authenticate_user, create_cake):
    client = authenticate_user
    url = reverse('orders')
    data = {
        'cake_id': 1,
    }
    response = client.post(url, data, fromat='json')
    data2 = json.loads(response.content)
    assert response.status_code == 200
    assert data2.get('finished') == False

