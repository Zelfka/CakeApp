from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .models import MyUser


def get_data(request):
    data = {
        'username': request.data.get('username'),
        'email': request.data.get('email'),
        'password': request.data.get('password'),
        'password2': request.data.get('password2')
    }
    return data


def generate_token(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def check_if_logged_in_user_is_the_same_user(request, pk):
    if request.user.id != pk:
        response = Response()
        response.status_code = 400
        response.data = {'detail': 'You are not allowed to access this profile'}
        return response


def find_user_by_id(pk):
    user = MyUser.objects.filter(pk=pk).first()
    return user
