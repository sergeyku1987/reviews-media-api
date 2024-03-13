from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.core.cache import cache
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import Token

from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication


from users.permissions import IsRole, IsEmptyRequest
from users.serializers import (
    UserSerializer, UserModelSerializer, RegistrationSerializer, MyTokenSerializer
)

CODE = '1234'


class TokenView(APIView):
    permission_classes = AllowAny, 

    def post(self, request, *args, **kwargs):
        print('post token view')

        if 'username' not in request.data:
            return Response(status=400)

        if not get_user_model().objects.filter(username=request.data.get('username')).exists():
            print('not exist')
            return Response({}, status=404)

        if request.data.get('confirmation_code') != CODE:
            return Response(status=400)

        serializer = MyTokenSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=200)
        return Response(serializer.errors)





class RegistrationView(APIView):
    permission_classes = AllowAny,

    def post(self, request, *args, **kwargs):
        user = request.data.get('username')
        is_user = get_user_model().objects.values('username').filter(username=user).exists()

        email = request.data.get('email')
        is_email = get_user_model().objects.values('email').filter(email=email).exists()

        user_email = get_user_model().objects.values(
            'username', 'email'
            ).filter(username=user)
        if user_email:
            user_db, email_db = user_email[0].get('username'), user_email[0].get('email')
            if (user_db == user) and (email_db != email):
                return Response(status=400)
        
        if is_email and not is_user:
            return Response(status=400)

        if request.data.get('username') == 'me':
            return Response(status=400)

        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            send_mail(
                    subject='Authentificated',
                    message=f'this is code: {CODE}',
                    from_email='admin@admin.com',
                    recipient_list=[request.data.get('email')],
                    fail_silently=True,
                )
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)  


class UserViewSet(ModelViewSet):
    queryset = get_user_model()
    serializer_class = UserModelSerializer
   # permission_classes = (IsEmptyRequest, IsRole)#(IsAdminUser, IsAuthenticated)


    def create(self, request, *args, **kwargs):
        print('creata view set')
        return super().create(request, *args, **kwargs)

    @action(methods=['get', 'post', 'patch'], detail=False)
    def me(self, request):
        if request.method == 'PATCH' or request.method == 'POST':
            serializer = self.serializer_class(
                instance=get_user_model().objects.get(username=request.user.username),
                data=request.data,
                partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({})

        # if request.method == 'GET':
        #     user_name, token = JWTAuthentication().authenticate(request)
        #     print(token.payload)
        #     user = get_user_model().objects.get(username=user_name)
        #return Response(UserSerializer(user).data)
