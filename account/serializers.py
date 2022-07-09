from account.models import CustomUser, Profession
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ('password', 'groups', 'user_permissions')
        depth = 1