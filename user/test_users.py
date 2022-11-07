import json
import pytest
from django.urls import reverse
from .models import MyUser
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_register(client):
    url = reverse('register')
    data = {
        'username': 'veverka',
        'email': 'test@test.com',
        'password': '123456pass',
        'password2': '123456pass'
    }
    response = client.post(url, data, format='json')
    user = MyUser.objects.filter().last()
    assert response.status_code == 200
    assert user.username == 'veverka'


@pytest.mark.django_db
def test_register_without_name(client):
    url = reverse('register')
    data = {
        'username': '',
        'email': 'test@test.com',
        'password': '123456pass',
        'password2': '123456pass'
    }
    response = client.post(url, data, format='json')
    data2 = json.loads(response.content)
    assert response.status_code == 400
    assert data2.get('detail') == 'All fields are required!'


@pytest.mark.django_db
def test_profile(login_user):
    client = APIClient()
    user = login_user
    client.force_authenticate(user)
    url = reverse('profile', kwargs={'pk': 1})
    response = client.get(url, format='json')
    data = json.loads(response.content)
    assert response.status_code == 200
    assert user.username == data.get('username')