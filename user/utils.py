from rest_framework_simplejwt.tokens import RefreshToken


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
