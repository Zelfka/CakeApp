import pytest
from django.urls import reverse
from .models import MyUser
from .models import Order
from cake.models import Cake
from rest_framework.test import APIClient

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


@pytest.fixture
def create_cake():
    cake = Cake.objects.create(name='Cake', description='Yummy cake', price=700)
    yield cake


@pytest.fixture
def create_order(login_user, create_cake):
    user = login_user
    oder = Order.objects.create(user=user, details='for 10 people')
    cake= create_cake
    oder.cakes.add(cake)
    oder.save()

@pytest.fixture
def authenticate_user(login_user):
    user = login_user
    client = APIClient()
    client.force_authenticate(user)
    yield client