from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueTogetherValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import re

from django.shortcuts import get_object_or_404


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    bio = serializers.CharField()
    role = serializers.CharField(read_only=True)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.save()
        return instance

    def validate_username(self, value):
        if len(value) >= 150:
            raise serializers.ValidationError("Blog post is not about Django")
        if bool(re.search(value, r'^[\w.@+-]+\Z')):
            raise serializers.ValidationError("Blog post is not about Django")
        return value

    def validate_first_name(self, value):
        if len(value) >= 150:
            raise serializers.ValidationError("Blog post is not about Django")
        return value

    def validate_last_name(self, value):
        if len(value) >= 150:
            raise serializers.ValidationError("Blog post is not about Django")
        return value

    def validate_email(self, value):
        if len(value) >= 254:
            raise serializers.ValidationError("Blog post is not about Django")
        return value


class RoleField(serializers.ChoiceField):
    def to_representation(self, value):
        return self.choices[value]

    def to_internal_value(self, data):
        if data in self.choices.values():
            for k, v in self.choices.items():
                if v == data:
                    return k
        else:
            raise TypeError

class UserModelSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)
    role = RoleField(
        choices=get_user_model().Status.choices,
        default=get_user_model().Status.USER,
        )
    
    def validate_username(self, value):
        if len(value) >= 150:
            raise serializers.ValidationError("")
        if bool(re.search(value, r'^[\w.@+-]+\Z')):
            raise serializers.ValidationError("")
        return value
    
    def validate_first_name(self, value):
        if len(value) >= 150:
            raise serializers.ValidationError("")
        return value

    def validate_last_name(self, value):
        if len(value) >= 150:
            raise serializers.ValidationError("")
        return value
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'role')
    
    def create(self, validated_data):
        print('serializer user model create')
        print(validated_data)
        return super().create(validated_data)


class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()

    # class Meta:
    #     validators = [
    #         UniqueTogetherValidator(
    #             queryset=get_user_model().objects.all(),
    #             fields=['username', 'email']
    #         )
    #     ]

    def create(self, validated_data):
        print('create')
        user, status = get_user_model().objects.get_or_create(**validated_data)
        #if not status:
            #return get_user_model().objects.create(**validated_data)
        return user

    def validate_email(self, value):
        if len(value) >= 254:
            raise serializers.ValidationError("")
        return value

    def validate_username(self, value):
        if len(value) >= 150:
            raise serializers.ValidationError("")
        if bool(re.search(value, r'^[\w.@+-]+\Z')):
            raise serializers.ValidationError("")
        return value


class MyTokenSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[self.username_field] = serializers.CharField()
        del self.fields['password']

    def validate(self, attrs):
        data = {}
        #usr = get_user_model().objects.get(username=attrs.get('username'))
        usr = get_object_or_404(
            get_user_model(),
            username=attrs.get('username')
        )
        refresh = self.get_token(usr)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        print(refresh.access_token.payload)
        return data

