from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MyUser
from .serializers import MyUserRequestRegistrationSerializer, MyUserResponseRegistrationSerializer, \
    ProfileResponseSerializer
from .utils import generate_token, get_data, check_if_logged_in_user_is_the_same_user,find_user_by_id
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated


class RegisterView(APIView):

    def post(self, request):
        data = get_data(request)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        password2 = data.get('password2')
        if len(username) == 0 or len(email) == 0 or len(password) == 0 or len(password2) == 0:
            return Response({'detail': 'All fields are required!'}, status=status.HTTP_400_BAD_REQUEST)
        if len(password) < 8:
            return Response({'detail': 'Password must be at least 8 characters long'},
                            status=status.HTTP_400_BAD_REQUEST)
        if password != password2:
            return Response({'detail': 'Passwords don\'t match'}, status=status.HTTP_400_BAD_REQUEST)

        user_instance = MyUser.objects.filter(username=username).first()
        if user_instance:
            return Response({'detail': 'User with this username already exists, please choose different one'},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = MyUserRequestRegistrationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            user_instance = MyUser.objects.filter(username=username).first()
            user_instance.set_password(data.get('password'))
            user_instance.save()
            response_serializer = MyUserResponseRegistrationSerializer(user_instance)
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        data = get_data(request)
        if len(data.get('username')) == 0 or len(data.get('password')) == 0:
            return Response({'detail': 'Both fields must be filled out.'}, status=status.HTTP_400_BAD_REQUEST)

        user_instance = MyUser.objects.filter(username=data.get('username')).first()
        if not user_instance:
            return Response({'detail': 'No user with such username exists!'}, status=status.HTTP_400_BAD_REQUEST)
        if not user_instance.check_password(data.get('password')):
            return Response({'detail': 'Wrong password, try again.'}, status=status.HTTP_400_BAD_REQUEST)
        user_instance = authenticate(request, username=data.get('username'), password=data.get('password'))

        tokens = generate_token(user_instance)
        login(request, user_instance)
        return Response({
            'refresh': tokens.get('refresh'),
            'access': tokens.get('access'),
            'id': user_instance.pk,
            'username': user_instance.username,
            'admin': user_instance.is_staff
        }, status=status.HTTP_200_OK)


class LogoutView(APIView):

    def post(self, request):
        logout(request)
        return Response({'detail': 'Logout successful.'}, status=status.HTTP_200_OK)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        response = check_if_logged_in_user_is_the_same_user(request, pk)
        if response:
            return response
        user = find_user_by_id(pk)
        if user is None:
            return Response({'detail': 'No such profile found, wrong id.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProfileResponseSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        response = check_if_logged_in_user_is_the_same_user(request, pk)
        if response:
            return response
        user = find_user_by_id(pk)
        if user is None:
            return Response({'detail': 'No such profile found, wrong id.'}, status=status.HTTP_400_BAD_REQUEST)

        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        street = request.data.get('street')
        city = request.data.get('city')
        zip_code = request.data.get('zip_code')
        phone = request.data.get('phone')

        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.street = street
        user.city = city
        user.zip_code = zip_code
        user.phone = phone

        user.save()
        serializer = ProfileResponseSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

