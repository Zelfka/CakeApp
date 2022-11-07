import pytest
from django.urls import reverse
from .models import MyUser


@pytest.fixture
def create_user(client):
    url = reverse('register')
    data = {
        'username': 'Veronika',
        'email': 'test@test.com',
        'password': '123456pass',
        'password2': '123456pass'
    }
    client.post(url, data, format='json')
    user = MyUser.objects.filter().last()
    yield user


@pytest.fixture
def login_user(client, create_user):
    url = reverse('login')
    data = {
        'username': 'Veronika',
        'password': '123456pass'
    }
    client.post(url,data, format='json')
    yield create_user



