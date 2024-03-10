import re
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.core.cache import cache


from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.response import Response
from rest_framework import serializers


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        print(data)
        return data

class MyTokenView(TokenObtainPairView):
    serializer_class = MyTokenSerializer
    def post(self, request, *args, **kwargs):
        print(request)
        return super().post(request, *args, **kwargs)

class Hook(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class Proxy(APIView):
    permission_classes = (AllowAny,)
    def post(sels, request, *args, **kwargs):
        print('start POST')
        code = 12345
        serializer = Hook(data=request.data)
        if 'confirmation_code' in request.data:
            print('hello world')
            TokenObtainPairView(**cache.get('user_data'))

        else:
            if serializer.is_valid():
                to_whom_send = get_user_model().objects.get(username=serializer.data.get('username'))
                cache.set('user_data', request.data)
                send_mail(
                    subject='Authentificated',
                    message=f'this is code: {code}',
                    from_email='admin@admin.com',
                    recipient_list=[to_whom_send.email],
                    fail_silently=True,
                )
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)



