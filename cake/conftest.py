import pytest
from django.urls import reverse
from user.models import MyUser
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
    client.post(url, data, format='json')
    yield create_user


@pytest.fixture
def create_orders(login_user):
    user = login_user
    Order.objects.create(user=user, details='for 10 people')
    Order.objects.create(user=user)


@pytest.fixture
def create_cake(create_orders):
    cake = Cake.objects.create(name='Cake', description='Yummy cake')
    order = Order.objects.filter(pk=1).first()
    cake.order = order
    cake.save()


@pytest.fixture
def authenticate_user(login_user):
    user = login_user
    client = APIClient()
    client.force_authenticate(user)
    yield client



